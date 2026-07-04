# the text_1 and text_2 is never going to be the same legth. but LCS do not care about the full strings. It only cares about the shared sequence that exists inside both.
# think of it as 2 people reading 2 diff book, and you want the longest list of word to be the same order. even there are 100 other words in between.
# then how do they actually match. 
# we have a grid text 1 in rows and text 2 in columns. 
# if text1[i] == text[j], 

def longest_common_subsequence(text1: str, text2: str) -> int:
    """
    computes the length of the longest common subsequence string
    time complexity : O(m*n)
    space complexity : O(m*n)
    """

    m,n = len(text1) , len(text2)
    #initialize the grid with )s, size is (m+1) x (n+1) to handle handel the empty base case.
    dp = [[0] * (n+1) for _ in range (m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                #No match, take the best path from top or left.
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]

if __name__ == "__main__":
    t1, t2 = "abcde", "ace"
    print(f"LCS length of {t1} and {t2}: {longest_common_subsequence(t1, t2)}") # Expected: 3