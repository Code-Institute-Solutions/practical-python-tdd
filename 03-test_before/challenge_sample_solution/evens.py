"""
Solution to the challenge in the `Test Before` unit found in the `Test Driven
Development with Python lesson`

NOTE: The solution found in this file is one of the many potential solutions
that can be used to achieve the end result expected by the challenge in the
lesson.
"""


def is_even(number):
    """
    A small helper function that simply checks to see if the number 
    question is an even number, or an odd number.

    `number` is the number in question

    Returns `True` if the number is even, `False` if the number is odd
    """
    if number % 2 == 0:
        return True
    else:
        return False


def even_number_of_evens(numbers):
    """
    Returns the number of even numbers contained in a list of numbers.

    `numbers` should be a list containing numbers
    
    Returns either True or False based on a number of criteria.
        - if the length of the list is greater than 0, iterate over each item
            to find out how many even numbers are in the list, and if the
            number of even numbers is an even number, return `True`
        - if the total number of even numbers in the list of 0, return `False`
        - if the number of even numbers contained in the list is an odd
            number, return `False`
        - if the list contains no items, return `False`
    """

    # Check to see if the list is empty. If it is, return `False`, else start
    # the iterative process
    if numbers == []:
        return False
    else:
        # Set a `number_of_evens` variable that will be incremented each time
        # an even number is found
        number_of_evens = 0
        for number in numbers:
            if is_even(number):
                number_of_evens += 1
        
        # If no even numbers are found, return `False`
        if number_of_evens == 0:
            return False
        
        # If the number of even numbers found, is even, return `True`,
        # else return `False`
        if is_even(number_of_evens):
            return True
        else:
            return False

# Our set of test cases
assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four even"
assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"

# If all the test cases pass, print some successful info to the console to let
# the developer know
print("All tests passed!")