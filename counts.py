def count_upper_case(message):
    count = 0
    for character in message:
        if character.isupper():
            count += 1
    return count

assert count_upper_case("") == 0, "Empty string should return 0"
assert count_upper_case("A") == 1, "Upper case 'A' should return 1"
assert count_upper_case("a") == 0, "Lower case 'a' should return 0"
assert count_upper_case("£$%%^") == 0, "Special characters should return 0"

print("All the tests passed")
