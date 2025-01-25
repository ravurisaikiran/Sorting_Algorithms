import psutil
import platform
import time
import random
import matplotlib.pyplot as plt

# Insertion Sort 
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Selection Sort 
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Bubble Sort 
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def print_system_info():
    system_info = platform.uname()
    print(f"System: {system_info.system} {system_info.version}")
    print(f"Node Name: {system_info.node}")
    print(f"Release: {system_info.release}")
    print(f"Machine: {system_info.machine}")
    print(f"Processor: {system_info.processor}")

    cpu_freq = psutil.cpu_freq()
    print(f"CPU Frequency: {cpu_freq.current:.2f} MHz")
    print(f"CPU Cores: {psutil.cpu_count(logical=False)} physical, {psutil.cpu_count(logical=True)} logical")

# Benchmark:-
def benchmark_sorting_algorithms():
    input_sizes = [5, 10, 50, 100, 500, 1000, 2000, 5000]
    insertion_times = []
    selection_times = []
    bubble_times = []

    for size in input_sizes:
        arr = [random.randint(0, 10000) for _ in range(size)]
        print(f"\nInput size: {size}")

        # For Time Insertion Sort
        start = time.time()
        insertion_sort(arr[:])  # Copy to avoid in-place modification
        elapsed_time = time.time() - start
        insertion_times.append(elapsed_time)
        print(f"Insertion Sort: {elapsed_time:.6f} seconds")

        # For Time Selection Sort
        start = time.time()
        selection_sort(arr[:])  # Copy to avoid in-place modification
        elapsed_time = time.time() - start
        selection_times.append(elapsed_time)
        print(f"Selection Sort: {elapsed_time:.6f} seconds")

        # For Time Bubble Sort
        start = time.time()
        bubble_sort(arr[:])  # Copy to avoid in-place modification
        elapsed_time = time.time() - start
        bubble_times.append(elapsed_time)
        print(f"Bubble Sort: {elapsed_time:.6f} seconds")

    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, insertion_times, label="Insertion Sort", marker="o")
    plt.plot(input_sizes, selection_times, label="Selection Sort", marker="o")
    plt.plot(input_sizes, bubble_times, label="Bubble Sort", marker="o")

    plt.title("Sorting Algorithm Benchmark")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.grid()
    plt.show()
    
def main():
    print("System Information:")
    print_system_info()
    print("\nBenchmarking Sorting Algorithms:")
    benchmark_sorting_algorithms()

if __name__ == "__main__":
    main()
