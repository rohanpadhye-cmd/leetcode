class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ''.join(c for c in s if c.isalnum()).lower()
        return temp == temp[::-1]