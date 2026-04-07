"""
Memory Allocation Simulator - Main Entry Point
This application simulates memory allocation using First Fit, Best Fit, and Worst Fit strategies
"""

import tkinter as tk
from ui.gui import MemoryAllocationSimulator

def main():
    root = tk.Tk()
    app = MemoryAllocationSimulator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
