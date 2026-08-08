# given an unsorted array of integers num and an integer k, return the kth largest element in the arra, 
# Ner the in the kth largest elent in teh sorted array, not the kth distinct element.

# the Logic : 
# sorting the entire array takes O(nlogn) time, but we can do better usinf a min head of fixed size k
# iterate through the array abd push elemnt in onto min heam usingnthe puthons heapq module, which is min heap by default.
# Because the heap evicts the smallest elements whenever it grows past capacity, it will retain only the k largest element of the entire stream. 


import heapq

def findKthLargest(nums:list[int], k:int) -> int:
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        # If heap exceeds size k, remove the smallest element
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    # the root of the min heap is the kth largest element
    return min_heap[0]


if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k_val = 2
    
    result = findKthLargest(nums, k_val)
    print(f"The {k_val}-th largest element is: {result}")
    
    assert result == 5, "Test Failed"
    print("Success: Kth Largest Element verified.")