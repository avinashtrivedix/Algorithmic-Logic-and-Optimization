# the Toolbox - 
# the pointeers - left and right
# the tracker - set ot dictionary, to keep track of the characters inside our active window.
# the golden rule about the pointers - POinters are always indices never character, because we wanna perform arithmetic operation in them

def longest_substring(s: str) -> int:
    left = 0
    tracker = set()
    max_length = 0

    for right in range(len(s)):
        # If we see a duplicate shirink th ewindow from the left
        while s[right] in tracker:
            tracker.remove(s[left])
            left += 1

        #Add the newe character to our window
        tracker.add(s[right])
        # Update the max length found so far
        max_length = max(max_length, right-left+1)

    return max_length

if __name__ == "__main__":
    test_str = "abcabcbb"
    result = longest_substring(test_str)
    print(f"Longest substring length: {result}")
    assert result == 3, "Test Failed"
    print("Success: Sliding Window verified.")