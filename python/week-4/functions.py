def sum_digits(number):
    digits = [int(number) for number in str(number)]
    total = 0
    for digit in digits:
       total += digit
    return total

# print(sum_digits(1234))

def pairwise_digits(number_a, number_b):
    output = ""
    for index, digit in enumerate(str(number_a)):
        if digit == str(number_b)[index]:
            output += "1"
        else:
            output += "0"
    return output
    

# print(pairwise_digits(1234, 1255))

def to_base_10(number, base):
    digits = [int(number) for number in str(number)]
    total = 0
    for index, digit in enumerate(digits):
        total += digit * (base ** index)
    return total

# print(to_base_10(1010, 2))


def binary_triangle(height):
    count = 0
    current_row = 1
    for row in range(height):
        output = ""
        for i in range(current_row):
            if count % 2 == 0:
                output = output + "1"
                count += 1
            else:
                output = output + "0"
                count += 1
        print(output)
        current_row += 1

binary_triangle(5)

