"""
Configuration settings for Memory Allocation Simulator
"""

# Memory Configuration
TOTAL_MEMORY_SIZE = 1000  # Total memory in KB

# UI Configuration
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
WINDOW_TITLE = "Memory Allocation Simulator"

# Visualization Configuration
BLOCK_HEIGHT = 40
CANVAS_BG_COLOR = 'white'

# Color Scheme
COLORS = {
    'allocated': '#FF6B6B',      # Red for allocated blocks
    'free': '#95E1D3',            # Cyan for free blocks
    'border': '#2C3E50',          # Dark for borders
    'text': '#FFFFFF'             # White for text
}

# Process color palette for different processes
PROCESS_COLOR_PALETTE = [
    '#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8',
    '#F7DC6F', '#BB8FCE', '#85C1E2', '#F8B88B', '#A9E5BB',
    '#FF6B9D', '#C44569', '#4ECDC4', '#44A08D', '#34495E'
]

# Font Configuration
FONT_TITLE = ("Arial", 16, "bold")
FONT_HEADER = ("Arial", 14, "bold")
FONT_SUBHEADER = ("Arial", 11, "bold")
FONT_NORMAL = ("Arial", 10)
FONT_MONO = ("Consolas", 9)

# Allocation Strategies
STRATEGIES = {
    'first_fit': 'First Fit',
    'best_fit': 'Best Fit',
    'worst_fit': 'Worst Fit'
}

# Simulation Parameters
MIN_PROCESS_SIZE = 10
MAX_PROCESS_SIZE = 300
RANDOM_ALLOCATION_MIN = 50
RANDOM_ALLOCATION_MAX = 300

# Demo Configuration
DEMO_PROCESSES = [100, 150, 200, 50, 80]
