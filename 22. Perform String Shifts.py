def perform_string_shifts(s, shift):
    total_shift = 0

    # Calculate net shift amount
    for direction, amount in shift:
        if direction == 0:
            total_shift -= amount  # left shift
        else:
            total_shift += amount  # right shift

    # Normalize the shift amount
    n = len(s)
    total_shift %= n  # To avoid unnecessary full rotations

    # Apply the net shift
    if total_shift == 0:
        return s
    elif total_shift > 0:
        return s[-total_shift:] + s[:-total_shift]
    else:
        return s[-total_shift:] + s[:n + total_shift]


# Test examples
print(perform_string_shifts("abc", [[0, 1], [1, 2]]))  # Output: "cab"
print(perform_string_shifts("abcdefg", [[1, 1], [1, 1], [0, 2], [1, 3]]))  # Output: "efgabcd"
