import re
from typing import List
import datetime


class Solution:
    def validate_coupons(
        self,
        codes: List[str],
        business_line: List[str],
        is_active: List[bool]
    ) -> List[str]:
        """
        # Method 1: The Manual Approach - DEEP DIVE EXPLANATION

        ## What's REALLY happening here - Line by Line Breakdown:

        ### Line 13-14: Dictionary-Based Priority System
        ```python
        order = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        ```
        This isn't just "creating a dictionary" - this is implementing a PRIORITY QUEUE system.
        - Why integers? Because Python's sort() uses lexicographical ordering
        - Electronics = 0 means it gets TOP priority in final sorting
        - Restaurant = 3 means it gets LOWEST priority
        - This dictionary serves as a LOOKUP TABLE for O(1) priority assignment

        ### Line 15: The Collection Container
        ```python
        valid = []
        ```
        This empty list isn't just storage - it's a FILTERED ACCUMULATOR.
        - Only coupons that pass ALL validation checks get added
        - Stores tuples, not strings (crucial for sorting later)
        - Acts as intermediate data structure before final transformation

        ### Line 17: The Triple Iterator Pattern
        ```python
        for one_code, code_business, active in zip(codes, business_line, is_active):
        ```
        ZIP is doing HEAVY LIFTING here:
        - Takes 3 separate arrays of length N
        - Creates N tuples of (code, business, active_status)
        - Maintains index relationship without manual tracking
        - Memory efficient - doesn't create new lists, just iterator

        ### Line 18-19: The Triple Gate Validation
        ```python
        if not (active and one_code and code_business in order):
            continue
        ```
        This is a COMPOUND BOOLEAN FILTER with three gates:
        Gate 1: `active` - Must be True (not just truthy)
        Gate 2: `one_code` - Must be non-empty string (empty string is falsy)
        Gate 3: `code_business in order` - Must be valid business type

        The `not (...)` inverts the logic - if ANY gate fails, we skip to next iteration
        Using `continue` is PERFORMANCE OPTIMIZATION - skips expensive character validation

        ### Line 21-22: Character-Level Validation Engine
        ```python
        if any(not (ch.isalnum() or ch == "_") for ch in one_code):
            continue
        ```
        This is a GENERATOR EXPRESSION inside ANY():
        - `for ch in one_code` - iterates every character
        - `ch.isalnum()` - checks if alphanumeric (a-z, A-Z, 0-9)
        - `or ch == "_"` - allows underscores specifically
        - `not (...)` - inverts to find BAD characters
        - `any(...)` - returns True if ANY character is bad

        WHY THIS WORKS: Short-circuit evaluation means it stops at FIRST bad character
        Performance: O(k) where k is length of coupon code

        ### Line 23: Tuple Construction for Sorting
        ```python
        valid.append((order[code_business], one_code))
        ```
        This is BRILLIANT sorting preparation:
        - Creates tuple with (priority_number, coupon_code)
        - order[code_business] does O(1) dictionary lookup
        - Tuple's first element becomes PRIMARY sort key
        - Tuple's second element becomes SECONDARY sort key

        ### Line 24: Python's Native Sorting Algorithm
        ```python
        valid.sort(key=lambda x: (x[0], x[1]))
        ```
        This leverages Python's TIMSORT algorithm:
        - Stable sort (maintains relative order of equal elements)
        - O(n log n) time complexity
        - Sorts by tuple comparison: first element, then second element
        - Lambda extracts both elements for explicit sorting

        ### Line 25: List Comprehension Transform
        ```python
        return [c for _, c in valid]
        ```
        Final transformation using TUPLE UNPACKING:
        - `_` discards the priority number (we don't need it anymore)
        - `c` extracts the coupon code
        - Creates new list with only the codes, maintaining sorted order

        ## Why This Approach is GENIUS:
        1. **Memory Efficient**: Only stores valid coupons
        2. **Performance Optimized**: Multiple early-exit conditions
        3. **Maintainable**: Clear separation of concerns
        4. **Extensible**: Easy to add new business types or validation rules
        """

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
        valid.sort(key=lambda x: (x[0], x[1]))  # Lambda creates anonymous function
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

        """
        # Method 2: The Regex Ninja - DEEP DIVE EXPLANATION

        ## What's REALLY happening here - Line by Line Breakdown:

        ### Line 109-110: Dictionary-Based Priority System (Same as Method 1)
        ```python
        order = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        ```
        Identical to Method 1 - establishes business line priorities for sorting.

        ### Line 111: Regex Pattern Compilation - THE GAME CHANGER
        ```python
        pat = re.compile(r'^[A-Za-z0-9_]+$')
        ```
        This is where Method 2 gets its POWER:
        - `re.compile()` - Pre-compiles the regex pattern into a Pattern object
        - `r'^[A-Za-z0-9_]+$'` - Raw string prevents Python escape sequence interference
        - `^` - Anchors to START of string (crucial for security)
        - `[A-Za-z0-9_]` - Character class: letters, digits, underscores
        - `+` - One or more of the preceding characters (rejects empty strings)
        - `$` - Anchors to END of string (prevents partial matches)

        WHY PRE-COMPILE? Performance optimization:
        - Compiling regex is expensive O(m) where m is pattern length
        - Pre-compilation happens ONCE, not for every coupon
        - Pattern object has optimized C-level matching engine

        ### Line 112: Collection Container (Same as Method 1)
        ```python
        valid = []
        ```
        Same filtered accumulator pattern as Method 1.

        ### Line 113: Triple Iterator Pattern (Same as Method 1)
        ```python
        for one_code, code_business, active in zip(codes, business_line, is_active):
        ```
        Same efficient zip iteration as Method 1.

        ### Line 114: The One-Line Validator - ELEGANCE IN ACTION
        ```python
        if active and one_code and pat.fullmatch(one_code) and code_business in order:
        ```
        This is a COMPOUND BOOLEAN CHAIN with four conditions:
        Condition 1: `active` - Must be True
        Condition 2: `one_code` - Must be non-empty (truthy check)
        Condition 3: `pat.fullmatch(one_code)` - THE REGEX MAGIC
        Condition 4: `code_business in order` - Must be valid business type

        THE REGEX MAGIC - `pat.fullmatch(one_code)`:
        - `fullmatch()` vs `match()` - fullmatch requires ENTIRE string to match
        - Returns Match object if valid, None if invalid
        - Match object is truthy, None is falsy
        - Leverages compiled pattern for maximum performance

        SHORT-CIRCUIT EVALUATION:
        - If `active` is False, other conditions never evaluated
        - If `one_code` is empty, regex never called
        - Regex only runs on potentially valid coupons

        ### Line 115: Tuple Construction (Same as Method 1)
        ```python
        valid.append((order[code_business], one_code))
        ```
        Same brilliant tuple construction for sorting preparation.

        ### Line 116: Native Sorting (Same as Method 1)
        ```python
        valid.sort(key=lambda x: (x[0], x[1]))
        ```
        Same TimSort algorithm with tuple comparison.

        ### Line 117: List Comprehension Transform (Same as Method 1)
        ```python
        return [one_code for _, one_code in valid]
        ```
        Same tuple unpacking and final transformation.

        ## Why This Approach is SUPERIOR for Character Validation:
        1. **Performance**: Regex engine is highly optimized C code
        2. **Readability**: Single pattern describes all validation rules
        3. **Maintainability**: Easy to modify validation rules by changing pattern
        4. **Security**: Anchored pattern prevents injection attacks
        5. **Expressiveness**: Complex patterns can be expressed concisely

        ## Performance Analysis:
        - Regex compilation: O(1) - done once
        - Per-coupon validation: O(k) where k is coupon length
        - But with optimized C-level matching vs Python loops
        - Best for complex validation patterns

        ## When to Use Method 2:
        - Complex character validation rules
        - Performance-critical applications
        - When validation logic might change frequently
        - When you need pattern matching beyond simple character checks
        """

        order = {"electronics": 0, "grocery": 1,
                 "pharmacy": 2, "restaurant": 3}
        # Regex compilation happens once - expensive operation moved outside loop
        # Raw string (r'') prevents Python from interpreting backslashes
        pat = re.compile(r'^[A-Za-z0-9_]+$')  # ^ = start, $ = end, + = one or more
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
        """
        # Method 3: The Helper Function Hero - DEEP DIVE EXPLANATION

        ## What's REALLY happening here - Line by Line Breakdown:

        ### Line 268-275: The Helper Function - SEPARATION OF CONCERNS
        ```python
        def goods(s):
            if s == "":
                return False
            for c in s:
                if not c.isalnum() and c != "_":
                    return False
            return True
        ```
        This is FUNCTIONAL PROGRAMMING at its finest:

        #### Line 269: Empty String Guard
        ```python
        if s == "":
            return False
        ```
        - EXPLICIT empty string check (more readable than truthy/falsy)
        - Early return optimization - stops processing immediately
        - Clear intent: empty strings are invalid

        #### Line 270-273: Character Validation Loop
        ```python
        for c in s:
            if not c.isalnum() and c != "_":
                return False
        ```
        This is a FAIL-FAST validation engine:
        - Iterates through each character in the string
        - `c.isalnum()` - checks if character is alphanumeric
        - `and c != "_"` - allows underscores as exception
        - `not (...)` - inverts the logic to find invalid characters
        - `return False` - IMMEDIATELY exits on first invalid character

        #### Line 274: Success Path
        ```python
        return True
        ```
        - Only reached if ALL characters are valid
        - Explicit return for clarity

        ## Why This Helper Function Design is BRILLIANT:
        1. **Single Responsibility**: Function does ONE thing - validates coupon format
        2. **Pure Function**: No side effects, same input always produces same output
        3. **Testable**: Can be unit tested independently
        4. **Reusable**: Could be used by other parts of the system
        5. **Readable**: Function name 'goods' clearly indicates purpose

        ### Line 276: Collection Container
        ```python
        arr = []
        ```
        Different variable name (`arr` vs `valid`) but same purpose as Methods 1 & 2.

        ### Line 277: Triple Iterator Pattern
        ```python
        for c, b, a in zip(codes, business_line, is_active):
        ```
        Same zip pattern but with SHORTENED variable names:
        - `c` = codes (more concise)
        - `b` = business_line (more concise)
        - `a` = is_active (more concise)

        ### Line 278: The Compound Validator - FUNCTIONAL COMPOSITION
        ```python
        if a and b in ("electronics", "grocery", "pharmacy", "restaurant") and goods(c):
        ```
        This is FUNCTIONAL COMPOSITION in action:
        Condition 1: `a` - Active status check
        Condition 2: `b in (...)` - Business type validation using TUPLE membership
        Condition 3: `goods(c)` - Character validation using our helper function

        WHY TUPLE INSTEAD OF DICTIONARY?
        - `("electronics", "grocery", "pharmacy", "restaurant")` - Tuple for membership testing
        - No need for priority values here since we're using alphabetical sorting
        - Tuple membership is O(n) but n=4 so effectively O(1)

        ### Line 279: Tuple Construction - DIFFERENT APPROACH
        ```python
        arr.append((b, c))
        ```
        KEY DIFFERENCE from Methods 1 & 2:
        - Stores `(business_line, coupon_code)` instead of `(priority_number, coupon_code)`
        - This means sorting will be ALPHABETICAL by business line, not by priority

        ### Line 280: Alphabetical Sorting
        ```python
        arr.sort(key=lambda x: (x[0], x[1]))
        ```
        - Sorts by business line name alphabetically, then by coupon code
        - "electronics" comes before "grocery" alphabetically
        - Different sort order than Methods 1 & 2!

        ### Line 281: List Comprehension Transform
        ```python
        return [c for _, c in arr]
        ```
        Same tuple unpacking pattern as other methods.

        ## Why This Approach is EXCELLENT for Complex Logic:
        1. **Modularity**: Validation logic is separated and reusable
        2. **Readability**: Helper function name makes intent clear
        3. **Maintainability**: Changes to validation rules only affect one function
        4. **Testability**: Helper function can be unit tested independently
        5. **Debugging**: Easier to step through and debug validation logic

        ## Performance Analysis:
        - Helper function call overhead: Minimal in Python
        - Character validation: Same O(k) as Method 1
        - Function call per coupon: Small constant overhead
        - Best for readable, maintainable code

        ## When to Use Method 3:
        - Complex validation logic that might change
        - When you need to unit test validation separately
        - When code readability is more important than micro-optimizations
        - When validation logic is used in multiple places
        - When working in a team where code clarity is crucial

        ## Key Difference in Output:
        Unlike Methods 1 & 2, this method sorts alphabetically by business line,
        not by the priority order (electronics, grocery, pharmacy, restaurant).
        """

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
                arr.append((b, c))  # This creates alphabetical sorting, not priority sorting
        # Same sorting algorithm but different data structure
        arr.sort(key=lambda x: (x[0], x[1]))  # Sorts by business name alphabetically
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
