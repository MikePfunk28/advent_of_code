class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        # string
        # indexes i and j, to make the window
        # self.s needs to be a string for this to work.
        self.s = ""

        # check if string between i and j is palindromic
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]
                if substring == substring[::-1] and len(substring) > len(self.s):
                    self.s = substring

        return self.s


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("ac"))


# Notes
#
# At first it was only printing the word, but I had to switch i start and end.
# As it j does start at i + 1 which you define in the local loop
# And the string does not end s-1, as that would check all substrings but the last.
# Finally s needed to be a string literal.
class Solution2(object):
    def longestPalindrome2(self, s):
        res = 0
        resLen = 0
        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # while it is a palindrome
                if (r - l + 1) > resLen:
                    res = s[l + r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l: r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        return res

if __name__ == "__main__":
    s = Solution2()
    print(s.longestPalindrome2("ac"))
