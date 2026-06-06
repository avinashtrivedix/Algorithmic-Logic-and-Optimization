from merge_sorted_lists import create_linked_list
class ListNode:
    def __init__(self, value: int = 0, next: "ListNode" = None):
        self.value = value
        self.next = next

# with a single pointerwe can do it by first calculating the legth of the list and then deleting that element form the last but it will take the O(n) time complexity because we need to traverse the list twice, once to calculate the length and once to delete the node
# this is non optimal solution becaus of O(n)  time complexity
# witht the two pointer the the time complexity is still O(n)
# solutiion with single pointer
def remove_nth_node_fron_end_single_pointer(head: ListNode, n:int) -> ListNode:
    dummy = ListNode(-1)
    dummy.next = head
    current = dummy
    length = 0
    while current.next:
        length += 1
        current = current.next
    current = dummy
    for _ in range(length - n): 
        current = current.next
    current.next = current.next.next
    return dummy.next


# solution with 2 pointers    
def remove_nth_node_from_end(head: ListNode, n:int) -> ListNode:
    dummy = ListNode(-1)
    dummy.next = head
    slow = dummy
    fast = dummy
    for _ in range(n+1):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next

if __name__ == "__main__":
    head = create_linked_list([1,2,3,4,5])
    n = 2
    new_head = remove_nth_node_from_end(head, n)
    current = new_head
    while current:
        print(current.value)
        current = current.next    
