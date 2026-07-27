# the story - Give a head of the linked list, determine if the linked list has a cycle is it. A cycle exists if there is some node in the list that can be reached again by continuaslyfollowing the next pointer.
# the cycle exists if some node in the list that can be reached again by continuosly following the next pinter.
# The Logic : if you use the has set to store the visited nodes, it takes O(n) extra space. The optimal O(space approach is Floyd's Cycle-Finding Algorithm) (Tortoise and Hare):
# Initialize 2 pointers: sloaw and fast , if there is no cycle fast will eventually reach None.
# If there is no cycle, the fast pointer will eventually lap through slow, causing them to point exactly to the same node.


class ListNode:
    def __init__ (self, val = 0, next = None):
        self.val = val
        self.next = next


def has_cycle(head: ListNode | None)-> bool:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next            # move 1 step
        fast = fast.next.next       # move 2 step

        if slow == fast:
            return True             # They met, cycle exists
        
    return False


if __name__ == "__main__":
    # Create a cyclic linked list: 3 -> 2 -> 0 -> -4, and -4 points back to 2
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Cycle created here
    
    result = has_cycle(node1)
    print(f"Cycle detected: {result}")
    
    assert result == True, "Test Failed"
    print("Success: Tortoise and Hare Cycle Detection verified.")