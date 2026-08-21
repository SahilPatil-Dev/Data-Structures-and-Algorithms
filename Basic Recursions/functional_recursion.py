class Solution:
    def functional_recursion(self, i: int, s: str) -> bool:
        # Base case: if we reach or pass the middle, it's a palindrome
        if i >= len(s) // 2:
            return True
        # If characters don't match, it's not a palindrome
        if s[i] != s[len(s) - i - 1]:
            return False
        # return the recursive call result
        return self.functional_recursion(i + 1, s)
       
# Time Complexity: O(n/2)
# Space Complexity: O(n/2)