def is_even(number):
    return number % 2 == 0

def even_number_of_evens(numbers):
    
    evens = sum([1 for n in numbers if is_even(n)])
    return False if evens == 0 else is_even(evens)
        
assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([1,3,9]) == False, "Three odd numbers"

print("All tests passed!")