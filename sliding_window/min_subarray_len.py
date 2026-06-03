def min_subarray_len(array: list[int], target: int) -> int:
    min_length = float("inf")
    current_sum = 0
    left = 0
    for right in range(len(array)):
        current_sum += array[right]
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= array[left]
            left +=1
    return min_length if min_length != float("inf") else 0