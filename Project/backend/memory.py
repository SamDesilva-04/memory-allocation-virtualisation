"""
Memory class representing the memory management system
"""

class MemoryBlock:
    """Represents a block in memory"""
    def __init__(self, block_id, start, size, allocated=False, process_id=None):
        self.block_id = block_id
        self.start = start
        self.size = size
        self.allocated = allocated
        self.process_id = process_id

    def __repr__(self):
        status = "Allocated" if self.allocated else "Free"
        return f"Block({self.block_id}, Start:{self.start}, Size:{self.size}, {status})"


class Memory:
    """Manages memory allocation and deallocation"""
    
    def __init__(self, total_memory_size=1000):
        self.total_size = total_memory_size
        self.blocks = [MemoryBlock(0, 0, total_memory_size, allocated=False)]
        self.process_counter = 0
        self.allocation_history = []

    def allocate(self, process_size, strategy='first_fit'):
        """
        Allocate memory using the specified strategy
        Returns: (success, allocated_block, message)
        """
        if process_size <= 0:
            return False, None, "Process size must be positive"

        suitable_block = self._find_suitable_block(process_size, strategy)

        if suitable_block is None:
            return False, None, f"No sufficient contiguous memory available for size {process_size}"

        return self._allocate_block(suitable_block, process_size)

    def _find_suitable_block(self, process_size, strategy):
        """Find a suitable free block based on the strategy"""
        free_blocks = [b for b in self.blocks if not b.allocated and b.size >= process_size]

        if not free_blocks:
            return None

        if strategy == 'first_fit':
            return free_blocks[0]
        elif strategy == 'best_fit':
            return min(free_blocks, key=lambda x: x.size)
        elif strategy == 'worst_fit':
            return max(free_blocks, key=lambda x: x.size)
        else:
            return free_blocks[0]

    def _allocate_block(self, block, process_size):
        """Allocate memory in the given block"""
        self.process_counter += 1
        process_id = f"P{self.process_counter}"

        # Remove the original block
        self.blocks.remove(block)

        # Create allocated block
        allocated_block = MemoryBlock(
            len([b for b in self.blocks if b.allocated]),
            block.start,
            process_size,
            allocated=True,
            process_id=process_id
        )
        self.blocks.append(allocated_block)

        # If there's remaining space, create a free block
        if block.size > process_size:
            remaining_block = MemoryBlock(
                len([b for b in self.blocks if not b.allocated]),
                block.start + process_size,
                block.size - process_size,
                allocated=False
            )
            self.blocks.append(remaining_block)

        # Sort blocks by starting address
        self.blocks.sort(key=lambda x: x.start)

        self.allocation_history.append({
            'process_id': process_id,
            'size': process_size,
            'start': allocated_block.start,
            'action': 'allocate'
        })

        return True, allocated_block, f"Process {process_id} allocated successfully"

    def deallocate(self, process_id):
        """Deallocate memory for a process"""
        block_to_free = None
        block_index = None

        for idx, block in enumerate(self.blocks):
            if block.allocated and block.process_id == process_id:
                block_to_free = block
                block_index = idx
                break

        if block_to_free is None:
            return False, f"Process {process_id} not found"

        self.blocks[block_index] = MemoryBlock(
            block_to_free.block_id,
            block_to_free.start,
            block_to_free.size,
            allocated=False,
            process_id=None
        )

        self._merge_adjacent_free_blocks()

        self.allocation_history.append({
            'process_id': process_id,
            'size': block_to_free.size,
            'start': block_to_free.start,
            'action': 'deallocate'
        })

        return True, f"Process {process_id} deallocated successfully"

    def _merge_adjacent_free_blocks(self):
        """Merge adjacent free blocks to reduce fragmentation"""
        merged = True
        while merged:
            merged = False
            for i in range(len(self.blocks) - 1):
                current = self.blocks[i]
                next_block = self.blocks[i + 1]

                if (not current.allocated and not next_block.allocated and
                    current.start + current.size == next_block.start):
                    
                    merged_block = MemoryBlock(
                        current.block_id,
                        current.start,
                        current.size + next_block.size,
                        allocated=False
                    )
                    self.blocks[i] = merged_block
                    self.blocks.pop(i + 1)
                    merged = True
                    break

    def reset(self):
        """Reset memory to initial state"""
        self.__init__(self.total_size)

    def get_memory_state(self):
        """Get current memory state"""
        return self.blocks.copy()

    def get_allocated_processes(self):
        """Get list of allocated processes"""
        return [b for b in self.blocks if b.allocated]

    def get_free_blocks(self):
        """Get list of free blocks"""
        return [b for b in self.blocks if not b.allocated]
