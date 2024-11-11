input_array = [-1, 1, 2, 4, 8]
target = 7


def find_sum(array):
    for first_number in array:
        for second_number in array:
            if first_number + second_number == target:
                return [first_number, second_number]
            else:
                continue

def find_sum_efficient(array):
    for item in array:
        if (target - item) in array:
            return [item, (target - item)]

# print(find_sum(input_array))
# print(find_sum_efficient(input_array))

def merge_lists(array1, array2):
    merged_list = []
    i = 0
    j = 0

    while i < len(array1) and j < len (array2):
        if array1[i] < array2[j]:
            merged_list.append(array1[i])
            i += 1
        else:
            merged_list.append(array2[j])
            j += 1

    while i < len(array1):
        merged_list.append(array1[i])
        i += 1
    
    while j < len(array2):
        merged_list.append(array2[j])
        j += 1

    return merged_list

print(merge_lists([1, 3, 4, 7], [2, 3, 5]))
