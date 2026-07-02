"""
The problem : 
Given an integer array nums, return True id you can partition the array into two subset such that the sum of the elements in both subsets is equal. Otherwise, return False
example input : [1,5,11,5]
example output : True (subset 1 [1,5,5], subset 2: [11])
to solve this we first calculate total_sum. if it is odd, we can never split into two equal parts, , return false , immediately
if if it is even our target is sum/2
we create boolean array dp of size target +1, where dp[i] tells us if sum of i is possible with the numbers processed so far.
initialize , dp[0] = True (a sum of 0 is always possible withan empty set).
iterate: for each numbers, in nums , we update our dp table.
The reverse loop: we must iterate through the dp table backwards (from target down to num). Why? Because if we went backwards , we might use the same number multiple times in one sum, whic violate the '0/0' (use it or lose it) contraint
"""

def can_partition(nums: list[int]) -> bool:
    """
    determines if an array can be partitioned into 2 subsets with equal sum
    Time complexity: O(n*target)
    space complexity: O(targert)
    """
    total_sum = sum(nums)

    #if odd, return false
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    # dp[i] will return True is sum[i] is achievable.
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        #Reverse loop prevents using the same elements multiple times
        for i in range(target, num -1, -1):
            if dp[i-num]:
                dp[i] = True

    return dp[target]

if __name__ == "__main__":
    nums = [1,5,11,5]
    print(f"can partition {nums} ? {can_partition(nums)}") # expected True

