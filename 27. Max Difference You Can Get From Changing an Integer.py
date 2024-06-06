def maxDiff(num):
    str_num = str(num)

    # Step 1: Find the maximum possible value
    max_num = list(str_num)
    for i in range(len(max_num)):
        if max_num[i] != '9':
            max_digit = max_num[i]
            break
    for i in range(len(max_num)):
        if max_num[i] == max_digit:
            max_num[i] = '9'
    max_num = int("".join(max_num))

    # Step 2: Find the minimum possible value
    min_num = list(str_num)
    if min_num[0] != '1':
        min_digit = min_num[0]
        for i in range(len(min_num)):
            if min_num[i] == min_digit:
                min_num[i] = '1'
    else:
        for i in range(1, len(min_num)):
            if min_num[i] != '0' and min_num[i] != '1':
                min_digit = min_num[i]
                break
        for i in range(1, len(min_num)):
            if min_num[i] == min_digit:
                min_num[i] = '0'
    min_num = int("".join(min_num))

    # Step 3: Calculate the difference
    return max_num - min_num


# Example usage
print(maxDiff(555))  # Output: 888

