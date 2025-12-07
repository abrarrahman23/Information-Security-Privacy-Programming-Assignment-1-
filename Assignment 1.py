def is_palindrome(s):
    """Check if a string is a palindrome (ignoring spaces and case)."""
    # Remove spaces and convert to lowercase
    cleaned = s.replace(" ", "").lower()
    # Compare with reversed string
    return cleaned == cleaned[::-1]

# Get user input
user_string = input("Enter a string to check if it's a palindrome: ")

if is_palindrome(user_string):
    print(f"'{user_string}' is a palindrome!")
else:
    print(f"'{user_string}' is not a palindrome.")