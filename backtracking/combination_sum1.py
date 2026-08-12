# The Problem: 
# Given an array of distinct integers candidates and a target intger target, retutn a list of all unique combinatins of candidates where the chsen numbers summ to target. you may retutrn the combination in any order.
# The same numbers may be chosen from the candidates an unlimited number of times. two combinations are unique if the frequency of atleast one chosen number is different

# the logic : 
# unlike the subsets problem where tou always move forward to index i+1, combination sum allows you to reuse the same number


def combinationSum(candidates: list[int], target : int) -> list[list[int]]:
    result = []

    def backtrack(i: int, current : list[int], total : int):
        # base case : if the total is the target
        if total == target:
            result.append(current.copy())
            return 
        
        # base case : if the total exceeds the target or if we have considered all the targets
        if total > target or i >= len(candidates):
            return
        
        # decision 1 : include candidatees[i] and recurse, 
        current.append(candidates[i])
        backtrack(i, current, total + candidates[i])

        # decision 2 : exclude candidates[i] and move to the next index
        current.pop()
        backtrack(i+1, current, total)

    backtrack(0, [], 0)
    return result


if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target_val = 7
    
    result = combinationSum(candidates, target_val)
    print(f"Combinations summing to {target_val}: {result}")
    
    assert [2, 2, 3] in result and [7] in result, "Test Failed"
    print("Success: Combination Sum backtracking verified.")