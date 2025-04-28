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
from typing import List, Dict, Any, Optional, Tuple

import matplotlib.pyplot as plt
import numpy as np

from sortkit.algorithms.registry import get_algorithm, list_algorithms
from sortkit.structs.dllist import DoublyLinkedList, get_linked_list_algorithm
from sortkit.structs.adapter import register_all_for_linked_list


def generate_random_data(size: int, max_value: int = 1000) -> List[int]:
    """Generate a list of random integers."""
    return [random.randint(0, max_value) for _ in range(size)]


def measure_performance(
    algorithm_name: str, 
    data: List[int], 
    data_type: str = "list"
) -> Tuple[float, int, int]:
    """
    Measure the performance of a sorting algorithm.
    
    Args:
        algorithm_name: Name of the algorithm to test
        data: Data to sort
        data_type: Type of data structure to use ("list" or "dllist")
        
    Returns:
        Tuple containing (execution_time, comparisons, swaps)
    """
    # Create a copy of the data to avoid modifying the original
    if data_type == "list":
        data_copy = data.copy()
        algorithm = get_algorithm(algorithm_name)
    else:  # dllist
        data_copy = DoublyLinkedList(data)
        algorithm = get_linked_list_algorithm(algorithm_name)
    
    # Reset trace counters
    algorithm.reset_trace()
    
    # Measure execution time
    start_time = time.time()
    sorted_data = algorithm(data_copy)
    end_time = time.time()
    
    # Get trace data
    trace_data = algorithm.get_trace()
    comparisons = trace_data.get("comparisons", 0)
    swaps = trace_data.get("swaps", 0)
    
    return end_time - start_time, comparisons, swaps


def compare_algorithms(
    algorithms: List[str],
    sizes: List[int],
    data_type: str = "list",
    repetitions: int = 3
) -> Dict[str, Dict[int, Dict[str, float]]]:
    """
    Compare performance of multiple algorithms across different data sizes.
    
    Args:
        algorithms: List of algorithm names to compare
        sizes: List of data sizes to test
        data_type: Type of data structure to use ("list" or "dllist")
        repetitions: Number of times to repeat each test for averaging
        
    Returns:
        Dictionary with performance metrics
    """
    results = {}
    
    for algorithm in algorithms:
        results[algorithm] = {}
        
        for size in sizes:
            print(f"Testing {algorithm} with {size} elements...")
            total_time = 0
            total_comparisons = 0
            total_swaps = 0
            
            for _ in range(repetitions):
                data = generate_random_data(size)
                time_taken, comparisons, swaps = measure_performance(
                    algorithm, data, data_type
                )
                total_time += time_taken
                total_comparisons += comparisons
                total_swaps += swaps
            
            # Calculate averages
            avg_time = total_time / repetitions
            avg_comparisons = total_comparisons / repetitions
            avg_swaps = total_swaps / repetitions
            
            results[algorithm][size] = {
                "time": avg_time,
                "comparisons": avg_comparisons,
                "swaps": avg_swaps
            }
    
    return results


def plot_results(results: Dict[str, Dict[int, Dict[str, float]]], metric: str = "time"):
    """Plot the performance results."""
    plt.figure(figsize=(10, 6))
    
    algorithms = list(results.keys())
    sizes = sorted(list(results[algorithms[0]].keys()))
    
    for algorithm in algorithms:
        values = [results[algorithm][size][metric] for size in sizes]
        plt.plot(sizes, values, marker='o', label=algorithm)
    
    plt.xlabel("Input Size")
    
    if metric == "time":
        plt.ylabel("Execution Time (seconds)")
        plt.title("Sorting Algorithm Performance: Execution Time")
    elif metric == "comparisons":
        plt.ylabel("Number of Comparisons")
        plt.title("Sorting Algorithm Performance: Comparisons")
    elif metric == "swaps":
        plt.ylabel("Number of Swaps")
        plt.title("Sorting Algorithm Performance: Swaps")
    
    plt.legend()
    plt.grid(True)
    plt.savefig(f"sorting_performance_{metric}.png")
    plt.close()


def main():
    parser = argparse.ArgumentParser(description="Compare sorting algorithm performance")
    parser.add_argument(
        "--algorithms", 
        nargs="+", 
        help="Algorithms to compare (default: all available)"
    )
    parser.add_argument(
        "--sizes", 
        nargs="+", 
        type=int, 
        default=[100, 500, 1000, 5000, 10000],
        help="Data sizes to test"
    )
    parser.add_argument(
        "--data-type", 
        choices=["list", "dllist"], 
        default="list",
        help="Data structure to use"
    )
    parser.add_argument(
        "--repetitions", 
        type=int, 
        default=3,
        help="Number of repetitions for each test"
    )
    parser.add_argument(
        "--metrics", 
        nargs="+", 
        choices=["time", "comparisons", "swaps", "all"],
        default=["all"],
        help="Performance metrics to plot"
    )
    
    args = parser.parse_args()
    
    # Register algorithms for linked list if needed
    if args.data_type == "dllist":
        register_all_for_linked_list()
    
    # If no algorithms specified, use all available
    if not args.algorithms:
        args.algorithms = list_algorithms()
    
    # Run comparison
    results = compare_algorithms(
        args.algorithms,
        args.sizes,
        args.data_type,
        args.repetitions
    )
    
    # Plot results
    metrics_to_plot = []
    if "all" in args.metrics:
        metrics_to_plot = ["time", "comparisons", "swaps"]
    else:
        metrics_to_plot = args.metrics
    
    for metric in metrics_to_plot:
        plot_results(results, metric)
        print(f"Plot saved as sorting_performance_{metric}.png")


if __name__ == "__main__":
    main() 