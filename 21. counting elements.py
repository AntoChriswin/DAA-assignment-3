def count_elements(arr):
    element_set = set(arr)
    count = 0

    for x in arr:
        if x + 1 in element_set:
            count += 1

    return count



print(count_elements([1, 2, 3]))  # Output: 2
print(count_elements([1, 1, 3, 3, 5, 5, 7, 7]))  # Output: 0
