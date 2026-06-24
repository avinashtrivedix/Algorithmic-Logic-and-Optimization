# we split the data into two rooms, small room, and the large room. 
# the small room :  max heap:  this room hold the numbers that are in th elower half of the data stream , because iit is s max heap it i will always have the largest number sitting on the top.
# the large room :  min heap:  this room hold sall the number that are on the upper half of the data stream . because it is a min_stream...

# how we find the median instantly- 
# if both room has same no. of person, we simply get the number standing ion the gate of the rooms and find the average.
# if one room has one extra number (we alwasy keep that extra no. on the left room ) then the number ion the door of the large room is your median

import heapq

class MedianFinder:
    """
    tracks a real time data stream and finds the median in O(logn) time.
    """
    def __init__(self):
        self.small_max_heap = []
        self.large_min_heap = []

    def add_num(self, num : int) -> None:
        # Push to max_heap (lower half) first by inverting the value
        heapq.heappush(self.small_max_heap, -num)

        # Ensure every element in small_max_heap is <= every element in large_min_heap
        if self.small_max_heap and self.large_min_heap:
            if (-self.small_max_heap[0] > self.large_min_heap[0]):
                val = -heapq.heappop(self.small_max_heap)
                heapq.heappush(self.large_min_heap, val)
        # handle size balancing contraints (small room can have at most 1 extra element)
        if len(self.small_max_heap) > len(self.large_min_heap) +1:
            val = -heapq.heappop(self.small_max_heap)
            heapq.heappush(self.large_min_heap, val)

        if len(self.large_min_heap) > len(self.small_max_heap):
            val = heapq.heappop(self.large_min_heap)
            heapq.heappush(self.small_max_heap, -val)

    def find_median(self) -> float:
        if len(self.small_max_heap) > len(self.large_min_heap):
            return float(-self.small_max_heap[0])
        return (self.small_max_heap[0] + self.large_min_heap[0]) / 2.0
    

if __name__ == "__main__":
    tracker = MedianFinder()

    tracker.add_num(3)
    print(f"Current Median (After 3): {tracker.find_median()}")  # Expected: 3.0
    
    tracker.add_num(1)
    print(f"Current Median (After 1): {tracker.find_median()}")  # Expected: 2.0
    
    tracker.add_num(5)
    print(f"Current Median (After 5): {tracker.find_median()}")  # Expected: 3.0