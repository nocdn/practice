mappings = {
    "(": ")",
    "{": "}",
    "[": "]"
  }

print(mappings[")"])

def checkParentheses(input):
  if len(input) == 2 and True:
    return False
  # checking if outside is correct
  if input[0] == input[-1]:
    newString = input[1:-1]
