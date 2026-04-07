"""
Main GUI for Memory Allocation Simulator using tkinter
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from backend.memory import Memory
from backend.analyzer import FragmentationAnalyzer
from ui.visualizer import MemoryVisualizer, StatisticsDisplay
import random


class MemoryAllocationSimulator:
    """Main GUI Application for Memory Allocation Simulator"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Allocation Simulator")
        self.root.geometry("1200x800")
        self.root.configure(bg='#F0F0F0')
        
        # Initialize memory with 1000 KB
        self.memory = Memory(total_memory_size=1000)
        self.current_strategy = tk.StringVar(value='first_fit')
        
        self.setup_styles()
        self.create_widgets()
        self.visualizer = MemoryVisualizer(self.canvas, self.memory)
        
        # Bind canvas resize
        self.canvas.bind("<Configure>", lambda e: self.update_visualization())
        
        # Initial draw
        self.root.after(100, self.update_visualization)
    
    def setup_styles(self):
        """Setup tkinter styles"""
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        self.style.configure('Header.TLabel', font=('Arial', 14, 'bold'))
        self.style.configure('Title.TLabel', font=('Arial', 16, 'bold'))
        self.style.configure('Subheader.TLabel', font=('Arial', 11, 'bold'))
        
        self.button_font = ('Arial', 10, 'bold')
        self.text_font = ('Consolas', 9)

    def create_widgets(self):
        """Create all GUI widgets"""
        # Main container
        main_container = ttk.Frame(self.root)
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title = ttk.Label(main_container, text="Memory Allocation Simulator", style='Title.TLabel')
        title.pack(pady=10)
        
        # Top section: Controls and Strategy
        top_frame = ttk.Frame(main_container)
        top_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Strategy selection
        strategy_frame = ttk.LabelFrame(top_frame, text="Allocation Strategy", padding=10)
        strategy_frame.pack(side=tk.LEFT, fill=tk.X, padx=5)
        
        strategies = [
            ('First Fit', 'first_fit'),
            ('Best Fit', 'best_fit'),
            ('Worst Fit', 'worst_fit')
        ]
        
        for text, value in strategies:
            ttk.Radiobutton(
                strategy_frame,
                text=text,
                variable=self.current_strategy,
                value=value
            ).pack(anchor=tk.W)
        
        # Process allocation controls
        control_frame = ttk.LabelFrame(top_frame, text="Process Management", padding=10)
        control_frame.pack(side=tk.LEFT, fill=tk.X, padx=5, expand=True)
        
        ttk.Label(control_frame, text="Process Size (KB):").pack(side=tk.LEFT, padx=5)
        self.size_entry = ttk.Entry(control_frame, width=10)
        self.size_entry.pack(side=tk.LEFT, padx=5)
        self.size_entry.insert(0, "100")
        
        ttk.Button(
            control_frame,
            text="Allocate",
            command=self.allocate_memory
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            control_frame,
            text="Random Allocate",
            command=self.random_allocate
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            control_frame,
            text="Reset Memory",
            command=self.reset_memory
        ).pack(side=tk.LEFT, padx=5)
        
        # Main content area
        content_frame = ttk.Frame(main_container)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Left section: Visualization and info
        left_frame = ttk.Frame(content_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        # Canvas for memory visualization
        viz_frame = ttk.LabelFrame(left_frame, text="Memory Layout", padding=5)
        viz_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.canvas = tk.Canvas(
            viz_frame,
            bg='white',
            height=300,
            relief=tk.SUNKEN,
            borderwidth=2
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Statistics frame
        stats_frame = ttk.LabelFrame(left_frame, text="Memory Statistics", padding=10)
        stats_frame.pack(fill=tk.X, pady=5)
        
        self.stats_text = tk.Text(stats_frame, height=10, width=50, font=self.text_font)
        self.stats_text.pack(fill=tk.BOTH, expand=True)
        self.stats_text.config(state=tk.DISABLED)
        
        # Right section: Process list and actions
        right_frame = ttk.Frame(content_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=5)
        
        # Process list
        process_frame = ttk.LabelFrame(right_frame, text="Allocated Processes", padding=10)
        process_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Create treeview for processes
        columns = ('Process', 'Size', 'Start', 'End')
        self.process_tree = ttk.Treeview(process_frame, columns=columns, height=10)
        self.process_tree.column('#0', width=0, stretch=tk.NO)
        self.process_tree.column('Process', anchor=tk.W, width=80)
        self.process_tree.column('Size', anchor=tk.CENTER, width=60)
        self.process_tree.column('Start', anchor=tk.CENTER, width=60)
        self.process_tree.column('End', anchor=tk.CENTER, width=60)
        
        self.process_tree.heading('#0', text='', anchor=tk.W)
        self.process_tree.heading('Process', text='Process', anchor=tk.W)
        self.process_tree.heading('Size', text='Size (KB)', anchor=tk.CENTER)
        self.process_tree.heading('Start', text='Start', anchor=tk.CENTER)
        self.process_tree.heading('End', text='End', anchor=tk.CENTER)
        
        scrollbar = ttk.Scrollbar(process_frame, orient=tk.VERTICAL, command=self.process_tree.yview)
        self.process_tree.configure(yscroll=scrollbar.set)
        
        self.process_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Deallocate button
        dealloc_frame = ttk.Frame(right_frame)
        dealloc_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(dealloc_frame, text="Selected Process:").pack(side=tk.LEFT)
        self.selected_process = tk.StringVar()
        
        ttk.Button(
            dealloc_frame,
            text="Deallocate",
            command=self.deallocate_process
        ).pack(side=tk.LEFT, padx=5)
        
        # History and Report
        report_frame = ttk.LabelFrame(right_frame, text="Analysis Report", padding=10)
        report_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        ttk.Button(
            report_frame,
            text="Generate Report",
            command=self.generate_report
        ).pack(fill=tk.X, pady=5)
        
        self.report_text = scrolledtext.ScrolledText(report_frame, height=8, width=30, font=self.text_font)
        self.report_text.pack(fill=tk.BOTH, expand=True)
        self.report_text.config(state=tk.DISABLED)
    
    def allocate_memory(self):
        """Handle memory allocation"""
        try:
            size = int(self.size_entry.get())
            if size <= 0:
                messagebox.showerror("Error", "Process size must be positive")
                return
            
            strategy = self.current_strategy.get()
            success, block, message = self.memory.allocate(size, strategy)
            
            if success:
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Allocation Failed", message)
            
            self.update_visualization()
        
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")
    
    def random_allocate(self):
        """Allocate random process sizes"""
        size = random.randint(50, 300)
        self.size_entry.delete(0, tk.END)
        self.size_entry.insert(0, str(size))
        self.allocate_memory()
    
    def deallocate_process(self):
        """Deallocate selected process"""
        selection = self.process_tree.selection()
        
        if not selection:
            messagebox.showwarning("Warning", "Please select a process to deallocate")
            return
        
        item = selection[0]
        values = self.process_tree.item(item, 'values')
        process_id = values[0]
        
        success, message = self.memory.deallocate(process_id)
        
        if success:
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)
        
        self.update_visualization()
    
    def reset_memory(self):
        """Reset memory to initial state"""
        if messagebox.askyesno("Confirm", "Reset all memory allocations?"):
            self.memory.reset()
            self.visualizer.clear()
            self.update_visualization()
    
    def update_visualization(self):
        """Update memory visualization and statistics"""
        self.visualizer.draw_memory()
        self.update_statistics()
        self.update_process_list()
    
    def update_statistics(self):
        """Update statistics display"""
        analysis = FragmentationAnalyzer.analyze_fragmentation(self.memory)
        stats = StatisticsDisplay.format_statistics(analysis)
        
        self.stats_text.config(state=tk.NORMAL)
        self.stats_text.delete('1.0', tk.END)
        self.stats_text.insert('1.0', stats)
        self.stats_text.config(state=tk.DISABLED)
    
    def update_process_list(self):
        """Update process list treeview"""
        # Clear existing items
        for item in self.process_tree.get_children():
            self.process_tree.delete(item)
        
        # Add allocated processes
        allocated = self.memory.get_allocated_processes()
        for block in allocated:
            end_address = block.start + block.size
            self.process_tree.insert('', 'end', values=(
                block.process_id,
                block.size,
                block.start,
                end_address
            ))
    
    def generate_report(self):
        """Generate fragmentation analysis report"""
        report = FragmentationAnalyzer.get_fragmentation_report(self.memory)
        
        self.report_text.config(state=tk.NORMAL)
        self.report_text.delete('1.0', tk.END)
        self.report_text.insert('1.0', report)
        self.report_text.config(state=tk.DISABLED)
        
        # Also show in message box
        messagebox.showinfo("Fragmentation Report", report)
