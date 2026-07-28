# the story : you are given the head if singly linked list. The list represented as 
# Reorder the linked list from -
# L0 -> L1 -> ...Ln-1 -> Ln
# to this
# L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...
# the Logic : find the midle. Reverse the second half. Merge Alternatingly.


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def reorder_list(head: ListNode | None) -> None:
    if not head or not head.next:
        return
    
    # step 1: Find the middle of the linked list.
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    #step 2:  Rverse the second half of the list.
    prev = None
    curr = slow.next
    slow.next = None    # cut the second half from the first half

    # You have to change the direction of the "arrows" (pointers) one by one, Think of this code as moving along the train track and flipping the rails backward behind as you go.
    # curr (current): the node you are currently standing on
    # prev (previous): The node behind you initially None, because the nothing is behind the first node
    # next_node : A temporary place holder to remember  where the rest of the train is
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    # step 3 : Merge the two halves alternatingly
    first = head
    second = prev

    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2



if __name__ == "__main__":
    # Helper to build a linked list: 1 -> 2 -> 3 -> 4
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    
    reorder_list(head)
    
    # Verify the reordered list: 1 -> 4 -> 2 -> 3
    vals = []
    curr = head
    while curr:
        vals.append(curr.val)
        curr = curr.next
        
    print(f"Reordered Linked List values: {vals}")
    assert vals == [1, 4, 2, 3], "Test Failed"
    print("Success: Linked List Reordering verified.")