class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean = ''.join(c for c in s if c.isalnum()).lower()
        print(clean)

        return clean == clean[::-1]