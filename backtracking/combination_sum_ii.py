"""
fid the combination that add upto the target sum, we cannot reuse the elements in this problem.
the input array also contains the duplicate elements, to make sure that we dont use those those 
duplicate elements, we can not use those, 
we have to sort those elements, first, 
and the apply sibbling skipping rule: the skipping condition inside the exploration loop, if the the current element is idential to the previous element (candidate[i] == candidate[i-1])
and and we are not at the very first step of our current loop. (i > start), we skip it completely using the continue 


vertically mean going deeper into a single chain of decisions down a branch."""

def combination_sum_ii(candidates: list[int], target: int)-> list[list[int]]:
    """
    Finds unique combinations with single useu items and duplicate input using sibling pruning
    Time COmplexity: O(2^n) - In the worst case, every elemen is explore and skipped.
    Space Complexity: O(n) - the recursion stack matches the length of thie candidate array"""

    candidates.sort()
    res = []
    path = []

    def _backtrack(start: int, current_target: int)-> None:
        if current_target == 0:
            res.append(path.copy())
            return
        if current_target < 0:
            return
        
        for i in range(start, len(candidates)):
            # sibling skip : skip duplicate numbers horizontally across the same loop level
            if i > start and candidates[i] == candidates[i-1]:
                continue

            #choose
            path.append(candidates[i])

            #explore
            _backtrack(i+1, current_target - candidates[i])

            # un - choose (Backtrack cleanunp)
            path.pop()
    _backtrack(0, target)
    return res

if __name__ == "__main__":
    test_candidates = [2,5,2,1,2]
    test_target = 5

    output = combination_sum_ii(test_candidates, test_target)
    print(f"Unique Combinations (No Reuse) for Target {test_target}:")
    print(output)  # Expected: [[1, 2, 2], [5]]