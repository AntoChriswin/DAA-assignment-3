def kidsWithCandies(candies, extraCandies):
    max_candies = max(candies)
    result = [(candy + extraCandies) >= max_candies for candy in candies]
    return result

# Example Usage
candies1 = [2, 3, 5, 1, 3]
extraCandies1 = 3
print(kidsWithCandies(candies1, extraCandies1))  # Output: [True, True, True, False, True]

candies2 = [4, 2, 1, 1, 2]
extraCandies2 = 1
print(kidsWithCandies(candies2, extraCandies2))  # Output: [True, False, False, False, False]

candies3 = [12, 1, 12]
extraCandies3 = 10
print(kidsWithCandies(candies3, extraCandies3))  # Output: [True, False, True]
