"""
Unit tests for Memory Allocation Simulator backend
Run with: python -m pytest tests.py
Or simply: python tests.py
"""

import sys
from backend.memory import Memory, MemoryBlock
from backend.analyzer import FragmentationAnalyzer


class TestMemoryAllocation:
    """Test memory allocation functionality"""
    
    def test_first_fit_allocation(self):
        """Test First Fit allocation strategy"""
        memory = Memory(1000)
        
        # Allocate first process
        success, block, msg = memory.allocate(100, 'first_fit')
        assert success, "First allocation should succeed"
        assert block.process_id == "P1", "First process should be P1"
        assert block.start == 0, "First process should start at 0"
        assert block.size == 100, "First process should have size 100"
        
        # Allocate second process
        success, block, msg = memory.allocate(150, 'first_fit')
        assert success, "Second allocation should succeed"
        assert block.process_id == "P2", "Second process should be P2"
        assert block.start == 100, "Second process should start at 100"
        
        print("✓ First Fit allocation test passed")
    
    def test_best_fit_allocation(self):
        """Test Best Fit allocation strategy"""
        memory = Memory(1000)
        
        # Allocate processes with gaps
        memory.allocate(50, 'best_fit')
        memory.allocate(300, 'best_fit')
        memory.allocate(100, 'best_fit')
        
        # Free middle block to create gaps
        memory.deallocate("P2")
        
        # Now allocate a process that fits best (best fit should use the 300 KB gap)
        success, block, msg = memory.allocate(250, 'best_fit')
        assert success, "Best fit allocation should succeed"
        # Best fit should allocate in the gap that was freed (which is at position 50)
        assert block.process_id == "P4", "Should be the 4th process"
        
        print("✓ Best Fit allocation test passed")
    
    def test_worst_fit_allocation(self):
        """Test Worst Fit allocation strategy"""
        memory = Memory(1000)
        
        # Create fragmentation
        memory.allocate(100, 'worst_fit')
        memory.allocate(100, 'worst_fit')
        memory.allocate(100, 'worst_fit')
        
        # Deallocate to create free blocks
        memory.deallocate("P2")  # Creates 100 KB gap
        
        # Allocate should use largest block
        success, block, msg = memory.allocate(50, 'worst_fit')
        assert success, "Worst fit allocation should succeed"
        
        print("✓ Worst Fit allocation test passed")
    
    def test_deallocation(self):
        """Test process deallocation"""
        memory = Memory(1000)
        
        # Allocate processes
        memory.allocate(100, 'first_fit')
        memory.allocate(150, 'first_fit')
        
        # Check allocated count
        assert len(memory.get_allocated_processes()) == 2, "Should have 2 allocated blocks"
        
        # Deallocate
        success, msg = memory.deallocate("P1")
        assert success, "Deallocation should succeed"
        assert len(memory.get_allocated_processes()) == 1, "Should have 1 allocated block"
        
        # Check free blocks were merged
        free_blocks = memory.get_free_blocks()
        assert any(b.size >= 100 for b in free_blocks), "Should have merged free blocks"
        
        print("✓ Deallocation test passed")
    
    def test_memory_merge(self):
        """Test adjacent free block merging"""
        memory = Memory(1000)
        
        # Create pattern: [Free 100][Allocate 100][Allocate 100][Free 700]
        memory.allocate(100, 'first_fit')
        memory.allocate(100, 'first_fit')
        
        # Deallocate both
        memory.deallocate("P1")
        memory.deallocate("P2")
        
        # Should have merged back to original state
        free_blocks = memory.get_free_blocks()
        assert len(free_blocks) == 1, "Should have single free block after merge"
        assert free_blocks[0].size == 1000, "Should have all memory free"
        
        print("✓ Memory merge test passed")
    
    def test_insufficient_memory(self):
        """Test allocation with insufficient memory"""
        memory = Memory(500)
        
        # Fill most memory
        memory.allocate(450, 'first_fit')
        
        # Try to allocate more than available
        success, block, msg = memory.allocate(100, 'first_fit')
        assert not success, "Should fail with insufficient memory"
        
        print("✓ Insufficient memory test passed")
    
    def test_fragmentation_calculation(self):
        """Test fragmentation analysis"""
        memory = Memory(1000)
        
        # Create fragmentation
        memory.allocate(100, 'first_fit')
        memory.allocate(100, 'first_fit')
        memory.allocate(100, 'first_fit')
        memory.deallocate("P2")  # Create gap
        
        # Calculate fragmentation
        ext_frag = FragmentationAnalyzer.calculate_external_fragmentation(memory)
        util = FragmentationAnalyzer.calculate_memory_utilization(memory)
        
        assert 0 <= ext_frag <= 100, "External fragmentation should be 0-100%"
        assert 0 <= util <= 100, "Utilization should be 0-100%"
        assert util == 20, "Utilization should be 20% (200/1000)"
        
        print("✓ Fragmentation calculation test passed")
    
    def test_statistics(self):
        """Test memory statistics"""
        memory = Memory(1000)
        
        memory.allocate(100, 'first_fit')
        memory.allocate(200, 'first_fit')
        
        analysis = FragmentationAnalyzer.analyze_fragmentation(memory)
        
        assert analysis['allocated_space'] == 300, "Should have 300 KB allocated"
        assert analysis['free_space'] == 700, "Should have 700 KB free"
        assert analysis['number_of_allocated_blocks'] == 2, "Should have 2 blocks"
        assert analysis['memory_utilization'] == 30.0, "Utilization should be 30%"
        
        print("✓ Statistics test passed")


def run_tests():
    """Run all tests"""
    print("=" * 60)
    print("Running Memory Allocation Simulator Tests".center(60))
    print("=" * 60)
    
    test_suite = TestMemoryAllocation()
    
    tests = [
        test_suite.test_first_fit_allocation,
        test_suite.test_best_fit_allocation,
        test_suite.test_worst_fit_allocation,
        test_suite.test_deallocation,
        test_suite.test_memory_merge,
        test_suite.test_insufficient_memory,
        test_suite.test_fragmentation_calculation,
        test_suite.test_statistics,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ {test.__name__} failed: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__} error: {e}")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"Tests Complete: {passed} passed, {failed} failed".center(60))
    print("=" * 60)
    
    return failed == 0


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
