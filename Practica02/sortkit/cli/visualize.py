"""
MIT License

Copyright (c) 2023 David Rivera Morales

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
"""

import argparse
import random
import time
from typing import List, Callable, Dict, Any

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

from sortkit.algorithms.registry import get_algorithm, list_algorithms
from sortkit.structs.dllist import DoublyLinkedList, get_linked_list_algorithm
from sortkit.structs.adapter import register_all_for_linked_list


class SortingVisualizer:
    """Class for visualizing sorting algorithms."""
    
    def __init__(
        self, 
        algorithm_name: str, 
        data: List[int], 
        data_type: str = "list",
        interval: int = 50,
        save_animation: bool = False,
        output_file: str = "sorting_animation.mp4"
    ):
        self.algorithm_name = algorithm_name
        self.original_data = data
        self.data_type = data_type
        self.interval = interval
        self.save_animation = save_animation
        self.output_file = output_file
        
        # Setup the figure and axis
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.bar_container = None
        
        # Initialize data and algorithm
        self._setup_algorithm()
        
        # History of states for animation
        self.history = []
        self.trace_data = {}
        
    def _setup_algorithm(self):
        """Setup the algorithm and data structure."""
        # Create a fresh copy of the data
        if self.data_type == "list":
            self.data = self.original_data.copy()
            self.algorithm = get_algorithm(self.algorithm_name)
        else:  # dllist
            self.data = DoublyLinkedList(self.original_data)
            self.algorithm = get_linked_list_algorithm(self.algorithm_name)
            
        # Track algorithm's original __call__ method
        self.original_call = self.algorithm.__call__
        
        # Reset trace counters
        self.algorithm.reset_trace()
    
    def _capture_state(self, data):
        """Capture the current state of the data."""
        if self.data_type == "list":
            # For list, we can just make a copy
            self.history.append(data.copy())
        else:
            # For DoublyLinkedList, we need to convert to a list
            self.history.append(list(data))
        
        # Also capture trace data
        self.trace_data = self.algorithm.get_trace()
    
    def _wrap_algorithm(self):
        """Wrap the algorithm to capture states during sorting."""
        def wrapped_call(data):
            # Reset history
            self.history = [data.copy() if self.data_type == "list" else list(data)]
            
            # Monkey patch the traceable functions to capture state
            original_compare = self.algorithm._compare
            original_swap = self.algorithm._swap
            
            def wrapped_compare(x, y):
                result = original_compare(x, y)
                self._capture_state(data)
                return result
            
            def wrapped_swap(data, i, j):
                result = original_swap(data, i, j)
                self._capture_state(data)
                return result
            
            self.algorithm._compare = wrapped_compare
            self.algorithm._swap = wrapped_swap
            
            # Call the original algorithm
            result = self.original_call(data)
            
            # Restore the original functions
            self.algorithm._compare = original_compare
            self.algorithm._swap = original_swap
            
            return result
        
        # Replace the call method
        self.algorithm.__call__ = wrapped_call
    
    def _init_animation(self):
        """Initialize the animation."""
        self.ax.set_title(f"Sorting Visualization: {self.algorithm_name}")
        self.ax.set_xlabel("Index")
        self.ax.set_ylabel("Value")
        
        # Initial bar plot
        x = np.arange(len(self.history[0]))
        self.bar_container = self.ax.bar(x, self.history[0], color='skyblue')
        
        return self.bar_container
    
    def _update_animation(self, frame):
        """Update function for animation."""
        # Update the heights of the bars
        for i, bar in enumerate(self.bar_container):
            bar.set_height(self.history[frame][i])
        
        # Color based on whether the item is in sorted position
        is_sorted = True
        for i in range(len(self.history[frame]) - 1):
            if self.history[frame][i] > self.history[frame][i + 1]:
                is_sorted = False
                break
        
        # Update colors - skyblue for unsorted, green for sorted
        for bar in self.bar_container:
            bar.set_color('skyblue')
        
        if is_sorted:
            for bar in self.bar_container:
                bar.set_color('limegreen')
                
        # Update title with trace information
        comparisons = self.trace_data.get("comparisons", 0)
        swaps = self.trace_data.get("swaps", 0)
        title = (f"{self.algorithm_name} - Frame {frame}/{len(self.history)-1}\n"
                f"Comparisons: {comparisons}, Swaps: {swaps}")
        self.ax.set_title(title)
        
        return self.bar_container
        
    def run(self):
        """Run the visualization."""
        # Wrap the algorithm to capture states
        self._wrap_algorithm()
        
        # Run the algorithm to capture all states
        start_time = time.time()
        self.algorithm(self.data)
        end_time = time.time()
        
        print(f"Sorting completed in {end_time - start_time:.6f} seconds")
        print(f"Total frames captured: {len(self.history)}")
        print(f"Comparisons: {self.trace_data.get('comparisons', 0)}")
        print(f"Swaps: {self.trace_data.get('swaps', 0)}")
        
        # Create the animation
        ani = animation.FuncAnimation(
            self.fig, 
            self._update_animation,
            frames=len(self.history),
            init_func=self._init_animation,
            interval=self.interval,
            blit=True,
            repeat=False
        )
        
        # Save animation if requested
        if self.save_animation:
            print(f"Saving animation to {self.output_file}...")
            # Adjust DPI and bitrate based on your needs
            writer = animation.FFMpegWriter(fps=30, metadata=dict(artist='SortKit'),
                                         bitrate=1800)
            ani.save(self.output_file, writer=writer)
            print(f"Animation saved to {self.output_file}")
        
        # Show the animation
        plt.tight_layout()
        plt.show()


def generate_random_data(size: int, max_value: int = 100) -> List[int]:
    """Generate random data for visualization."""
    return [random.randint(1, max_value) for _ in range(size)]


def main():
    parser = argparse.ArgumentParser(description="Visualize sorting algorithms")
    parser.add_argument(
        "--algorithm", 
        type=str,
        required=True,
        help="Sorting algorithm to visualize"
    )
    parser.add_argument(
        "--size", 
        type=int, 
        default=30,
        help="Size of the data set"
    )
    parser.add_argument(
        "--max-value", 
        type=int, 
        default=100,
        help="Maximum value in the data set"
    )
    parser.add_argument(
        "--data-type", 
        choices=["list", "dllist"], 
        default="list",
        help="Data structure to use"
    )
    parser.add_argument(
        "--interval", 
        type=int, 
        default=50,
        help="Animation interval in milliseconds"
    )
    parser.add_argument(
        "--save", 
        action="store_true",
        help="Save the animation to a file"
    )
    parser.add_argument(
        "--output", 
        type=str, 
        default="sorting_animation.mp4",
        help="Output file name"
    )
    parser.add_argument(
        "--list-algorithms", 
        action="store_true",
        help="List available algorithms and exit"
    )
    
    args = parser.parse_args()
    
    # Register algorithms for linked list if needed
    if args.data_type == "dllist":
        register_all_for_linked_list()
    
    # List available algorithms if requested
    if args.list_algorithms:
        print("Available algorithms:")
        for algo in list_algorithms():
            print(f"  - {algo}")
        return
    
    # Check if the specified algorithm exists
    available_algorithms = list_algorithms()
    if args.algorithm not in available_algorithms:
        print(f"Error: Algorithm '{args.algorithm}' not found.")
        print("Available algorithms:")
        for algo in available_algorithms:
            print(f"  - {algo}")
        return
    
    # Generate random data
    data = generate_random_data(args.size, args.max_value)
    
    # Run the visualization
    visualizer = SortingVisualizer(
        algorithm_name=args.algorithm,
        data=data,
        data_type=args.data_type,
        interval=args.interval,
        save_animation=args.save,
        output_file=args.output
    )
    
    visualizer.run()


if __name__ == "__main__":
    main() 