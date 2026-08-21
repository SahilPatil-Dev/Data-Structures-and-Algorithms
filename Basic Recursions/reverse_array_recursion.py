class Solution:
    def reverse_arr_recursion(self, i: int, arr: list, n: int) -> list:
        """
        Reverses an array in-place using recursion.
        
        Time Complexity: O(N) - Visited N/2 elements, linear time.
        Space Complexity: O(N) - Due to the recursive call stack frame.
        """
        # Base case: if we reach or pass the middle, return the reversed array
        if i >= n // 2:
            return arr
            
        # Swap elements from start and end moving inward
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
        
        # Return the recursive call result
        return self.reverse_arr_recursion(i + 1, arr, n)
