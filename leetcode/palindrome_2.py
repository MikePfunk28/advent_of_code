class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Check if the integer is a palindrome by converting to string
        if str(x) == str(x)[::-1]:
            return True
        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(121))
    print(sol.isPalindrome(-121))
    print(sol.isPalindrome(10))