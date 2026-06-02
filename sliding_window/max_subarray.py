#using nested loops/ brute forse method
def max_subarray(array: list[int], k: int) -> int:
    if k > len(array):
        return 0
    max_sum = float("-inf")
    # loop through all valid starting positions
    for i in range(len(array) - k+1):
        current_sum = 0
        # inner loop to add up the next elements
        for j in range(i, i+k):
            current_sum += array[j]

        #update our record holder if the current sum is larger
        max_sum = max(max_sum, current_sum)
    return max_sum

# The sliding window solution - imagine the glass window of size k that is sliding over the array, and we are keeping the track of the sum of the elements in the window,

def max_subarray_sliding_window_solution(array: list[int], k: int) -> int:
    if k > len(array):
        return 0
    max_sum = float("-inf")
    current_sum = sum(array[:k]) # sum of the first window
    max_sum = max(max_sum, current_sum)
    # slide the window exactly one position a at a time 
    for i in range(k, len(array)):
        current_sum += array[i] - array[i-k]
        max_sum = max(max_sum, current_sum)
    return max_sum


