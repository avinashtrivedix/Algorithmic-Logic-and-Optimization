# the problem -  you are now, given an interger array nums where each element represents your maximum jump length at that position. determine if you are able to reach the index starting from the first index. 
# instead of using dp , to trach evvery possible path, we track the furthest reachable index. As iterate through  the array if our current index is ever greater than our max_reachability , it means we are stuck and can proceed  
# nums[i] is the capacity, this is your fuel, it is not a coordinate. it is distance you are allowd to add to your position . 


def can_jump(nums: list[int]) -> bool:
    """
    Determines if the last index is reachable using a greedy pointer.
    Time complexity : O(n) 
    Space Complexity : O(1)
    """

    goal = len(nums) - 1

    # Iterate backwards from the socond to the last index.
    for i in range(len(nums) -2 , -1 , -1):
        # if this index can reach teh current goal, move the goal closer.
        if i + nums[i] >= goal:
            goal = i
    return goal == 0

if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    print(f"Can reach the end of {nums}? {can_jump(nums)}") # Expected: True