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
import sys
import random
import time
from typing import List, Optional, Any, Dict

from sortkit.registry import ALGORITHMS, list_algorithms, get_algorithm
from sortkit.bench import run_benchmarks, print_benchmark_results


def parse_args() -> argparse.Namespace:
    """
    Parse command line arguments.
    
    Returns:
        The parsed arguments
    """
    parser = argparse.ArgumentParser(
        description="SortKit: Modular Sorting Algorithms Toolkit"
    )
    
    # Create a mutual exclusion group for commands
    cmd_group = parser.add_mutually_exclusive_group(required=True)
    cmd_group.add_argument(
        "--algo", "-a", 
        type=str, 
        choices=list_algorithms(),
        help=f"Sorting algorithm to use (one of: {', '.join(list_algorithms())})"
    )
    cmd_group.add_argument(
        "demo", 
        nargs="?", 
        help="Run a demonstration of all sorting algorithms"
    )
    cmd_group.add_argument(
        "--benchmark", "-b", 
        action="store_true", 
        help="Run benchmarks for all sorting algorithms"
    )
    
    # Other arguments
    parser.add_argument(
        "--size", "-s", 
        type=int, 
        default=10,
        help="Size of the random array to sort (default: 10)"
    )
    parser.add_argument(
        "--trace", "-t", 
        action="store_true",
        help="Show step-by-step tracing of the algorithm"
    )
    parser.add_argument(
        "--linked-list", "-l", 
        action="store_true",
        help="Use doubly-linked list implementation instead of arrays"
    )
    parser.add_argument(
        "--seed", 
        type=int,
        help="Random seed for reproducibility"
    )
    
    return parser.parse_args()


def generate_random_data(size: int, seed: Optional[int] = None) -> List[int]:
    """
    Generate a list of random integers.
    
    Args:
        size: Number of elements to generate
        seed: Random seed for reproducibility
        
    Returns:
        A list of random integers
    """
    if seed is not None:
        random.seed(seed)
    return [random.randint(0, 100) for _ in range(size)]


def print_steps(steps: List[List[int]]) -> None:
    """
    Print sorting steps in a human-readable format.
    
    Args:
        steps: List of lists, each representing a step in the sorting process
    """
    for i, step in enumerate(steps):
        if i == 0:
            print(f"Initial: {step}")
        elif i == len(steps) - 1:
            print(f"Final:   {step}")
        else:
            print(f"Step {i}: {step}")


def run_algorithm(algorithm_name: str, size: int, trace: bool, seed: Optional[int]) -> None:
    """
    Run a sorting algorithm and display the results.
    
    Args:
        algorithm_name: Name of the algorithm to run
        size: Size of the input array
        trace: Whether to show step-by-step tracing
        seed: Random seed for reproducibility
    """
    algorithm = get_algorithm(algorithm_name)
    data = generate_random_data(size, seed)
    
    print(f"\nRunning {algorithm_name.capitalize()} Sort on list of size {size}")
    print(f"Input: {data}")
    
    if trace:
        start_time = time.perf_counter()
        steps = list(algorithm(data, trace=True))
        end_time = time.perf_counter()
        
        print(f"\nSorting steps:")
        print_steps(steps)
    else:
        start_time = time.perf_counter()
        result = algorithm(data)
        end_time = time.perf_counter()
        
        print(f"Output: {result}")
    
    elapsed = end_time - start_time
    print(f"\nTime elapsed: {elapsed:.6f} seconds")


def run_demo(size: int, trace: bool, seed: Optional[int]) -> None:
    """
    Run a demonstration of all sorting algorithms.
    
    Args:
        size: Size of the input array
        trace: Whether to show step-by-step tracing
        seed: Random seed for reproducibility
    """
    print("\n===== SORTKIT DEMONSTRATION =====\n")
    
    # Ensure the same data is used for all algorithms in the demo
    if seed is not None:
        random.seed(seed)
    data = generate_random_data(size)
    
    for algorithm_name in list_algorithms():
        algorithm = get_algorithm(algorithm_name)
        
        print(f"\n--- {algorithm_name.capitalize()} Sort ---")
        print(f"Input: {data}")
        
        if trace:
            start_time = time.perf_counter()
            steps = list(algorithm(data.copy(), trace=True))
            end_time = time.perf_counter()
            
            print("\nSorting steps:")
            print_steps(steps)
        else:
            start_time = time.perf_counter()
            result = algorithm(data.copy())
            end_time = time.perf_counter()
            
            print(f"Output: {result}")
        
        elapsed = end_time - start_time
        print(f"Time elapsed: {elapsed:.6f} seconds\n")
        print("-" * 50)


def main() -> None:
    """Main entry point for the CLI."""
    args = parse_args()
    
    # Handle the linked list flag
    if args.linked_list:
        # This will be handled once the linked list implementation is completed
        print("Note: Linked list implementation will be used when available.")
    
    # Run the appropriate command
    if args.demo is not None:
        run_demo(args.size, args.trace, args.seed)
    elif args.benchmark:
        results = run_benchmarks(sizes=[100, 1000, args.size])
        print_benchmark_results(results)
    else:  # --algo was specified
        run_algorithm(args.algo, args.size, args.trace, args.seed)


if __name__ == "__main__":
    main()
