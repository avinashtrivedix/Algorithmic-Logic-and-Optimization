# given an array of intervals where intervals[i] = [start_i, end_i]
# merge all the overlapping intervals, and return an array of the non_overlapping intervals that covers all the intervals in the input
# sort the values basede on their start time. 
# once they are sorted, any overlapping intervals intervals that covers all the interals in the input 


def merge(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []
    
    # step 1: sort intervals based on they starting values - 
    intervals.sort(key = lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        last_merged_end = merged[-1][1]
        
        # If current interval overlaps with the last merged one, merge them
        if current[0] <= last_merged_end:
            merged[-1][1] = max(last_merged_end, current[1])

        else:
            #No Ovelaps, safe to add as a new separate intervals
            merged.append(current)

    return merged

if __name__ == "__main__":
    test_intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    result = merge(test_intervals)
    print(f"Merged intervals: {result}")
    
    assert result == [[1, 6], [8, 10], [15, 18]], "Test Failed"
    print("Success: Merge Intervals verified.")