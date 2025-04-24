import aoc_day2

# Test file for aoc day2
def test_results():
    """Test the results of the file."""
    assert aoc_day2.main() == (2, 0)  # Test case 1
    assert aoc_day2.main() == (3, 1)  # Test case 2 with unique expected result
    assert aoc_day2.main() == (4, 2)  # Test case 3 with unique expected result
    assert aoc_day2.main() == (5, 3)  # Test case 4 with unique expected result
# Explain assert
    assert aoc_day2.main()