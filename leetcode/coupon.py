import re
from typing import List
import datetime
import time

class Solution:
    def validate_coupons(
        self,
        codes: List[str],
        business_line: List[str],
        is_active: List[bool]
    ) -> List[str]:
        order = {"electronics": 0, "grocery": 1,
                 "pharmacy": 2, "restaurant": 3}
        valid = []

        for one_code, code_business, active in zip(codes, business_line, is_active):
            # Short-circuit evaluation: if any condition is False, the rest are not evaluated
            # This is a performance optimization - we skip expensive operations if early conditions fail
            if not (active and one_code and code_business in order):
                continue
            # Generator expression inside any() - creates an iterator, not a list
            # This is memory efficient and stops at first True value (short-circuits)
            if any(not (ch.isalnum() or ch == "_") for ch in one_code):
                continue
            # Dictionary lookup is O(1) average case due to hash table implementation
            valid.append((order[code_business], one_code))
        # Python uses TimSort algorithm - hybrid of merge sort and insertion sort
        # Stable sort means equal elements maintain their relative order
        # Lambda creates anonymous function
        valid.sort(key=lambda x: (x[0], x[1]))
        # Tuple unpacking: _ discards first element, c keeps second element
        # This is Pythonic way to ignore values you don't need
        return [c for _, c in valid]


my_solution = Solution()
my_solution.validate_coupons(
    ["SAVE20", "", "PHARMA5", "SAVE@20"],
    ["restaurant", "grocery", "pharmacy", "restaurant"],
    [True, True, True, True]
)

# ["PHARMA5","SAVE20"]


class Solution2:
    def validate_coupons(
        self,
        codes: List[str],
        business_line: List[str],
        is_active: List[bool]
    ) -> List[str]:

        order = {"electronics": 0, "grocery": 1,
                 "pharmacy": 2, "restaurant": 3}
        # Regex compilation happens once - expensive operation moved outside loop
        # Raw string (r'') prevents Python from interpreting backslashes
        # ^ = start, $ = end, + = one or more
        pat = re.compile(r'^[A-Za-z0-9_]+$')
        valid = []
        for one_code, code_business, active in zip(codes, business_line, is_active):
            # Chained boolean conditions with short-circuit evaluation
            # fullmatch() returns Match object (truthy) or None (falsy)
            if active and one_code and pat.fullmatch(one_code) and code_business in order:
                valid.append((order[code_business], one_code))
        # Same TimSort algorithm as Method 1
        valid.sort(key=lambda x: (x[0], x[1]))
        # Variable name in comprehension shadows the outer variable intentionally
        return [one_code for _, one_code in valid]


my_solution2 = Solution2()
my_solution2.validate_coupons(
    ["SAVE20", "", "PHARMA5", "SAVE@20"],
    ["restaurant", "grocery", "pharmacy", "restaurant"],
    [True, True, True, True]
)


class Solution3:
    def validate_coupons(self, codes: List[str], business_line: List[str], is_active: List[bool]) -> List[str]:


        def goods(s):
            # Explicit string comparison is more readable than truthy/falsy check
            if s == "":
                return False
            # Traditional for loop - sometimes clearer than comprehensions for simple logic
            for c in s:
                # De Morgan's law: not (A or B) = (not A) and (not B)
                if not c.isalnum() and c != "_":
                    return False  # Early return - fail fast pattern
            return True  # Only reached if all characters are valid

        arr = []  # Different variable naming convention than other methods
        # Shortened variable names for conciseness in loop
        for c, b, a in zip(codes, business_line, is_active):
            # Tuple membership test: in operator checks each element sequentially
            # O(n) complexity but n=4 so effectively constant time
            if a and b in ("electronics", "grocery", "pharmacy", "restaurant") and goods(c):
                # Stores business name directly instead of priority number
                # This creates alphabetical sorting, not priority sorting
                arr.append((b, c))
        # Same sorting algorithm but different data structure
        # Sorts by business name alphabetically
        arr.sort(key=lambda x: (x[0], x[1]))
        # Same tuple unpacking pattern as other methods
        return [c for _, c in arr]


my_solution3 = Solution3()
my_solution3.validate_coupons(
    ["SAVE20", "", "PHARMA5", "SAVE@20"],
    ["restaurant", "grocery", "pharmacy", "restaurant"],
    [True, True, True, True]
)

print(my_solution3.validate_coupons(
    ["SAVE20", "", "PHARMA5", "SAVE@20"],
    ["restaurant", "grocery", "pharmacy", "restaurant"],
    [True, True, True, True]
))
print(my_solution2.validate_coupons(
    ["SAVE20", "", "PHARMA5", "SAVE@20"],
    ["restaurant", "grocery", "pharmacy", "restaurant"],
    [True, True, True, True]
))
print(my_solution.validate_coupons(
    ["SAVE20", "", "PHARMA5", "SAVE@20"],
    ["restaurant", "grocery", "pharmacy", "restaurant"],
    [True, True, True, True]
))
print(my_solution)

# Performance timing snippet - add this at the bottom of your file

# Test data
test_codes = ["SAVE20", "", "PHARMA5", "SAVE@20"]
test_business = ["restaurant", "grocery", "pharmacy", "restaurant"]
test_active = [True, True, True, True]

# Time Method 1 (Manual)
start_time = time.perf_counter()
result1 = my_solution.validate_coupons(test_codes, test_business, test_active)
end_time = time.perf_counter()
method1_time = end_time - start_time

# Time Method 2 (Regex)
start_time = time.perf_counter()
result2 = my_solution2.validate_coupons(test_codes, test_business, test_active)
end_time = time.perf_counter()
method2_time = end_time - start_time

# Time Method 3 (Helper Function)
start_time = time.perf_counter()
result3 = my_solution3.validate_coupons(test_codes, test_business, test_active)
end_time = time.perf_counter()
method3_time = end_time - start_time

# Print results
print(f"Method 1 (Manual): {method1_time:.6f} seconds - Result: {result1}")
print(f"Method 2 (Regex): {method2_time:.6f} seconds - Result: {result2}")
print(f"Method 3 (Helper): {method3_time:.6f} seconds - Result: {result3}")
print(f"All methods returned the same result: {result1 == result2 == result3}")
