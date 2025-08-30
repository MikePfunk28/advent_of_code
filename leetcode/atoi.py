class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        # Determine the sign by having sign = 1
        # We assume sign is positive, then we check
        # also when in algebra we learn x is really 1x,
        # so you could have + - and that would be 1 or -1.
        # same here with the sign, if - then -1.
        sign = 1
        i = 0
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1

        num = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        # Boundary for 32-bit signed integer
        num *= sign
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        return num


if __name__ == "__main__":
    sol = Solution()
    print(sol.myAtoi("-91283472332"))
# -2147483648
