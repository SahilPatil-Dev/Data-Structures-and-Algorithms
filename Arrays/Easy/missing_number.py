class Solution:

    # Brute Force
    def MissingNumbers_brute_force(arr: list, n: int):
        """
        Find the missing number using brute force.

        Approach:
        - Check every number from 0 to n.
        - Search for each number in the array.
        - If a number is not found, it is the missing number.

        Time Complexity:
            O(n²)

        Space Complexity:
            O(1)
        """
        for i in range(n + 1):
            flag = 0

            for j in arr:
                if j == i:
                    flag = 1
                    break

            if flag == 0:
                return i

    # Better
    def MissingNumbers_better(arr: list, n: int):
        """
        Find the missing number using a hash array.

        Approach:
        - Create a hash array to store the presence of each number.
        - Mark every number present in the input array.
        - The index with value 0 is the missing number.

        Time Complexity:
            O(n)

        Space Complexity:
            O(n)
        """
        hash = [0] * (n + 1)

        for i in arr:
            hash[i] = 1

        for i in range(n + 1):
            if hash[i] == 0:
                return i

    # Optimal - Sum
    def MissingNumbers_optimal_sum(arr: list, n: int):
        """
        Find the missing number using the sum formula.

        Approach:
        - Calculate the sum of numbers from 0 to n:
              n * (n + 1) / 2
        - Calculate the sum of all elements in the array.
        - The difference between both sums is the missing number.

        Time Complexity:
            O(n)

        Space Complexity:
            O(1)
        """
        total_sum = n * (n + 1) // 2
        array_sum = 0

        for i in range(n - 1):
            array_sum += arr[i]

        return total_sum - array_sum

    # Optimal - XOR
    def MissingNumbers_optimal_xor(arr: list, n: int):
        """
        Find the missing number using XOR.

        Approach:
        - XOR all numbers from 1 to n.
        - XOR all elements of the array.
        - Same numbers cancel each other:
              x ^ x = 0
        - The remaining value is the missing number.

        Time Complexity:
            O(n)

        Space Complexity:
            O(1)
        """
        xor1 = 0
        xor2 = 0

        for i in range(n - 1):
            xor2 = xor2 ^ arr[i]
            xor1 = xor1 ^ (i + 1)
        xor1 = xor1 ^ n
        return xor1 ^ xor2