
def fizzBuzz(n):
    n = int(n)
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"  # Return instead of print
    if n % 3 == 0:
        return "Fizz"      # Return instead of print
    if n % 5 == 0:
        return "Buzz"      # Return instead of print
    return str(n)          # Return string version of n


# Test cases
print(fizzBuzz(15))  # Should print "FizzBuzz"
print(fizzBuzz(3))   # Should print "Fizz"
print(fizzBuzz(5))   # Should print "Buzz"
print(fizzBuzz(7))   # Should print "7"
print(fizzBuzz(30))  # Should print "FizzBuzz"
print(fizzBuzz(85))  # Should print "Buzz"

# Add debugging for hidden test cases
print("\nTesting hidden cases:")
for i in range(1, 100):  # Test cases 0-7
    print(f"Test case {i}: {fizzBuzz(i)}")
