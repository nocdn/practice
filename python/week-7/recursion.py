def countdown(n):
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n-1)

# countdown(3)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
# print(factorial(5))

def recursive_is_palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    else:
        return recursive_is_palindrome(word[1:-1])
    
# print(recursive_is_palindrome("racecar"))