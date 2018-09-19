def is_even(number):
    """
    A simple helper function that will check to see if a number is even or not

    `number` is the number that we wish to check

    Returns True or False depending on whether or not the number is evenly
    divisble by 2
    """
    return number % 2 == 0


def even_number_of_evens(numbers):
    """
    Returns the number of even numbers contained in a list of numbers.

    `numbers` should be a list containing numbers
    
    Returns either True or False based on a number of criteria.
        - if `numbers` is empty, return `False`
        - if the number of even numbers is odd, return `False`
        - if the number of even numbers is 0, return `False`
        - if the number of even numbers is even, return `True`
    """
        
    # Iterate of over each item and if it's an even number, increment the
    # `evens` variable
    evens = sum([1 for n in numbers if is_even(n)])
    return False if evens == 0 else is_even(evens)

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