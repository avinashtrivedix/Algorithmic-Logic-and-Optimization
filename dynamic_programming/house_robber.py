#the problem
# given an integer array nums representing the amount of money in each house, return the maximum amount you can rob without triggering an alarm(no two adjacent houses.)
# the tabulation stratregy O(n) time  and O(n) space
def rob(nums: list[int]) -> int:
    """
    determine the maximum amount of money that can be robbed without alerting the police
    time compplexity : O(n) -  we process each house once.
    Space complexity: O(n) - we store the maximum loot for each house in a dp array.
    """
    if not nums: return 0
    if len(nums) == 1: return nums[0]

    # initialize the dp table
    dp = [0] * len(nums)

    # set the base cases
    dp[0]  = nums[0]
    dp[1] = max(nums[0], nums[1])

    # fill the dp table based on the previous 2 decisions
    for i in range(2, len(nums)): 
        # you are standing at house i, and you have exactly 2 choises to make ,, your dp table is just a record of the best choise made at every single house.
        # choise 1: skip this house:  if you fi you decide to skip thisd your totla loot remains ecactly the same as your previouse house 
        # choise 2: rob this house 1 , so yoou look at the loot you had accunulated at the house two doors back (i-2) and add the money from the current house (nums[1]) to it.
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        

    return dp[-1]


if __name__ == "__main__":
    houses  = [2,7,9,3,1]
    print(f"maximum loot from {houses} is: {rob(houses)}") # expected 12


