#given a string s, return the longest palindrome substring in s.
# example i/p - "babad" ; o/p - "bab" or "aba"
# this problem shifts the dp focus from comparing 2 different strings
# to analyzing the structure within a single string.
#palindrome reads the same forward and same backward.
# to find one, we observe that a string s[i:j] is a palindrome if s[i] == s[j] AND the inner substrind s[i+1 : j-1] is also a palindrome.

def longest_palindrome(s:str) -> str:
    """
    Finds the longest palindrome substring using DP gap-fillling tabulation.
    gap filling tabulation strategy
    Time Complexity: O(n^2)
    Space COmplexity: O(n^2)
    """
    n = len(s)
    if n<2: return s

    # dp[i][j] will be true is s[i..j] is a palindrome.
    # do we always create a list of Falses? Not always,but yes, 
    # we essentially building a map of "known truths"
    # in DP, the DP table is your "Knowledge base." 
    # when we initialize a list of False value, 
    # we are saying: "I assume of these are palindrome yet. 
    # I will only mark them as True if I can prove they are"
    dp = [[False] * n for  _ in range(n)]
    start, max_len = 0,1
    for i in range(n):
        dp[i][i] = True

    # Check for substring of len 2 to n 
    # way of picking the sliding window of a specific size and moving it along the string.
    for length in range(2, n+1): # first check all the string of length n and then all the string of length 3  and all the way up to length n. 
        for i in range(n-length +1): # Move the left edge i of your window. 
            j = i + length - 1 # this is the mathematical anchor for right edge (j)

            # palindrome condition: ends must match and the middle must be a palindrome
            if s[i] == s[j]:
                if length == 2 or dp[i+1][j-1]:
                    dp[i][j] = True
                    if length  > max_len:
                        start, max_len = i, length

    return s[start: start + max_len]

if __name__ == "__main__":
    test_str = "babad"
    print(f"Longest palindrome of {test_str}: {longest_palindrome(test_str)}") # expected : "bab" or "aba"