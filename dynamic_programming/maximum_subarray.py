# Kadane's Algorithm - 
# this algoritihm is used to find the maximum sum of a contiguous subarray in an array of intgers.
# contiguous means the elements that are adjacent/alligned to each other.


def max_subarray(nums: list[int]) -> int:
    """
    finds the mmaximum sum of a contiguous subarray using kadane's Algorithm.
    Time complexity : O(n) - we proces every single in the array once.
    Space Complexity : O(1) - we only onr the we only need to track the current sum and the maximum sum so far.
    """

    # initialize with the first element with current sum and max sum
    current_max = global_max = nums[0]

    for num in nums[1:]:
        # decision: start fresh or extend the current subarray?
        current_max = max(num, current_max +num)
        #update the global best
        global_max = max(global_max, current_max)

    return global_max

if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Max subarray sum: {max_subarray(nums)}") # Expected: 6