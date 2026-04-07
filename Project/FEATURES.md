# Memory Allocation Simulator - Features & Documentation

## 📋 Project Overview

A fully functional desktop application for simulating **contiguous memory allocation techniques** in operating systems, featuring three allocation strategies (First Fit, Best Fit, Worst Fit) with visual analysis of fragmentation.

---

## ✨ Core Features

### 1. Memory Allocation Strategies ✅
- **First Fit**: Allocates memory in the first available block large enough to hold the process
- **Best Fit**: Allocates memory in the smallest available block that fits the process
- **Worst Fit**: Allocates memory in the largest available block to reduce fragmentation

### 2. Memory Management Operations ✅
- **Allocate Process**: Add new process with configurable size
- **Deallocate Process**: Remove process and free its memory
- **Automatic Merging**: Adjacent free blocks are automatically combined
- **Memory Reset**: Clear all allocations and restart

### 3. Visualization Features ✅
- **Real-time Memory Layout**: Color-coded visual representation of memory blocks
- **Dynamic Canvas**: Automatically scales and updates with allocations
- **Color Coding**: Different color for each allocated process, cyan for free space
- **Address Scale**: Memory addresses clearly marked at bottom
- **Block Information**: Each block shows Process ID and size

### 4. Fragmentation Analysis ✅
- **External Fragmentation Calculation**: Measures scattered free memory
  - Formula: `(Total Free - Largest Contiguous) / Total Free × 100%`
- **Internal Fragmentation**: Tracks wasted space within blocks
- **Memory Utilization**: Shows percentage of memory in use
  - Formula: `(Allocated) / (Total) × 100%`
- **Largest Contiguous Block**: Identifies largest available space

### 5. Statistics & Reporting ✅
- **Real-time Metrics**: Memory statistics update instantly
- **Block Counting**: Tracks number of allocated and free blocks
- **Fragmentation Report**: Generate detailed analysis report
- **Memory State Display**: Show current allocation pattern

### 6. User Interface ✅
- **Professional GUI**: Built with tkinter for cross-platform compatibility
- **Intuitive Layout**: Organized panels for strategy, control, and visualization
- **Interactive Controls**: Buttons for allocate, deallocate, reset, and reporting
- **Table View**: List all processes with details (ID, size, start address, end address)
- **Status Display**: Real-time statistics and fragmentation metrics

---

## 📊 Technical Specifications

### Backend Components

#### 1. **Memory Module** (`backend/memory.py`)
```python
- MemoryBlock class
  - Properties: block_id, start, size, allocated, process_id
  - Methods: __repr__

- Memory class
  - allocate(process_size, strategy)
  - deallocate(process_id)
  - _find_suitable_block()
  - _allocate_block()
  - _merge_adjacent_free_blocks()
  - get_memory_state()
  - get_allocated_processes()
  - get_free_blocks()
  - reset()
```

#### 2. **Analyzer Module** (`backend/analyzer.py`)
```python
- FragmentationAnalyzer class (static methods)
  - calculate_external_fragmentation()
  - calculate_internal_fragmentation()
  - calculate_memory_utilization()
  - get_free_space()
  - get_allocated_space()
  - get_largest_free_block()
  - analyze_fragmentation()
  - get_fragmentation_report()
```

### UI Components

#### 1. **Main GUI** (`ui/gui.py`)
```python
- MemoryAllocationSimulator class
  - Canvas for visualization
  - Strategy radio buttons
  - Process allocation controls
  - Process list treeview
  - Statistics display
  - Report generation
  - Methods for all user interactions
```

#### 2. **Visualizer Module** (`ui/visualizer.py`)
```python
- MemoryVisualizer class
  - draw_memory()
  - draw_address_scale()
  - draw_legend()
  
- StatisticsDisplay class (formatting)
  - format_statistics()
```

### Configuration
- `config.py`: Centralized configuration
  - Memory size: 1000 KB
  - UI dimensions: 1200x800
  - Color schemes
  - Font definitions

---

## 🚀 How It Works

### Memory Allocation Flow

```
User Input (Size + Strategy)
    ↓
Memory.allocate(size, strategy)
    ↓
_find_suitable_block(strategy)
    ├─ First Fit: Return first fitting block
    ├─ Best Fit: Return smallest fitting block
    └─ Worst Fit: Return largest block
    ↓
_allocate_block(selected_block)
    ├─ Create allocated block
    ├─ Create remainder free block (if any)
    └─ Sort blocks by start address
    ↓
_merge_adjacent_free_blocks()
    └─ Combine adjacent free spaces
    ↓
Update Visualization & Statistics
```

### Fragmentation Calculation

```
Example Scenario:
Total Memory: 1000 KB
Allocated: 500 KB (4 blocks)
Free: 500 KB in 3 blocks (100KB, 150KB, 250KB)

Largest Contiguous: 250 KB
External Fragmentation = (500 - 250) / 500 × 100 = 50%

Memory Utilization = 500 / 1000 × 100 = 50%
```

---

## 📁 File Structure

```
Memory Allocation Simulator/
│
├── main.py                 [Run this to start GUI]
├── demo.py                 [Console demonstration]
├── tests.py                [Unit tests - 8 tests]
├── config.py               [Configuration settings]
├── requirements.txt        [Dependencies]
│
├── backend/
│   ├── __init__.py
│   ├── memory.py          [Core allocation logic]
│   └── analyzer.py        [Fragmentation analysis]
│
├── ui/
│   ├── __init__.py
│   ├── gui.py             [Main GUI window]
│   └── visualizer.py      [Memory visualization]
│
├── README.md              [Complete documentation]
├── USERGUIDE.md           [User instructions]
└── FEATURES.md            [This file]
```

---

## 🧪 Testing

### Unit Tests (`tests.py`)
8 comprehensive tests covering:
1. **test_first_fit_allocation** - First Fit strategy
2. **test_best_fit_allocation** - Best Fit strategy
3. **test_worst_fit_allocation** - Worst Fit strategy
4. **test_deallocation** - Process removal
5. **test_memory_merge** - Block merging
6. **test_insufficient_memory** - Error handling
7. **test_fragmentation_calculation** - Analysis accuracy
8. **test_statistics** - Statistics calculation

**Run:** `python tests.py`

### Demo Script (`demo.py`)
Demonstrates all three strategies with:
- Automatic allocation of 5 processes
- Fragmentation reports
- Side-by-side comparison
- Console output for learning

**Run:** `python demo.py`

---

## 💾 Key Data Structures

### MemoryBlock
```python
{
    block_id: int,              # Unique identifier
    start: int,                 # Starting address in KB
    size: int,                  # Size in KB
    allocated: bool,            # Is allocated?
    process_id: str             # Process identifier (P1, P2, ...)
}
```

### Fragmentation Analysis Result
```python
{
    'external_fragmentation': float,    # Percentage (0-100)
    'internal_fragmentation': float,    # Percentage (0-100)
    'memory_utilization': float,        # Percentage (0-100)
    'total_memory': int,                # Total KB
    'allocated_space': int,             # Allocated KB
    'free_space': int,                  # Free KB
    'largest_free_block': int,          # Size of largest free block
    'number_of_allocated_blocks': int,  # Count
    'number_of_free_blocks': int        # Count
}
```

---

## 🎯 Use Cases

### Educational
- ✅ Learn memory allocation concepts
- ✅ Understand fragmentation
- ✅ Compare allocation strategies
- ✅ Hands-on OS concepts

### Research
- ✅ Analyze strategy performance
- ✅ Measure fragmentation metrics
- ✅ Test allocation patterns
- ✅ Generate reports

### Demonstration
- ✅ Show memory management visually
- ✅ Illustrate fragmentation problems
- ✅ Compare strategies side-by-side
- ✅ Educational presentations

---

## ⚙️ System Requirements

### Hardware
- CPU: Any modern processor
- RAM: 256MB minimum
- Storage: 10MB

### Software
- **Python**: 3.6 or higher
- **tkinter**: Included with Python
- **OS**: Windows, Linux, macOS (cross-platform)

---

## 🔧 Customization Guide

### Change Memory Size
```python
# In main.py, line ~9
self.memory = Memory(total_memory_size=2000)  # Default: 1000
```

### Modify Colors
```python
# In ui/visualizer.py, line ~17
self.colors = {
    'allocated': '#FF6B6B',      # Change hex colors
    'free': '#95E1D3',
    'border': '#2C3E50',
    'text': '#FFFFFF'
}
```

### Add New Strategy
1. Create method in `Memory` class
2. Update `_find_suitable_block()` method
3. Add radio button in GUI

### Change Window Size
```python
# In main.py
self.root.geometry("1400x900")  # Change dimensions
```

---

## 📈 Algorithm Complexity

| Operation | First Fit | Best Fit | Worst Fit |
|-----------|-----------|----------|-----------|
| Allocate | O(n) | O(n) | O(n) |
| Deallocate | O(n log n) | O(n log n) | O(n log n) |
| Merge | O(n) | O(n) | O(n) |

Where n = number of memory blocks

---

## 🎓 Learning Outcomes

Students will understand:

1. **Memory Management**
   - How OS allocates memory to processes
   - Different allocation strategies
   - Tradeoffs between strategies

2. **Fragmentation**
   - What is external fragmentation
   - What is internal fragmentation
   - How to measure and calculate it
   - Impact on system performance

3. **Data Structures**
   - Memory block representation
   - Block management techniques
   - Sorting and merging blocks

4. **Algorithms**
   - First Fit algorithm
   - Best Fit algorithm
   - Worst Fit algorithm
   - Block merging/compaction

5. **Software Engineering**
   - GUI development with tkinter
   - Backend-frontend separation
   - Unit testing
   - Configuration management

---

## 🔍 Example Output

### Console Output (from demo.py)
```
FRAGMENTATION ANALYSIS REPORT
═════════════════════════════════════════════════════════
Total Memory Size:              1000 KB
Allocated Space:                580 KB
Free Space:                     420 KB

Memory Utilization:             58.0%
External Fragmentation:         0.0%
Internal Fragmentation:         0.0%

Largest Contiguous Free Block:  420 KB
Number of Allocated Blocks:     5
Number of Free Blocks:          1
═════════════════════════════════════════════════════════
```

### Statistics Display
```
MEMORY STATISTICS
─────────────────────────
Total Memory:      1000 KB
Allocated:           300 KB
Free:                700 KB

FRAGMENTATION
─────────────────────────
Memory Util:        30.0%
External Frag:       0.0%
Largest Free Blk:   700 KB

BLOCKS
─────────────────────────
Allocated Blocks:      3
Free Blocks:           1
```

---

## 🐛 Known Limitations

1. **Single Memory System**: Only one 1000 KB memory space
2. **No Process Files**: Processes are simplified (no actual code)
3. **2D Visualization**: Linear memory representation only
4. **No Preemption**: Processes don't move after allocation
5. **No Time Simulation**: Instant allocation/deallocation

These are intentional for educational clarity.

---

## 🚀 Future Enhancements

Possible improvements:
- [ ] Multiple memory partitions
- [ ] Process priority levels
- [ ] Memory paging simulation
- [ ] Virtual memory support
- [ ] Statistics graphs/charts
- [ ] Process timing simulation
- [ ] Custom memory policies
- [ ] Export analysis reports (PDF/CSV)
- [ ] Undo/Redo functionality
- [ ] Animation of allocations

---

## 📚 References & Related Topics

### Operating Systems Concepts
- Contiguous Memory Allocation
- Memory Management Unit (MMU)
- Virtual Memory
- Paging and Segmentation
- Memory Fragmentation

### Algorithms
- First Fit Algorithm
- Best Fit Algorithm  
- Worst Fit Algorithm
- Next Fit Algorithm

### Performance Analysis
- Fragmentation measurement
- Memory utilization tracking
- Algorithm efficiency comparison

---

## 📝 Notes for Instructors

This simulator is ideal for:
- **Lectures**: Demonstrate concepts visually
- **Labs**: Hands-on algorithm practice
- **Projects**: Extend with new features
- **Exams**: Conceptual understanding questions

**Suggested Activities:**
1. Allocate/deallocate patterns and observe fragmentation
2. Compare strategies with same workload
3. Calculate fragmentation manually and verify
4. Modify and test new strategies
5. Generate reports and analyze results

---

## 🎉 Conclusion

This Memory Allocation Simulator provides a comprehensive, interactive platform for understanding operating systems memory management. With its intuitive GUI, multiple allocation strategies, and detailed fragmentation analysis, it serves as an excellent educational tool for operating systems courses.

---

**Version**: 1.0  
**Date**: February 2026  
**Status**: ✅ Fully Functional  
**Tests**: ✅ All Passing (8/8)  
**Documentation**: ✅ Complete

---

For questions or suggestions, refer to [README.md](README.md) or [USERGUIDE.md](USERGUIDE.md)
