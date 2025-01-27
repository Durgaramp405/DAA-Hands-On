import time
import psutil
import matplotlib.pyplot as plt
import numpy as np
from GPUtil import getGPUs

# Bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_x = i
        for j in range(i+1, n):
            if arr[j] < arr[min_x]:
                min_x = j
        arr[i], arr[min_x] = arr[min_x], arr[i]

# Insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        k = arr[i]
        j = i - 1
        while j >= 0 and k < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = k

# Benchmarking and system usage monitoring
def benchmark_sorting_algorithms():
    input_sizes = [100, 500, 1000, 5000, 10000,50000]
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort
    }

    runtime_data = {alg: [] for alg in algorithms.keys()}
    system_data = {"CPU": [], "RAM": []}

    for size in input_sizes:
        arr = np.random.randint(0, 10000, size).tolist()

        for name, func in algorithms.items():
            arr_copy = arr.copy()
            start_time = time.time()
            func(arr_copy)
            end_time = time.time()
            runtime_data[name].append(end_time - start_time)

    # Record system usage
        cpu_usage = psutil.cpu_percent(interval=1)
        ram_usage = psutil.virtual_memory().percent
        system_data["CPU"].append(cpu_usage)
        system_data["RAM"].append(ram_usage)

    # Runtime vs input size
    for name, runtimes in runtime_data.items():
        plt.plot(input_sizes, runtimes, label=name)

    plt.xlabel("Input Size")
    plt.ylabel("Runtime (in seconds)")
    plt.title("Sorting Algorithm Runtime Comparison")
    plt.legend()
    plt.grid()
    plt.show()

    # Display system usage
    print("System Benchmark Data:")
    for size, cpu, ram in zip(input_sizes, system_data["CPU"], system_data["RAM"]):
        print(f"Input Size: {size}, CPU Usage: {cpu}%, RAM Usage: {ram}%")

if __name__ == "__main__":
    benchmark_sorting_algorithms()
