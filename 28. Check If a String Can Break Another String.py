def canBreak(s1: str, s2: str) -> bool:
    # Sort both strings
    s1_sorted = sorted(s1)
    s2_sorted = sorted(s2)

    # Check if s1 can break s2
    s1_breaks_s2 = all(c1 >= c2 for c1, c2 in zip(s1_sorted, s2_sorted))
    # Check if s2 can break s1
    s2_breaks_s1 = all(c2 >= c1 for c1, c2 in zip(s1_sorted, s2_sorted))

    # Return true if either condition is satisfied
    return s1_breaks_s2 or s2_breaks_s1


# Example Usage
print(canBreak("abc", "xya"))  # Output: True
print(canBreak("abe", "acd"))  # Output: False
print(canBreak("leetcodee", "interview"))  # Output: True
