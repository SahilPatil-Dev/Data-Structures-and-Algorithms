class Solution:

    # Brute Force
    def majorityElement_brute_force(arr: list):
        """
        Check the frequency of every element.
        Time: O(n²) | Space: O(1)
        """
        n = len(arr)

        # For every element → O(n)
        for i in range(n):
            count = 0

            # Count its occurrences → O(n)
            for j in range(n):
                if arr[j] == arr[i]:
                    count += 1

            # Majority means frequency > n / 2
            if count > n // 2:
                return arr[i]

        return -1


    # Better - Hashing
    def majorityElement_better(arr: list):
        """
        Store the frequency of each element.
        Time: O(n) average | Space: O(n)
        """
        frequency = {}  # At most n unique elements → O(n) space

        # One loop + hash update → O(n) average
        for num in arr:
            frequency[num] = frequency.get(num, 0) + 1

        # At most n elements → O(n)
        for num, count in frequency.items():
            if count > len(arr) // 2:
                return num

        return -1


    # Optimal - Boyer-Moore Voting Algorithm
    def majorityElement_optimal(arr: list):
        """
        Find the majority element using Boyer-Moore voting.
        Time: O(n) | Space: O(1)
        """
        candidate = None
        count = 0

        # Find the possible majority candidate → O(n)
        for num in arr:

            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        # Verify candidate if majority is not guaranteed.
        count = 0

        # Verification pass → O(n)
        for num in arr:
            if num == candidate:
                count += 1

        if count > len(arr) // 2:
            return candidate

        return -1