# backtracking is the systematic brute-force algorithmic framework used for solvig optimization, search and combinatorial problem. think of it as a controlled dfs explorer, walking through a maze of decision
"""
the core concept
in a backtracking problem , you build a solution step-by-step. at each step, you face a fork in the road.(multiple choice)
choose : you pick one path and walk down it recursively
explore :  you check if this path leads to the valid solution.
un-choose : (backtrack) : if you hit a dead - end, or if you finish recording a valid oath yu physically a step backwad udo the last choiuse m andn try the next available choice at that fork

the absolute rule of backtracking is :  cleap up your mess 
if you add number to your tracking list wehn the resursion return so the next branch starts with clean slate. """

# the problem - given an integer array nums of unique elements, return all possible subsets (the power set). the solution set must not contain duplicate subsets. you my return the solution in any order.

#1. the base case - if i pointer reaches the end of an arau i == len(nums) , you have made a decision for every single number, append a copy of your current tracking pathh to you final results list and return.
#2. the left branch (Include): Add num[i] to you path list, then recursively call your helper function for undex i+1
#3. the backtre reset:  pop nums[i] out of your path to rese the state
#4. the right branch - excude: call you helper function for index i+1 with the empty state.


def subsets(nums : list[int]) -> list[list[int]]:
    """
    generates the complete power set of binary decesion tree.
    Time complexity : O(n*2^n) : there are 2^n subsets and copying each takes O(n)
    Space Complexiy : O(n) - The recursion stack frames are are bounded by array length n
    """

    res = []
    path  = []

    def _backtrack (i: int) -> None:
        # basecase : if the index reaches the end, record the subset snapshot.
        if  i == len(nums): 
            res.append(path.copy())
            return
        
        #Choise 1: Include the element in the current index.
        path.append(nums[i])
        _backtrack(i+1)

        # the backtrack strp: undo the inclusion step to clean up our state.
        path.pop()

        #choise 2 : Exclude the element at the current index and move forward
        _backtrack(i+1)

    _backtrack(0)
    return res


if __name__ == "__main__" :
    input_set = [1,2,3]
    output_power_set = subsets(input_set)

    print(f"Generated power set (Total Subsets : {len(output_power_set)}): ")
    print(output_power_set)