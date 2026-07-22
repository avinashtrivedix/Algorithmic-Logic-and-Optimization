# you are give na sorted array of integers and a target sum. you need to find the need to ifnd the indices whose values add up to the target.



def two_sum_sorted(numbers : list[int], target: int) -> list[int]:
    left = 0
    right = len(numbers) - 1

    while left< right:
        current_sum = numbers[left] + numbers[right]
        if current_sum  == target:
            return [left + 1, right + 1]
        if current_sum < target:
            left += 1
        else:
            right -= 1

    return []


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target_val = 9
    result = two_sum_sorted(nums, target_val)
    print(f"Indices found: {result}")
    
    assert result == [1, 2], "Test Failed"
    print("Success: Sorted Two-Pointer verified.")