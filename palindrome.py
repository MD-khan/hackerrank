from operator import ne


def is_palindrome(input_string):
    # We'll create two strings, to compare them
    new_string = input_string.replace(" ", "").lower()

    if new_string == new_string[::-1]: # reversig the string
        return True  
    else:
        return False

print(is_palindrome("Never Odd or Even"))  # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True
