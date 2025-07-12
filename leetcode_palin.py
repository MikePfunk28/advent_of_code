# LeetCode Problem: Longest Palindromic Substring

import datetime
import logging

# Problem Link: https://leetcode.com/problems/longest-palindromic-substring/
# Problem Statement: Given a string s, return the longest palindromic substring in s.

# Configure logging at module level
FORMAT = '%(asctime)s %(name)s %(levelname)s: %(message)s'
logging.basicConfig(
    filename='palindrome.log',
    level=logging.INFO,
    format=FORMAT,
    filemode='a'
)

# Create logger for this module
logger = logging.getLogger(__name__)


class Solution:
    def __init__(self):
        """Initialize Solution class with logging support"""
        self.logger = logger

    def longestPalindrome(self, s: str) -> str:  # type: ignore
        """Find the longest palindromic substring in the given string"""
        longest = ""
        start = datetime.datetime.now()

        # Log the input string
        self.logger.info(
            f"Finding longest palindrome in string of length {len(s)}")

        # Define base cases for while loop
        if len(s) == 0:
            self.logger.warning("Empty string provided as input")
            return ""

        if len(s) == 1:
            self.logger.info(
                "Single character string - returning as palindrome")
            return s


# Second way of implementing this solution using a more efficient approach.
# As nested loops are not efficient for larger strings.

        # Split the string into characters and iterate through each character
        for i in range(len(s)):
            # Odd length palindromes
            # Define left and right pointers, like making a linked list
            # and expand around the center
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(longest):
                    longest = s[left:right+1]
                left -= 1
                right += 1

            # Even length palindromes
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(longest):
                    longest = s[left:right+1]
                left -= 1
                right += 1        # Benchmarking the time needed - add logs here
        end = datetime.datetime.now()
        time_taken = end - start
        self.logger.info("Algorithm completed in %s seconds",
                         time_taken.total_seconds())
        self.logger.info(
            "Found palindrome: '%s' with length %d", longest, len(longest))

        print(f"Time taken: {time_taken}")
        return longest


input_text = "babad"
solution = Solution().longestPalindrome(input_text)
print(f"Longest palindromic substring in '{input_text}' is: '{solution}'")

input_text = "cbbd"
solution = Solution().longestPalindrome(input_text)
print(f"Longest palindromic substring in '{input_text}' is: '{solution}'")

input_text = "cbfareegrhrtefecwgnhwwdujohfhjflkhjsoidfyhghakjdfpabbaababbaojfokqahjfdabbafkhosdgjalkewmnflkhjsaabbaabbacacacojhdflwejnfkNmfslksdghjbd"
solution = Solution().longestPalindrome(input_text)
print(f"Longest palindromic substring in '{input_text}' is: '{solution}'")
