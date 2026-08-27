def largest_element(arr: list[int], n: int) -> int:
    """
    Return the largest element among the first n items.

    Time: O(n)
    Space: O(1)
    """
    largest: int = arr[0]

    # Check each element and update the maximum.
    for i in range(1, n):
        if arr[i] > largest:
            largest = arr[i]

    return largest