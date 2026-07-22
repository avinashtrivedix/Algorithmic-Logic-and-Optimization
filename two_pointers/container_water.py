# container with most water. you are given an array of heights representing vertical lines. find two lines that together that together with the x -axis form a container, such that the container contains the most water. 
# the Logic : A brute force check of evry pair takes O(N^2) time, 
# use the lwft pointer at index 0 and right poiter at the end of the arra
# takes O(N) time

# the toolbox - Greedy Convergencce - 
# the area -  the width and height - 
# = (right - left) * min(height[left] , height[right])


def max_area(height: list[int]) -> int:
    left= 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        # calculate the current water area
        width = right - left
        current_height = min(height[left], height[right])
        current_water = width * current_height

        max_water = max(current_water, max_water)

        # move the pointer with the smaller wall inward
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water

if __name__ == "__main__":
    # Test Case: Heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    # Expected maximum area: 49 (between index 1 (height 8) and index 8 (height 7), width = 7)
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result = max_area(heights)
    print(f"Maximum Water Area: {result}")
    
    assert result == 49, "Test Failed"
    print("Success: Two-Pointer Pincer verified.")

        