class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_prime = ""
        for c in s:
            if c.isalnum():
                s_prime += c.lower()
        return s_prime == s_prime[::-1]