class ListNode:
    def __init__ (self, value: int = 0, next: "Listnode" = None):
        self.value = value
        self.next = next

def merge_sorted_lists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode() # we will use this dummy node to to build the merged list without worrying about the edge cases.
    tail = dummy # this tail pointer will always point towards the last node in the merged list
    while list1 and list2:
        if list1.value < list2.value:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    # at this point one of the node is exhausted and the other node still has some nodes left, so we will just point the next of the tail to the remaining nodes of the non-exhausted list.
    tail.next = list1 if list1 else list2
    return dummy.next

def create_linked_list(values: list[int]) -> ListNode:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

if __name__ == "__main__":
    list1 = create_linked_list([1,2,4])
    list2 = create_linked_list([1,3,4])
    merged_head = merge_sorted_lists(list1, list2)
    current = merged_head
    while current:
        print(current.value)
        current = current.next

