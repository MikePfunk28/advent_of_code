import numpy as np

matrix = np.array([[''] * 7 for _ in range(3)])
element = matrix[0][1]
matrix[0][0] = 'P'
matrix[0][1] = ' '
matrix[0][2] = 'A'
matrix[0][3] = ' '
matrix[0][4] = 'H'
matrix[0][5] = ' '
matrix[0][6] = 'N'

matrix[1][0] = 'A'
matrix[1][1] = 'P'
matrix[1][2] = 'L'
matrix[1][3] = 'S'
matrix[1][4] = 'I'
matrix[1][5] = 'I'
matrix[1][6] = 'G'

matrix[2][0] = 'Y'
matrix[2][1] = ' '
matrix[2][2] = 'I'
matrix[2][3] = ' '
matrix[2][4] = 'R'
matrix[2][5] = ' '
matrix[2][6] = ' '

print(matrix)

class Solution:
    # This is the first way of implementing this solution.
    # This is a brute force solution.
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: if numRows is 1 or greater than the length of the string, return the original string
        if numRows == 1 or numRows >= len(s):
            return s

        # Initialize an array with strings
        # Create a list of strings for each row
        cols = [''] * numRows
        # Initialize variables to keep track of the current row and direction
        index, step = 0, 1

        # Iterate through each character in the string
        for char in s:
            # Add the character to the current row
            cols[index] += char
            # If we are at the top or bottom row, reverse the direction
            if index == 0:
                # We have reached the top row, change direction to down
                step = 1
            # If we are at the bottom row, change direction to up
            elif index == numRows - 1:
                # We have reached the bottom row, change direction to up
                step = -1
            # Move to the next row
            index += step

        # Join all the rows to get the final string
        return ''.join(cols)

mystring = Solution().convert("PAYPALISHIRING", 3)
print(mystring)


class Solution2:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s): return s

        # Initialize an array with strings
        result = ""
        # Iterate through each row
        for r in range(numRows):
            # what is our increment, well it takes
            #  2 * (numRows - 1) to get to the next row
            # 0, 4, 8, 12
            increment = 2 * (numRows - 1)
            # Use i to tell us where we are in the string
            # row 0 starts at index 0, row 2 starts at
            # index 2, etc,
            for i in range(r, len(s), increment):
                # Now add the character to the result
                # but rows inbetween has other values
                # we don't want to forget about.
                result += s[i]
                # So we check both if we are in the middle
                # and if we are in bounds, we want to get
                # the extra characters, (current i + increment - 2*r)
                # decreases by 2 each time, so each time we are
                # going to subtract 2*r.  We check if it is inbounds
                # if it is less than the length of the string
                # Only do this in the middle rows, not first or last.
                if r > 0 and r < numRows - 1 and i + increment - 2 * r < len(s):
                    result += s[i + increment - 2 * r]