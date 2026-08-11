# The choice Tree - 
# Given an integer array nums of unique elments, return all possible subsets (the power set). The solution must contianduplicate subsets. the solution set must not contain duplicate subsets. return the solution in any order.
# The Logic: Backtracking is essentiall a depth first search through a decision tree where you make a choice, explore adown that path, and then undo your choice (backtrack)to try the next option. For subsets, at every index of the array. You have two decision for every element:
# Incled teh current number in you wrokinf subset and recurse forward.
# Backtrack (remove the number) and exclude it, moving on to the next branch of choices.

def subsets(nums: list[int]) -> list[list[int]]:
    result = []
    current_subset = []

    def backtrack(i : int):
        # Base case: when we considered every number in nums
        if i >= len(nums):
            result.append(current_subset.copy())
            return
        
        #decision 1: include nums[i]
        current_subset.append(nums[i])
        backtrack(i+1)

        #decision 2: exclude nums[i] (backtrack by popping it off)
        current_subset.pop()
        backtrack(i+1)

    backtrack(0)
    return result

if __name__ == "__main__":
    nums = [1,2,3]
    result = subsets(nums)
    print(f"All generated subsets: {result}")

    # Check that we generated all 8 possible subsets(2^3)

    assert len(result) == 8, "Test Failed"
    print("Sccess : Subsets Backtrackinf verified.")