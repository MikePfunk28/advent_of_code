class Solution2:
    def lengthOfLongestSubstring2(self, s: str) -> int:
        new_s = self.convert_toset(s)
        return len(new_s)

    def convert_toset(self, s):
        s = set(s)
        return s


# start with a window size, and index i and index j, and length of the string k.
# max_length is 0 and max_substring is empty.
# while j < k:
# if the window is not in the set, add it to the set, and increment j.
# if the window is in the set, remove the first character of the window, and increment i.
# if the window is not in the set, and the length of the window is greater than the max_length, set max_length to the length of the window, and set max_substring to the window.
# return max_substring


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        max_substring = ""
        window = set()
        i = 0
        j = 0
        k = len(s)
        while j < k:
            if s[j] not in window:
                window.add(s[j])
                j += 1
            else:
                window.remove(s[i])
                i += 1
            if len(window) > max_length:
                max_length = len(window)
                max_substring = "".join(window)
        return len(max_substring)


s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))

max_length = s.lengthOfLongestSubstring("pwwkew")
print(max_length)

s2 = Solution2()
print(s2.lengthOfLongestSubstring2("pwwkew"))

max_length = s2.lengthOfLongestSubstring2("pwwkew")
print(max_length)
