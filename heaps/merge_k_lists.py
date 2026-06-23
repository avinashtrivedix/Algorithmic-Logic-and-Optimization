"""
a heap is a specialized binary tree that satisfies two strict requirements:
1. The Hape property: It is a complete binary tree. this means every single gap is 
completely filled from left to right, with no missing gaps.
2. the heap property : 
in a min heap, the value of any given node must be greater than or equa to value of it's parent
therefore , the absolute smallesst element in the entire system is guaranteed to live at th etop root. 
(in am max-heap, the root holds the absolute larget element.)

the hiiden array mapping formula
the ultimate beaty of heap: because it is guarateed to be complete binary tree with not missing slots, we never use pointers, (node.left , node.right)
to build a heap. Instead , we flatten it completely into a standard array/list, and calculate child-parent realtionship and calculate chile parent
relationship using pure index arthmetic.
 
if a parent node lives at index i ina 0-indexed list, it's children are guaranteed
to live at these exact positions:
left child index : 2i+1
right child index : 2i+2
conversely if you are standing at any child node at index c, you can instantly find its parent
using this integer division formula
parent index = (c-1)//2
"""

"""real time data ingestion pipline that reads straming analytics from k different server channels simultaneously.
each individual stream is sorted in ascending order . merge all these sorted channels into a single , master sorted linked list.


if you ignore the fact that they are already sorted you and you pool them and and sort them from scratch, you you waste processing time, O(nlogn)
intead we use min-heap acting as a real time tournament tracker. the heap will only ever hold k elements
at any givrn moment"""

import heapq

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

    # python's heapq need a comaparision operator to sesolve ties if two nodes share identical values. we istruct it to evaluate memory location or order.
    def __lt__(self, other):
        return self.val < other.val
    
def merge_k_lists(lists: list[ListNode | None]) -> ListNode | None:
    """
    merge k sorted linkekd list into a a single master linked list using a Min-Heap
    Time Complexity: O(nlogk) - where n is the tital number of nodesm ansd k is the nuber of streams
    space complexity : O(k) - the heap only holds at most one node pointer per stram channel
    """
    min_heap = []

    # initialize the heap with head node of each non_empty list.
    for idx, l_head in enumerate(lists):
        if l_head:
            #we push a tuple: (node_value, unique_index, node_object)
            # the unique_index prevents python from crashing if 2 nodes have same values.
            heapq.heappush(min_heap, (l_head.val, idx, l_head))
        
    # create a dummy node to act as the head pointer of our final merged list.
    dummy = ListNode(0)
    current = dummy
    while min_heap:
        val, stream_idx, node = heapq.heappop(min_heap)

        #connect this node to our final master list chain
        current.next = node
        current = current.next

        # if the extracted node has the successor, in its, original stream, push it onto th heap.
        if node.next:
            heapq.heappush(min_heap, (node.next.val, stream_idx, node.next))

    return dummy.next

def print_linked_list(head: ListNode | None) -> None:
    """utility function to print sesequential node cleanly."""
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print(" -> ".join(vals))


if __name__ == "__main__":
    # Assemble Test Stream 1: 1 -> 4 -> 5
    s1 = ListNode(1, ListNode(4, ListNode(5)))
    # Assemble Test Stream 2: 1 -> 3 -> 4
    s2 = ListNode(1, ListNode(3, ListNode(4)))
    # Assemble Test Stream 3: 2 -> 6
    s3 = ListNode(2, ListNode(6))
    
    channels = [s1, s2, s3]
    
    print("Ingested Target Channels:")
    for c in channels:
        print_linked_list(c)
    print()
    
    merged_head = merge_k_lists(channels)
    
    print("Master Sorted Stream Output:")
    print_linked_list(merged_head)
    # Expected: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6