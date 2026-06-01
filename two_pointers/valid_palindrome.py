#by building a new string
def valid_palindrome(s: str) -> bool:
    new_string = ""
    for char in s:
        if char.isalnum():
            new_string += char.lower()
    return new_string == new_string[::-1]

# two pointer solution
def valid_palindrome_two_pointers(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left +=1
        right -= 1
    return True