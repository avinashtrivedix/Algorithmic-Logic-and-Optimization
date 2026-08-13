# Given an array nums of distinct integers, return all the possible permutaions.
# you can return the answer in any order.
# Unlike subsets where order does'nt matter, permutaiotns care about every unique arrangement. Instead of maintaininga a separate tracking, we can generate in place bt swapping elements.
# define a recursive backtracking function that takes start index.
# iterate through  indext choices from start to teh end if the array.
# swap the element at the start index with the element at the current loop index i.
# Recursively call the backtracking for start+1.


def permute(nums : list[int]) -> list[list[int]]:
    result = []

    def backtrack(start : int):
        # Base case: if we have considered number in nums, if start index reaches the end.
        if start == len(nums):
            result.append(nums.copy())
            return
        
        for i in range(start, len(nums)):
            # make the choice  :  swap teh current index with the start index.
            nums[start], nums[i] = nums[i], nums[start]

            # Explore further down the decision tree.
            backtrack(start + 1)

            # Undo the choice (Backtrack) : swap back to restore the original order.
            nums[start], nums[i] = nums[i], nums[start]

    backtrack(0)
    return result
    
if __name__ == "__main__":
    nums = [1, 2, 3]
    result = permute(nums)
    print(f"All generated permutations: {result}")
    
    # Check that we generated all 6 possible permutations (3! = 6)
    assert len(result) == 6, "Test Failed"
    print("Success: Permutations backtracking verified.")



