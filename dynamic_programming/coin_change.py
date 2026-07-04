#you have given an integer arrau (coins) representing coins of different denomination and an integer amount representing the total amount of money, return the fewest no. of coinsa that tou need to make up that amount. if that amouint of mpney canot be made up by any combanation ofo the coins return -1.

def coin_change(coins : list[int], amount: int) -> int:
    """
    Finds the minimum of coins required to make upa given amount.
    time complexity: O(N * amount)
    space complexity: O(amount)
    """

    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    #fill up the dp table
    for a in range(1, amount +1):
        for coin in coins:
            if a - coin >= 0:
                # the minimum is either the current value or 1 coin + the result for the remainder.
                dp[a] = min(dp[a], 1 + dp[a-coin])

    return dp[amount] if dp[amount] != amount + 1 else -1

if __name__ == "__main__":
    test_coins = [1, 2, 5]
    test_amount = 11
    print(f"Min coins for {test_amount}: {coin_change(test_coins, test_amount)}") # Expected: 3if __name__ == "__main__":