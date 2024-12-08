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

def sum_digits(number):
    if len(number) <= 1:
        return number
    # to implement


def merge_lists(list1, list2):
    final_list = []
    for item in list1:
        final_list.append(item)
    for item in list2:
        final_list.append(item)
    final_list.sort()
    return final_list

print(merge_lists([4, 7, 1, 8, 9], [5, 5, 9, 1, 3, 1, 6, 4]))