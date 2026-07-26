# POinter manipulation with linked list
# You are gien the head of a singly linked list. you need to reverse the list and return the new head
# the logic - Unlike arrays where you can swap using indices, a linked listonly lets you move forward. using (node.next). TO reverse you need three trackinp pointer
# prev, curr, during each step, you store next_node = curr.next, flip curr.
# In a standard linked list, each node only knows ablut the next node in the line, To reverse the list you have to make each node point to the previous node instead.


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

    
def reverse_list(head: ListNode | None) -> ListNode | None:
    prev = None
    curr = head

    while curr:
        next_node = curr.next   # temorarily store the next node
        curr.next = prev        # Reverse the pointer backward
        prev = curr             # Advance the prev to curremt
        curr = next_node        # Advance curr to the next node

    return prev

if __name__ == "__main__":
    # Helper to build a linked list: 1 -> 2 -> 3 -> None
    head = ListNode(1, ListNode(2, ListNode(3, None)))
    
    reversed_head = reverse_list(head)
    
    # Verify the reversed list: 3 -> 2 -> 1 -> None

    vals = []
    curr = reversed_head
    while curr:
        vals.append(curr.val)
        curr = curr.next
        
    print(f"Reversed Linked List values: {vals}")
    assert vals == [3, 2, 1], "Test Failed"
    print("Success: Linked List Reversal verified.")