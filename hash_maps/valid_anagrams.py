# given two strings s & t, return true if they are anagrams of each other, and false otherwise.an anagaram is the same word but with the letters rearranged. for example, "listen" and "silent" are anagrams of each other, but "hello" and "world" are not.

def is_anagram(s: str, t: str) -> bool:
    #if lengths are different, they can't be anagrams
    if len(s) != len(t):
        return False
    if sorted(s) == sorted(t):
        return True
    return False
# the time compleplexity of this solution is O(n log n) because of the sorting step, where n is the length of the strings. space complexity is O(1) if we ignore the space used by the sorting algorithms, or O(n) if we consider the space used by the sorting algorithms.


# counter solution
from collections import Counter
def is_anagram_counter(s: str, t: str) ->bool:
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)


# the hashmap solution
def is_anagram_hashmap(s: str, t: str) ->bool:
    if len(s) != len(t):
        return False
    char_count = {}
    #build the tally from "s"
    for char in s:
        char_count[char] = char_count.get(char, 0)+1
    # buils the tally from "t"
    for char in t:
        char_count[char] = char_count.get(char, 0)-1
    # audit the final result
    for count in char_count.values():
        if count != 0:
            return False
    return True



