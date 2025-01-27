**Argue Selection Sort Correctness**:

**Selection Sort Algorithm**:

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_x = i
        for j in range(i+1, n):
            if arr[j] < arr[min_x]:
                min_x = j
        arr[i], arr[min_x] = arr[min_x], arr[i]


Selection sort is something that divides the input array into two parts: the sorted subarray and unsorted subarray. The algorithm repeatedly selects the smallest element from the unsorted subarray and moves it to the end of the sorted subarray, growing the sorted portion of the array step by step.

**Example**:

Let us consider an array for sorting 
arr = [65,30,10,22,7]

1) **First Iteration(i=0)**:
-> The minimum element from the unsorted portion [65,30,10,22,7] is 7.
-> Swap 7 with arr[0] = [7,65,30,10,22]
2) **Second Iteration(i=1)**:
-> The minimum element from the unsorted portion [7,65,30,10,22] is 10.
-> Swap 10 with arr[1] = [7,10,65,30,22]
3) **Third Iteration(i=2)**:
-> The minimum element from the unsorted portion [7,10,65,30,22] is 22.
-> Swap 22 with arr[2] = [7,10,22,65,30]
4) **Fourth Iteration(i=3)**:
-> The minimum element from the unsorted portion [7,10,22,65,30] is 30.
-> Swap 30 with arr[3] = [7,10,22,30,65]
5) **Fifth Iteration(i=5)**:
-> The array is fully sorted.

**Conclusion**:
Through each iteration, selection sort places the smallest element in its correct position, which guarantees the array is sorted by the end of the process. This ensures that the algorithm is correct, as the partial sorting after each iteration leads to a fully sorted array by the end.
