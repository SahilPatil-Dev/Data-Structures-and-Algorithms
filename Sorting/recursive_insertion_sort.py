def insertion_sort(arr, i, n):
    """
    Sort an array in ascending order using recursive Insertion Sort.

    Time Complexity:
        Best:    O(n)
        Average: O(n²)
        Worst:   O(n²)

    Space Complexity:
        O(n) — recursive call stack
    """
    # Base case: all elements have been processed.
    if i >= n:
        return

    j = i

    # Move the current element left until it reaches its correct position.
    while j > 0 and arr[j - 1] > arr[j]:
        arr[j - 1], arr[j] = arr[j], arr[j - 1]
        j -= 1

    # Recursively process the next element.
    insertion_sort(arr, i + 1, n)