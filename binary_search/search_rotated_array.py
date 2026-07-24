# the logic: A normal binary search expects fully sorted array. here, the array has a break point(the pivot). however , if you devide the rotate sorted array in half, at least one of the two halves will always br strictly sorted.
# find the middle index
# check if it is the target value, if not then 


def search(nums: list[int], target : int) -> int:
    left = 0
    right = len(nums)-1

    while left <= right:
        mid = (left + right)//2

        if nums[mid] == target:
            return mid
        
        #check if the left half is sorted
        if nums[left] <= nums[mid]:
            #check if the target lies in the sorted half left
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left= mid+1
        # otherwise, the right half must be sorted
        else:
            #target lies within right half soted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid-1

    return -1

if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    target_value = 0
    result = search(nums, target_value)
    print(f"target found at index: {result}")

    assert result == 4, "Test Failed"
    print("success: Rotated Binary Search verified")