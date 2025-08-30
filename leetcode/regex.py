import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # take in regular expression, evaluate it, then
        # use that to see if it matches the string
        return bool(re.fullmatch(p, s))



if __name__ == '__main__':

    sol = Solution()
    print(sol.isMatch("aa", "a"))
    print(sol.isMatch("aa", "a*"))
    print(sol.isMatch("ab", ".*"))
    print(sol.isMatch("aab", "c*a*b"))
    print(sol.isMatch("mississippi", "mis*is*p*."))