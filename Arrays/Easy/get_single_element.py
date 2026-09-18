from collections import Counter


# 1. Brute Force Approach
def get_single_element_bruteforce(arr):
    """
    Find the element that appears exactly once using brute force.

    Time Complexity:
        O(n^2)
        - For every element, we traverse the entire array
          to count its frequency.

    Space Complexity:
        O(1)
        - No extra data structure is used.
    """

    n = len(arr)

    # Traverse through every element
    for i in range(n):
        num = arr[i]
        count = 0

        # Count how many times the current element appears
        for j in range(n):
            if arr[j] == num:
                count += 1

        # If the element occurs only once, return it
        if count == 1:
            return num

    # Return -1 if no single element is found
    return -1


# 2. Hash Map Approach
def get_single_element_hash(arr):
    """
    Find the element that appears exactly once using a hash map.

    Time Complexity:
        O(n) average
        - First loop counts frequencies.
        - Second loop searches for the element with frequency 1.

    Space Complexity:
        O(n)
        - The dictionary can store up to n different elements.
    """

    # Dictionary to store frequency of each element
    freq = {}

    # Count the frequency of every element
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    # Find the element whose frequency is exactly 1
    for num in arr:
        if freq[num] == 1:
            return num

    # Return -1 if no single element is found
    return -1


# 3. Counter / Frequency Map Approach
def get_single_element_counter(arr):
    """
    Find the element that appears exactly once using Counter.

    Time Complexity:
        O(n) average
        - Counter traverses the array once.
        - We then traverse the frequency map.

    Space Complexity:
        O(n)
        - Counter stores the frequency of each distinct element.
    """

    # Counter automatically calculates the frequency
    # of every element in the array.
    freq = Counter(arr)

    # Check each element and find the one with frequency 1
    for num, count in freq.items():
        if count == 1:
            return num

    # Return -1 if no single element is found
    return -1


# 4. Sorting Approach
def get_single_element_sort(arr):
    """
    Find the element that appears exactly once using sorting.

    Time Complexity:
        O(n log n)
        - Sorting the array takes O(n log n).
        - The subsequent traversal takes O(n).
        - Overall: O(n log n).

    Space Complexity:
        O(n)
        - sorted(arr) creates a new sorted list.
    """

    # Sort the array so that duplicate elements
    # appear next to each other.
    arr = sorted(arr)

    # Check elements in pairs.
    # If arr[i] != arr[i + 1], arr[i] is the single element.
    for i in range(0, len(arr) - 1, 2):
        if arr[i] != arr[i + 1]:
            return arr[i]

    # If every previous pair matched,
    # the last element must be the single element.
    return arr[-1]


# 5. XOR - Optimal Approach
def get_single_element(arr):
    """
    Find the element that appears exactly once using XOR.

    Time Complexity:
        O(n)
        - We traverse the array exactly once.

    Space Complexity:
        O(1)
        - Only one variable (xor) is used.

    XOR Properties:
        1. a ^ a = 0
        2. a ^ 0 = a
        3. XOR is commutative and associative.

    Therefore, all duplicate elements cancel each other,
    leaving only the element that appears once.
    """

    # Initialize XOR result with 0
    xor = 0

    # XOR every element with the result
    for num in arr:
        xor ^= num

    # All duplicate numbers cancel out,
    # so xor contains the single element.
    return xor