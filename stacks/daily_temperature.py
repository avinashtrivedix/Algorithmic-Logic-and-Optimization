# The Monotonic Decreasing stack.
# you are given a list of daily temperature. For each day uou need to find how many days you would have tp wait until the warmer temperature. 
# if there is no future days for which this is possible , return 0 instead.
# the Logic :  the naicve approch is to look ahead for every single day O(n^2) time. 
# Thw professsional approach uses monotonic Stack to aolve it in a sinsle plass O(N) time
# the monotici stack: we maintain a stack that only stores indices of a temperatures in decreasing order of their values.
# Iterate through the array. 
# while the current temperature is warmer than the temperature at the index stored at the top of the stack, you have found your "Next Greater day" pop from the stack and calculate the difference in the days
# create a function for warmer days diffenece which take sthe list of daily temperature as the a argument. 
# create stack (which is basicallly set. ) as the lifo. 
# which will append strictly dcreasing temperature indices 
# and pop if it is increased , and then return the difference in the indices +1 
# otherwise return 0


def warmer_days_difference(temperatures: list[float]) -> list[int]:
    n = len(temperatures)
    # result array initialized to zero
    answer = [0] * n
    # stack will store indice, maintaining, a monotonically decreasing order of temperatures
    stack = []

    for i in range(n):
        # while stack is not empty and the current temperature is warmer than the top of the stack
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_index = stack.pop()
            # The differnece in indices gives the number of days to wait
            answer[prev_index] = i-prev_index

        stack.append(i)

    return answer

if __name__ == "__main__":
    #Test Case 1
    temps = [73, 74, 75, 71, 69, 72, 76, 73]
    # Expected: [1, 1, 4, 2, 1, 1, 0, 0]
    result = warmer_days_difference(temps)
    print(f"Result: {result}")
    
    assert result == [1, 1, 4, 2, 1, 1, 0, 0], "Test Failed"
    print("Success: Monotonic Stack algorithm verified.")