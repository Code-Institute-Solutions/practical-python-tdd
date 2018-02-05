def is_even(number):
    return number % 2 == 0


def even_number_of_evens(numbers):
    evens_count = 0
    for num in numbers:
        if is_even(num):
            evens_count += 1
    return is_even(evens_count)


assert even_number_of_evens([]), "An empty list has zero evens (even)"
assert not even_number_of_evens([1, 2]), "One even number (odd)"
assert even_number_of_evens([1, 2, 4]), "Two even numbers (even)"
assert not even_number_of_evens([1, 2, 4, 6, 7]), "Three even numbers (odd)"
assert even_number_of_evens([1, 3, 9]), "No even numbers (even)"

print("All tests passed!")
