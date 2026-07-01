"""
if backtracking is try everything, dynaic programming is ' remember what you have tried so you naver have do it again'
we are moving from exhaustice search to the overlapping subproblems,
"""

"""
the prblem -
you are climbing a staircase. it takes n steps to reach the top . each time you can either climb 1 or  2 steps. in how many distinct ways can you climb to teh top?
ex i/p: n = 3
o/p: 3(1+1+1, 1+2, 2+1)
"""

# the memorization strategy- 
# a recursive solution would compute the same sub-steps thousands of time for n =5, to compute the steps fo r5 , tou 4 and 3. to compute the steps for 4 you need 3 and 2. Notice that 3 is calculated twice . as n grows , this becomes exponential .
#  by memorization (a dictionary or array to store results of function calls , we ensure that each stair index is computed exactly once.)
# breaking down the final decisio to reach the top. how could you possible land at any nth step. there are exactly two disjoint entry points , you take step 1 step jump form n-1 you take two step jup from n-2
# therefore the total no. of ways to reach at the step (n-1) + ways (n-2)
# ways(n) = ways(n-1) + ways(n-2)


def climb_stairs(n: int) -> int:
    """
    Calculates the number of distinct ways to climb stairs using memorizarion.
    Time complexity : O(n) - Each stair is compted once.
    Space complexity : O(n) - the sictianry and recursion stack depth sclae with n
    """
    # Memorization table to store results of subproblem
    memo = {}
    def _dp(i: int) ->int:
        #Base cases
        if i==n: return 1   # Reached the top 
        if i > n: return 0  # Overshot the top

        # Check if already computed
        if i in memo:
            return memo[i]

        # Recusion relation: ways to reach reach top = ways(step +1) + ways(step + 2)
        memo[i] = _dp(i+1) + _dp(i + 2)
        return memo[i]
    
    return _dp(0)

if __name__ == "__main__":
    n = 3
    ways = climb_stairs(n)
    print(f"Total distinct ways to climb {n} stairs: {ways}")
    