"""
Demo script to test memory allocation simulator programmatically
Shows how to use the backend directly without the GUI
"""

from backend.memory import Memory
from backend.analyzer import FragmentationAnalyzer

def demo_memory_simulator():
    """Demonstrate memory allocation simulator"""
    
    print("=" * 70)
    print("MEMORY ALLOCATION SIMULATOR - DEMO".center(70))
    print("=" * 70)
    
    # Create memory system with 1000 KB
    memory = Memory(total_memory_size=1000)
    
    # ========== FIRST FIT DEMO ==========
    print("\n1. FIRST FIT ALLOCATION")
    print("-" * 70)
    
    processes_ff = [100, 150, 200, 50, 80]
    for size in processes_ff:
        success, block, msg = memory.allocate(size, strategy='first_fit')
        print(f"   Allocate {size} KB: {msg}")
        if success:
            print(f"      → Allocated at address {block.start} KB")
    
    # Show statistics
    print("\n   Current Memory State (First Fit):")
    report = FragmentationAnalyzer.get_fragmentation_report(memory)
    print(report)
    
    # ========== DEALLOCATE DEMO ==========
    print("\n2. DEALLOCATION EXAMPLE")
    print("-" * 70)
    
    success, msg = memory.deallocate("P2")
    print(f"   Deallocate P2: {msg}")
    
    print("\n   Memory State After Deallocation:")
    report = FragmentationAnalyzer.get_fragmentation_report(memory)
    print(report)
    
    # ========== RESET AND BEST FIT DEMO ==========
    memory.reset()
    print("\n3. BEST FIT ALLOCATION")
    print("-" * 70)
    
    processes_bf = [100, 150, 200, 50, 80]
    for size in processes_bf:
        success, block, msg = memory.allocate(size, strategy='best_fit')
        print(f"   Allocate {size} KB: {msg}")
        if success:
            print(f"      → Allocated at address {block.start} KB")
    
    print("\n   Current Memory State (Best Fit):")
    report = FragmentationAnalyzer.get_fragmentation_report(memory)
    print(report)
    
    # ========== RESET AND WORST FIT DEMO ==========
    memory.reset()
    print("\n4. WORST FIT ALLOCATION")
    print("-" * 70)
    
    processes_wf = [100, 150, 200, 50, 80]
    for size in processes_wf:
        success, block, msg = memory.allocate(size, strategy='worst_fit')
        print(f"   Allocate {size} KB: {msg}")
        if success:
            print(f"      → Allocated at address {block.start} KB")
    
    print("\n   Current Memory State (Worst Fit):")
    report = FragmentationAnalyzer.get_fragmentation_report(memory)
    print(report)
    
    # ========== FRAGMENTATION COMPARISON ==========
    print("\n5. SUMMARY")
    print("-" * 70)
    print("   This demo shows how different allocation strategies affect:")
    print("   • Memory utilization")
    print("   • External fragmentation")
    print("   • Block allocation patterns")
    print("   • Memory compaction and merging")
    print("\n   Run 'python main.py' to launch the interactive GUI version!")
    print("=" * 70)

if __name__ == "__main__":
    demo_memory_simulator()
