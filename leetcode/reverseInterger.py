class Solution:
    def reverse(self, x: int) -> int:
        # I need to rework this solution
        # actually one of the interesting things is the test case
        # goes out of bounds on purpose

        # Essentially I just realized that it uses the range in the test
        # case.  So it has to be in bounds of 32bit integer.

        self.x = x
        # define the range of the 32bit or use numpy
        n = -2**31 <= x <= 2**31 - 1
        # convert to string to then reverse with slicing
        # then convert back to int
        # then check if it is in the range
        x = str(x)
        x = x[::-1]
        if x[-1] == "-":
            x = "-" + x[:-1]
        if not n or int(x) < -2**31 or int(x) > 2**31 - 1:
            return 0
        return int(x)

print(Solution().reverse(-223))
mystring = "hello world"
print(mystring[:-1])