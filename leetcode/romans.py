class Solution:
    def intToRoman(self, num: int) -> str:
        I = 1
        IV = 4
        V = 5
        IX = 9
        X = 10
        XL = 40
        L = 50
        XC = 90
        C = 100
        CD = 400
        D = 500
        CM = 900
        M = 1000

        # Create a list of tuples for Roman numeral values and their symbols
        val = [
            (M, 'M'),
            (CM, 'CM'),
            (D, 'D'),
            (CD, 'CD'),
            (C, 'C'),
            (XC, 'XC'),
            (L, 'L'),
            (XL, 'XL'),
            (X, 'X'),
            (IX, 'IX'),
            (V, 'V'),
            (IV, 'IV'),
            (I, 'I')
        ]
        # Convert the integer to Roman numerals
        roman_numerals = []
        for value, symbol in val:
            while num >= value:
                roman_numerals.append(symbol)
                num -= value
        # Join the Roman numerals into a single string
        # concatenate the list into a string
        return ''.join(roman_numerals)


if __name__ == "__main__":
    solution = Solution()
    print(solution.intToRoman(1994))


class Solution2:
    def RomanToInt(self, s: str) -> int:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC",
                   "L", "XL", "X", "IX", "V", "IV", "I"]
        num = 0
        for i, symbol in enumerate(symbols):
            while s.startswith(symbol):
                num += values[i]
                s = s[len(symbol):]
        return num


if __name__ == "__main__":
    solution = Solution2()
    print(solution.RomanToInt("MCMXCIV"))


class Solution3:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC",
                   "L", "XL", "X", "IX", "V", "IV", "I"]

        result = ""
        for value, symbol in zip(values, symbols):
            count = num // value
            result += symbol * count
            num %= value

        return result

if __name__ == '__main__':
    solution = Solution3()
    print(solution.intToRoman(1994))