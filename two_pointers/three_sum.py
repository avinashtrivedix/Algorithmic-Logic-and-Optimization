def three_sum(nums: list[int]) -> list[list[int]]:
    res = []
    nums.sort() # sorting is mandatory for two pointer sweep
    for i in range(len(nums) - 2):
        #skip duplicate anchor to avoid duplicate triplets
        if nums[i] > 0 and nums[i] == nums[i-1]:
            continue

        left = i+1
        right = len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == 0:
                res.append([nums[i], nums[left], nums[right]])
                #move left and right inward, skipping all duplicates valuesimultaneosly
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1

              
            elif current_sum < 0:
                left +=1
            else:
                right -=1

    return res

if __name__ == "__main__":
    numbers = [-1, 0, 1, 2, -1, -4]
    result = three_sum(numbers)
    print(f"Triplets found: {result}")
    
    # Let's make the assertion check robust
    expected = [[-1, -1, 2], [-1, 0, 1]]
    for item in expected:
        assert item in result, f"Missing expected triplet {item}"
        
    print("Success: Three-Pointer 3Sum verified.")
