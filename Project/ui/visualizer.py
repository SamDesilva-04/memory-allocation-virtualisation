"""
Memory visualization module for tkinter GUI
"""

import tkinter as tk
from tkinter import Canvas
import math

class MemoryVisualizer:
    """Handles visual representation of memory blocks"""
    
    def __init__(self, canvas, memory_obj):
        self.canvas = canvas
        self.memory = memory_obj
        self.block_height = 40
        self.colors = {
            'allocated': '#FF6B6B',
            'free': '#95E1D3',
            'border': '#2C3E50',
            'text': '#FFFFFF'
        }
        self.process_colors = {}
        self.color_palette = [
            '#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8',
            '#F7DC6F', '#BB8FCE', '#85C1E2', '#F8B88B', '#A9E5BB'
        ]
        self.color_index = 0

    def draw_memory(self):
        """Draw memory blocks on canvas"""
        self.canvas.delete("all")
        
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        if canvas_width <= 1:
            canvas_width = 800
        if canvas_height <= 1:
            canvas_height = 300
        
        blocks = self.memory.get_memory_state()
        
        if not blocks:
            return
        
        # Calculate scale
        total_memory = self.memory.total_size
        pixels_per_kb = (canvas_width - 40) / total_memory
        
        # Draw blocks
        y_start = 50
        
        for block in blocks:
            x_start = 20 + (block.start * pixels_per_kb)
            block_width = max(3, block.size * pixels_per_kb)
            
            # Choose color
            if block.allocated:
                if block.process_id not in self.process_colors:
                    self.process_colors[block.process_id] = self.color_palette[
                        self.color_index % len(self.color_palette)
                    ]
                    self.color_index += 1
                color = self.process_colors[block.process_id]
            else:
                color = self.colors['free']
            
            # Draw rectangle
            self.canvas.create_rectangle(
                x_start, y_start,
                x_start + block_width, y_start + self.block_height,
                fill=color,
                outline=self.colors['border'],
                width=2,
                tags=f"block_{block.block_id}"
            )
            
            # Draw label
            if block_width > 30:
                if block.allocated:
                    label = f"{block.process_id}\n{block.size}KB"
                else:
                    label = f"Free\n{block.size}KB"
                
                self.canvas.create_text(
                    x_start + block_width / 2,
                    y_start + self.block_height / 2,
                    text=label,
                    fill=self.colors['text'],
                    font=("Arial", 9, "bold"),
                    tags=f"label_{block.block_id}"
                )
        
        # Draw addresses at bottom
        self.draw_address_scale(canvas_width, y_start + self.block_height + 30, pixels_per_kb)
        
        # Draw legend
        self.draw_legend(canvas_width, canvas_height)

    def draw_address_scale(self, canvas_width, y_position, pixels_per_kb):
        """Draw memory address scale"""
        step = self._calculate_step(self.memory.total_size)
        
        for address in range(0, self.memory.total_size + 1, step):
            x = 20 + (address * pixels_per_kb)
            if x <= canvas_width - 20:
                self.canvas.create_line(x, y_position, x, y_position + 5)
                self.canvas.create_text(
                    x, y_position + 15,
                    text=str(address),
                    font=("Arial", 8),
                    angle=45
                )

    def draw_legend(self, canvas_width, canvas_height):
        """Draw legend for allocated and free blocks"""
        legend_y = canvas_height - 40
        
        # Allocated block example
        self.canvas.create_rectangle(
            20, legend_y, 50, legend_y + 20,
            fill=self.colors['allocated'],
            outline=self.colors['border']
        )
        self.canvas.create_text(
            60, legend_y + 10,
            text="Allocated",
            font=("Arial", 9),
            anchor="w"
        )
        
        # Free block example
        self.canvas.create_rectangle(
            150, legend_y, 180, legend_y + 20,
            fill=self.colors['free'],
            outline=self.colors['border']
        )
        self.canvas.create_text(
            190, legend_y + 10,
            text="Free",
            font=("Arial", 9),
            anchor="w"
        )

    def _calculate_step(self, total_size):
        """Calculate appropriate step for address scale"""
        if total_size <= 100:
            return 10
        elif total_size <= 500:
            return 50
        else:
            return max(100, total_size // 10)

    def clear(self):
        """Clear canvas"""
        self.canvas.delete("all")
        self.process_colors.clear()
        self.color_index = 0


class StatisticsDisplay:
    """Display memory statistics"""
    
    @staticmethod
    def format_statistics(analysis):
        """Format statistics for display"""
        stats = f"""
MEMORY STATISTICS
─────────────────────────
Total Memory:      {analysis['total_memory']:>6} KB
Allocated:         {analysis['allocated_space']:>6} KB
Free:              {analysis['free_space']:>6} KB

FRAGMENTATION
─────────────────────────
Memory Util:       {analysis['memory_utilization']:>5.1f}%
External Frag:     {analysis['external_fragmentation']:>5.1f}%
Largest Free Blk:  {analysis['largest_free_block']:>6} KB

BLOCKS
─────────────────────────
Allocated Blocks:  {analysis['number_of_allocated_blocks']:>6}
Free Blocks:       {analysis['number_of_free_blocks']:>6}
        """
        return stats
