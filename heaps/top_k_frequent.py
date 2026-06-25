# Priority with the frequencies.
"""
The Problem : 
Given an integer array nums and an integer k, return the k most frequent element.
"""

#the naive approach - count all teh element and the frequencies, but that would take the O(nlogn) time and O(n)
from collections import Counter

def topKFrequent_count_sort(nums : list[int], k: int) -> list[int]:
    count = Counter(nums)
    return [item[0] for item in count.most_common(k)]

# bucket sort , fastest possible approach. it evaluates O(n) linear time complexity by avoiding sorting and and heaps entirely.
# intead of dorting by frequency, you use the frequncy as an index in an array of lists. (bucket)
#count frequnecy 

def topkFrequent_buckesort(nums: list[int],k: int) -> list[int]:
    #step1 : count frequncies
    count = {} #initialize and emoty has map to store numbers as keya asn their frequncies as values.
    for num in nums:
        count[num] = count.get(num, 0) + 1

    #step 2: Create buckets (indices from 0 to len(nums))
    buckets = [[] for _ in range(len(nums) + 1)] # shortcut to create the list populated with other empty lists. range

    #step 3: populate buckets based on frequnecy
    for num, freq in count.items(): # .items() method in python return a view object containing the key-value pairs of a dictionary as a tuple. 
        buckets[freq].append(num)

    # step 4 collect the top k elements from righ to left.
    result = []
    for i in range(len(buckets) -1, 0, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result
            

import heapq
from collections import Counter
def top_k_frequent_heap(nums: list[int], k: int) -> list[int]:
    """
    Finds the k most frequent elements using a frequency map and a pruned min-heap.
    Tine complexity : O(nlogk) - we push n unique elemnets into a heap of max size k.
    space complexity: O(n) - Allocated space for the frequency dictionary mapping tracker
    """

    # build a hash map tracking countnt of each number
    count_map = Counter(nums)
    min_heap = []

    # iterate through the unique numbers and their frequencies.
    for num, freq in count_map.items():
        heapq.heappush(min_heap, (freq, num))

    # if heap grows larger than k , discard the the lowest frequency element
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return [num for freq, num in min_heap]


if __name__  == "__main__":
    test_nums = [1,1,1,2,2,3]
    target_k = 2

    result = top_k_frequent_heap(test_nums, target_k)
    print(f"top {target_k} frquent Elements: {result}")