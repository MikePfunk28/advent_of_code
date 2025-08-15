def expand(s: str, l: int, r: int) -> tuple[int, int]:
    n = len(s)
    while l >= 0 and r < n and s[l] == s[r]:
        l -= 1
        r += 1
    return l + 1, r - 1  # inclusive bounds


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        res = ""
        resLen = 0

        for i in range(n):
            # odd
            l, r = expand(s, i, i)
            if r - l + 1 > resLen:
                res = s[l:r+1]
                resLen = r - l + 1
            # even
            l, r = expand(s, i, i + 1)
            if r - l + 1 > resLen:
                res = s[l:r+1]
                resLen = r - l + 1

        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("babad"))