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

import time
import random
from typing import Dict, List, Callable, Optional, Tuple
import statistics

from sortkit.registry import ALGORITHMS, list_algorithms


def generate_random_data(size: int, seed: Optional[int] = None) -> List[int]:
    """
    Generate a list of random integers.
    
    Args:
        size: Number of elements to generate
        seed: Optional seed for reproducibility
        
    Returns:
        A list of random integers
    """
    if seed is not None:
        random.seed(seed)
    return [random.randint(-1000, 1000) for _ in range(size)]


def generate_sorted_data(size: int) -> List[int]:
    """
    Generate a sorted list of integers.
    
    Args:
        size: Number of elements to generate
        
    Returns:
        A sorted list of integers
    """
    return list(range(size))


def generate_reversed_data(size: int) -> List[int]:
    """
    Generate a reversed (descending) list of integers.
    
    Args:
        size: Number of elements to generate
        
    Returns:
        A reversed list of integers
    """
    return list(range(size - 1, -1, -1))


def benchmark_algorithm(
    algorithm: Callable, data: List[int], runs: int = 3
) -> Dict[str, float]:
    """
    Benchmark a sorting algorithm on the given data.
    
    Args:
        algorithm: The sorting function to benchmark
        data: The input data for sorting
        runs: Number of runs to average over
        
    Returns:
        Dictionary with timing results
    """
    times = []
    
    for _ in range(runs):
        # Make a copy of the data for each run
        data_copy = data.copy()
        
        # Time the execution
        start = time.perf_counter()
        algorithm(data_copy)
        end = time.perf_counter()
        
        times.append(end - start)
    
    return {
        "min": min(times),
        "max": max(times),
        "avg": statistics.mean(times),
        "median": statistics.median(times),
    }


def run_benchmarks(
    sizes: List[int] = [100, 1000, 10000],
    algorithms: Optional[List[str]] = None,
    runs: int = 3,
) -> Dict[str, Dict[str, Dict[str, Dict[str, float]]]]:
    """
    Run benchmarks for multiple algorithms and data sizes.
    
    Args:
        sizes: List of data sizes to benchmark
        algorithms: List of algorithm names to benchmark (defaults to all)
        runs: Number of runs to average over
        
    Returns:
        Nested dictionary with benchmark results:
        {data_type: {size: {algorithm_name: {timing_metrics}}}}
    """
    results = {}
    
    # Use all algorithms if none are specified
    if algorithms is None:
        algorithms = list_algorithms()
    
    # Map of data type names to generator functions
    data_generators = {
        "random": generate_random_data,
        "sorted": generate_sorted_data,
        "reversed": generate_reversed_data,
    }
    
    # Run benchmarks for each data type, size, and algorithm
    for data_type, generator in data_generators.items():
        results[data_type] = {}
        
        for size in sizes:
            results[data_type][size] = {}
            data = generator(size)
            
            for algo_name in algorithms:
                algorithm = ALGORITHMS[algo_name]
                results[data_type][size][algo_name] = benchmark_algorithm(
                    algorithm, data, runs
                )
    
    return results


def print_benchmark_results(results: Dict[str, Dict[str, Dict[str, Dict[str, float]]]]) -> None:
    """
    Print benchmark results as a formatted table.
    
    Args:
        results: The benchmark results from run_benchmarks
    """
    # Print header
    print("\n===== SORTKIT BENCHMARK RESULTS =====\n")
    
    # For each data type
    for data_type, size_data in results.items():
        print(f"\n--- Data Type: {data_type} ---\n")
        
        # Print table headers
        headers = ["Size", "Algorithm", "Min (s)", "Avg (s)", "Max (s)", "Median (s)"]
        header_row = "| " + " | ".join(headers) + " |"
        separator = "|" + "|".join(["-" * (len(h) + 2) for h in headers]) + "|"
        
        print(header_row)
        print(separator)
        
        # For each size and algorithm
        for size, algo_data in size_data.items():
            for algo_name, metrics in algo_data.items():
                row_data = [
                    str(size),
                    algo_name,
                    f"{metrics['min']:.6f}",
                    f"{metrics['avg']:.6f}",
                    f"{metrics['max']:.6f}",
                    f"{metrics['median']:.6f}",
                ]
                row = "| " + " | ".join(row_data) + " |"
                print(row)
        
        print("\n")


if __name__ == "__main__":
    # Example usage when this file is run directly
    results = run_benchmarks()
    print_benchmark_results(results)
