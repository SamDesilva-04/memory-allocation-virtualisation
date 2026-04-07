# Memory Allocation Simulator - User Guide

## Quick Start

### Running the Application

```bash
# Navigate to project directory
cd S:\Edu\BTIT\OS\Project

# Run the GUI application
python main.py
```

The application window will open with a professional interface for simulating memory allocation.

---

## User Interface Overview

### 1. **Strategy Selection Panel** (Top Left)
Choose your memory allocation strategy:
- **First Fit**: Allocates in the first block that has enough space
- **Best Fit**: Allocates in the smallest block that fits
- **Worst Fit**: Allocates in the largest available block

### 2. **Process Management Panel** (Top Center)
- **Process Size Input**: Enter the size of process to allocate (in KB)
- **Allocate Button**: Allocate memory with current strategy
- **Random Allocate Button**: Allocate a random-sized process (50-300 KB)
- **Reset Memory Button**: Clear all allocations and start fresh

### 3. **Memory Layout Visualization** (Left Panel)
Visual representation of memory blocks:
- **Colored blocks**: Each allocated process has a unique color
- **Cyan/Turquoise blocks**: Free memory spaces
- **Block labels**: Show process ID and size
- **Address scale**: Memory addresses at bottom for reference

### 4. **Memory Statistics** (Lower Left)
Real-time statistics display:
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

### 5. **Allocated Processes Table** (Right Panel)
Displays all currently allocated processes with:
- **Process ID**: P1, P2, P3, etc.
- **Size (KB)**: Size of the allocated process
- **Start Address**: Memory address where process starts
- **End Address**: Memory address where process ends

### 6. **Analysis Report** (Lower Right)
Click "Generate Report" to see detailed fragmentation analysis including:
- Total memory configuration
- Allocated vs free space
- Utilization percentage
- Fragmentation metrics
- Block statistics

---

## Step-by-Step Tutorial

### Tutorial 1: Basic Memory Allocation

1. **Set Initial Parameters**
   - Strategy selection: Select "First Fit"
   - Process size: Enter "150" in the size field

2. **Allocate First Process**
   - Click **"Allocate"** button
   - Observe: 
     - A red block appears in visualization
     - P1 appears in the Allocated Processes table
     - Statistics update showing 150 KB used

3. **Allocate More Processes**
   - Change size to "200", click Allocate
   - Change size to "100", click Allocate
   - Change size to "300", click Allocate
   - Watch the visualization fill with different colored blocks

### Tutorial 2: Testing Fragmentation

1. **Create Fragmentation**
   - Allocate: 100 KB (P1)
   - Allocate: 100 KB (P2)
   - Allocate: 100 KB (P3)
   - Allocate: 100 KB (P4)

2. **Deallocate Middle Processes**
   - Select P2 from table, click Deallocate
   - This creates a 100 KB free gap
   - Select P3 from table, click Deallocate
   - This creates another 100 KB gap

3. **Observe Fragmentation**
   - Check statistics: External fragmentation should be > 0%
   - Note: You now have 200 KB free but in two separate 100 KB blocks
   - The largest contiguous block is 100 KB

4. **Allocate a Process**
   - Try to allocate 150 KB
   - Result: Will fail because no single block has 150 KB
   - This demonstrates external fragmentation

### Tutorial 3: Compare Allocation Strategies

1. **Reset Memory**
   - Click Reset Memory button

2. **Use First Fit**
   - Select "First Fit" strategy
   - Allocate: 100, 150, 50, 100, 100 KB
   - Generate Report (save results)

3. **Reset Again**
   - Click Reset Memory

4. **Use Best Fit**
   - Select "Best Fit" strategy
   - Allocate same sizes: 100, 150, 50, 100, 100 KB
   - Generate Report and compare

5. **Reset and Test Worst Fit**
   - Click Reset Memory
   - Select "Worst Fit" strategy
   - Allocate same sizes again
   - Generate Report
   - Compare fragmentation between all three strategies

---

## Understanding Fragmentation

### External Fragmentation
- **What it is**: Free memory scattered in small blocks that can't be used
- **Formula**: `(Total Free - Largest Free Block) / Total Free × 100%`
- **Example**: 
  - Total free: 200 KB
  - Largest block: 80 KB
  - External fragmentation: (200-80)/200 × 100 = 60%

### Memory Utilization
- **What it is**: Percentage of memory actually in use
- **Formula**: `Used Memory / Total Memory × 100%`
- **Example**:
  - Used: 300 KB
  - Total: 1000 KB  
  - Utilization: 300/1000 × 100 = 30%

### Number of Free Blocks
- **What it is**: How many separate free memory regions exist
- **Why it matters**: More blocks = more fragmentation

---

## Allocation Strategy Comparison

| Feature | First Fit | Best Fit | Worst Fit |
|---------|-----------|----------|-----------|
| **Speed** | Fast ⚡ | Slower | Medium |
| **Wasted Space** | Medium | Low | Low |
| **Fragmentation** | Can be high | Can be low | Attempts low |
| **Use Case** | Quick simple systems | Minimize waste | Balance approach |
| **Complexity** | Simple | Moderate | Moderate |

---

## Common Scenarios

### Scenario 1: Allocate Until Full
```
1. Reset memory
2. Keep clicking "Random Allocate" 
3. Eventually get "No sufficient memory" error
4. Check statistics
5. View the fragmented memory layout
```

### Scenario 2: Fragment the Memory
```
1. Allocate: 100 KB, 100 KB, 100 KB, 100 KB, 100 KB, 100 KB
2. Deallocate: P2, P4, P6 (every other process)
3. Try to allocate 200 KB
4. Will fail due to external fragmentation
5. Generate report to see fragmentation metrics
```

### Scenario 3: Compare Strategies with Same Workload
```
For each strategy (First/Best/Worst):
1. Reset Memory
2. Use strategy
3. Allocate: 100, 150, 200, 75, 125 KB
4. Deallocate: P2, P4
5. Generate Report
6. Note differences in stats
```

---

## Tips and Tricks

### For Better Understanding
1. **Slow down with pauses**: Allocate one at a time and observe changes
2. **Use Random Allocate**: Helps see how strategies handle varied sizes
3. **Generate Reports often**: Helps track metrics changes
4. **Compare side-by-side**: Reset and use different strategies with same sequence

### Memory Management Best Practices
1. **Watch fragmentation**: High external fragmentation indicates memory issues
2. **Monitor utilization**: Low utilization with high fragmentation is problematic
3. **Balance allocation**: Mix different process sizes to understand tradeoffs
4. **Study patterns**: Notice how each strategy creates different block patterns

---

## Demo Script

Run the command-line demo to see programmatic usage:

```bash
python demo.py
```

This shows:
- Automated allocation sequences
- Console output of allocation results
- Fragmentation reports for each strategy
- Comparison examples

---

## Troubleshooting

### Issue: "No sufficient memory" error
**Cause**: Memory is full or no single block is large enough
**Solution**: 
- Click Reset Memory to start fresh
- Try allocating smaller processes
- Deallocate some processes first

### Issue: Visualization not updating
**Cause**: Canvas may not have rendered properly
**Solution**:
- Resize the window
- Click Reset Memory
- Restart application

### Issue: Application won't start
**Cause**: tkinter not available or Python version too old
**Solution**:
```bash
# Check Python version (need 3.6+)
python --version

# Check tkinter
python -m tkinter

# If fails, install tkinter (Windows)
pip install tk
```

### Issue: Numbers don't look right
**Cause**: Integer division or rounding
**Solution**: Check if values make sense (they should be whole KBs)

---

## Performance Notes

- **Memory size**: 1000 KB (total)
- **Min process**: 1 KB
- **Max process**: 999 KB (almost all memory)
- **Merge time**: Instant (automatic)
- **Visualization**: Updates in real-time

---

## Advanced Usage

### Modifying Total Memory
Edit [main.py](main.py):
```python
# Line in MemoryAllocationSimulator.__init__
self.memory = Memory(total_memory_size=2000)  # Change 2000 to desired size
```

### Adding Custom Allocation Strategy
1. Add method to `Memory` class in [backend/memory.py](backend/memory.py)
2. Update `_find_suitable_block()` method
3. Add radio button in [ui/gui.py](ui/gui.py)

### Changing Colors
Edit [ui/visualizer.py](ui/visualizer.py) in `MemoryVisualizer` class:
```python
self.colors = {
    'allocated': '#FF6B6B',  # Change hex color
    'free': '#95E1D3',
    ...
}
```

---

## Testing

Run unit tests to verify functionality:

```bash
python tests.py
```

This runs 8 comprehensive tests to validate:
- All allocation strategies
- Memory deallocation
- Block merging
- Fragmentation calculations
- Statistics accuracy

---

## Learning Resources

### Concepts Covered
- Contiguous Memory Allocation
- Memory Fragmentation (Internal & External)
- Dynamic Memory Management
- Process Management
- Resource Allocation Algorithms

### Related Topics to Study
- Virtual Memory and Paging
- Memory Segmentation
- Dynamic Partitioning
- Non-contiguous Allocation
- Cache Memory Management

---

## File Structure Reference

```
project/
├── main.py              ← Run this to start
├── demo.py              ← Run for console demo
├── tests.py             ← Run for unit tests
├── config.py            ← Configuration settings
├── requirements.txt     ← Dependencies
├── README.md            ← Full documentation
├── USERGUIDE.md         ← This file
│
├── backend/
│   ├── memory.py        ← Core allocation logic
│   └── analyzer.py      ← Fragmentation analysis
│
└── ui/
    ├── gui.py           ← Main GUI
    └── visualizer.py    ← Visualization logic
```

---

## Support and Further Help

- Check [README.md](README.md) for technical details
- Run demo.py for examples
- Run tests.py to verify system
- Review inline code comments
- Modify config.py for customization

---

**Happy Learning!** 🎓

*Memory Allocation Simulator v1.0*
*Operating Systems Course Project*
