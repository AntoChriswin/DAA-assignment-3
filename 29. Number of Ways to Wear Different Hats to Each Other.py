def numberWays(hats):
    MOD = 10 ** 9 + 7
    n = len(hats)

    # Preprocess to get which hats each person likes
    from collections import defaultdict
    hat_to_people = defaultdict(list)
    for person, hat_list in enumerate(hats):
        for hat in hat_list:
            hat_to_people[hat].append(person)

    # Dynamic programming with bitmask
    dp = [0] * (1 << n)
    dp[0] = 1

    # Iterate over each hat from 1 to 40
    for hat in range(1, 41):
        if hat in hat_to_people:
            # Update dp array in reverse order to avoid overwriting states in the same iteration
            for mask in range((1 << n) - 1, -1, -1):
                for person in hat_to_people[hat]:
                    if mask & (1 << person) == 0:
                        dp[mask | (1 << person)] = (dp[mask | (1 << person)] + dp[mask]) % MOD

    return dp[(1 << n) - 1]


# Example Usage
print(numberWays([[3, 4], [4, 5], [5]]))  # Output: 1
print(numberWays([[3, 5, 1], [3, 5]]))  # Output: 4
print(numberWays([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]))  # Output: 24
