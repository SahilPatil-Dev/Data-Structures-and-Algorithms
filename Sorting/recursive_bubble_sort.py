def bubble_sort(arr, n):
    """
    Sort the first `n` elements of `arr` in ascending order
    using recursive Bubble Sort.

    Time Complexity:
        Best:    O(n)    — if optimized with an early-exit check
        Average: O(n²)
        Worst:   O(n²)

    Space Complexity:
        O(n) — recursive call stack
    """
    # Base case: one element is already sorted.
    if n <= 1:
        return

    # Perform one pass: move the largest element to the end.
    for j in range(n - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # Recursively sort the remaining elements.
    bubble_sort(arr, n - 1)