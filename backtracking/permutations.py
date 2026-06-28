def permute(nums: list[int]) -> list[list[int]]:
    """
    Generates all unique linear permutation of distinct integer array using global state tracking.
    Time Complexity : O(n*n!) - there are n! variations, and copying each take o(n) time
    Space Complexity : O(n) - The depth if the recursion stack and the visited tracking array scale with n.
    """

    res = []
    path = []

    #track which physical indices are locked in the current vertical path.
    visited = [False] * len(nums)

    def _backtrack() -> None:
        # Base Case: Every available number has been positioned in the current permutaion layout.
        if len(path) == len(nums):
            res.append(path.copy())
            return 
        
        # scan the entire array from the base index 0 on every step to evaluate all options
        for i in range(len(nums)):
            # if the elements at this index is already present in our path, skip it
            if visited[i]:
                continue

            #1. Choose: Lock the element index and add the value to our path
            visited[i] = True
            path.append(nums[i])

            #2. Explore: 
            _backtrack()
            
            #2. Un-choose: (Backtrack cleanup) - Unlock the index state for alternative branches
            path.pop()
            visited[i] = False

    _backtrack()
    return res

if __name__ == "__main__":
    input_array = [1, 2, 3]
    all_permutations = permute(input_array)
    
    print(f"Total Generated Permutations ({len(all_permutations)} configurations):")
    print(all_permutations)