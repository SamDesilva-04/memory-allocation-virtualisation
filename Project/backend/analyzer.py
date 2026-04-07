"""
Memory fragmentation analyzer
Calculates internal and external fragmentation metrics
"""

class FragmentationAnalyzer:
    """Analyzes memory fragmentation"""
    
    @staticmethod
    def calculate_external_fragmentation(memory):
        """
        Calculate external fragmentation percentage
        External fragmentation = (Total Free Space - Largest Contiguous Free Block) / Total Free Space * 100
        """
        free_blocks = memory.get_free_blocks()
        
        if not free_blocks:
            return 0.0
        
        total_free = sum(block.size for block in free_blocks)
        largest_free = max(block.size for block in free_blocks)
        
        if total_free == 0:
            return 0.0
        
        fragmentation = ((total_free - largest_free) / total_free) * 100
        return round(fragmentation, 2)

    @staticmethod
    def calculate_internal_fragmentation(memory):
        """
        Calculate internal fragmentation percentage
        Internal fragmentation = Total Wasted Space in Allocated Blocks / Total Memory * 100
        This is typically 0 for simple allocation strategies
        """
        # In basic allocation, there's typically no internal fragmentation
        # since we allocate exact sizes
        return 0.0

    @staticmethod
    def calculate_memory_utilization(memory):
        """Calculate memory utilization percentage"""
        total_allocated = sum(block.size for block in memory.get_allocated_processes())
        utilization = (total_allocated / memory.total_size) * 100
        return round(utilization, 2)

    @staticmethod
    def get_free_space(memory):
        """Get total free space"""
        free_blocks = memory.get_free_blocks()
        return sum(block.size for block in free_blocks)

    @staticmethod
    def get_allocated_space(memory):
        """Get total allocated space"""
        allocated_blocks = memory.get_allocated_processes()
        return sum(block.size for block in allocated_blocks)

    @staticmethod
    def get_largest_free_block(memory):
        """Get size of largest contiguous free block"""
        free_blocks = memory.get_free_blocks()
        if not free_blocks:
            return 0
        return max(block.size for block in free_blocks)

    @staticmethod
    def analyze_fragmentation(memory):
        """Get comprehensive fragmentation analysis"""
        return {
            'external_fragmentation': FragmentationAnalyzer.calculate_external_fragmentation(memory),
            'internal_fragmentation': FragmentationAnalyzer.calculate_internal_fragmentation(memory),
            'memory_utilization': FragmentationAnalyzer.calculate_memory_utilization(memory),
            'total_memory': memory.total_size,
            'allocated_space': FragmentationAnalyzer.get_allocated_space(memory),
            'free_space': FragmentationAnalyzer.get_free_space(memory),
            'largest_free_block': FragmentationAnalyzer.get_largest_free_block(memory),
            'number_of_allocated_blocks': len(memory.get_allocated_processes()),
            'number_of_free_blocks': len(memory.get_free_blocks()),
        }

    @staticmethod
    def get_fragmentation_report(memory):
        """Generate a formatted fragmentation report"""
        analysis = FragmentationAnalyzer.analyze_fragmentation(memory)
        
        report = f"""
═══════════════════════════════════════════════════════════════
                   FRAGMENTATION ANALYSIS REPORT
═══════════════════════════════════════════════════════════════

Total Memory Size:              {analysis['total_memory']} KB
Allocated Space:                {analysis['allocated_space']} KB
Free Space:                     {analysis['free_space']} KB

Memory Utilization:             {analysis['memory_utilization']}%
External Fragmentation:         {analysis['external_fragmentation']}%
Internal Fragmentation:         {analysis['internal_fragmentation']}%

Largest Contiguous Free Block:  {analysis['largest_free_block']} KB
Number of Allocated Blocks:     {analysis['number_of_allocated_blocks']}
Number of Free Blocks:          {analysis['number_of_free_blocks']}

═══════════════════════════════════════════════════════════════
"""
        return report
