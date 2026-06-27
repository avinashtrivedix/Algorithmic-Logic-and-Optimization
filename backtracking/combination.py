# the structural reason behind the copy rule :  IN Python, lists are mutable object passed by reference. If you write res.append(path), 
# you are not saving the element in the list. you are saving the pointers to the the single path memory location. 
# beacsue the backtracking loop continually append and pops element from the exact same list, 
# your final res array would just end up containing 8 references to a completely empty list. 
# writing .copy() takes an isolated snapshot of the values at that exact split second.

# given an array of distincet(candidates) and a target integer  (target), return a list of all unique 
# unique combinations of candidates where the chosen numbers sum to target. you may return the combination in any order.
# to avoid generating suplicate combinations , we pass tracking index down our recusion line. 
# the algorithm is only allowed to choose numbers at or after the start index.

def combination_sum(candidates: list[int], target: int) ->list[list[int]]:
    #find all the unique combinations that sum up to a target value using nd unbounded decision loop.
    #time comlexity : O(2^target) - in the worst case, the tree depth scales with the target size.
    #space complexity : O(target) - recusion stack frames are bounded by target depth limit.
    
    res = []
    path = []
    def _backtrack(start: int, current_target : int) -> None:
        #Base case :1: Target reached exactly
        if current_target == 0:
            res.append(path.copy())
            return
        
        #base case :2: oveshot the the target, prune the remaining branch path
        if current_target < 0:
            return
        
        # loop through remaining choices starting at our current indext boundary
        for i in range(start, len(candidates)):
            #1. Choose
            path.append(candidates[i])

            #2. explore (pass "i" istead of "i+1" to allow unlimited reuse)
            _backtrack(i, current_target - candidates[i])

            #3. Un-choose (backtrack cleanup)
            path.pop()

    _backtrack(0, target)
    return res

if __name__ == "__main__":
    nums = [2,3,6,7]
    target_val = 7

    valid_combinations = combination_sum(nums, target_val)
    print(f"Unique Combinations that sum up to {target_val}:")
    print(valid_combinations)