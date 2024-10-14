word = input()

letters = list(word)
reverse_letters = list(word[::-1])

alphabet = 'abcdefghijklmnopqrstuvwxyz'

letters = [letter for letter in letters if letter in alphabet]
#print(letters)
reverse_letters = [letter for letter in reverse_letters if letter in alphabet]
#print(reverse_letters)

if letters == reverse_letters:
    print(True)
else:
    print(False)
