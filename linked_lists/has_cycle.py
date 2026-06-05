class ListNode:
    def __init__(self, val: int = 0, next: "ListNode" = None):
        self.val = val
        self.next = next

# the naive approach, keep track of every single node we have seen in a hash set (hassh set is basically a data structure that allows us to store unique 
# values and check for their exixtence in O(1) time complexity). if we see a node that we have already seen before,
# then we know there is a cycle in a linked list. but in this approach the time complexity is O(n) because we need to traverse the entire list once, 
# and the space complexity is also O(n) because in the worst case we might need to store all the nodes in the hash set if there is no cycle in the list.
# the naive approach is not the optimal solution because of the O(n) space complexity.
# the bnaive approach


def has_cycle(head: ListNode) -> bool:
    seen = set()
    current = head
    while current:
        if current in seen:
            return True
        seen.add(current)
        current = current.next
    return False

# the optimal solution is to use the Floyd's Tortoise and Hare algorithm . which uses two pointers 
# to traverse the list at different speeds. the slow pointer (tortoise) moves one step at a time, 
# while the fast pointer (hare) moves teo step at a time is there is a cycle in the list,
# the fast pointer will eventually meet the slow pointer because they are moving at diffeentn speed 
# if there is no cycle in the list, the fast pointer will reach the end of the list without meeting the slow pointer. 
# the time complexity of this solution is still O(N) because in the worst case
# we need to traverse the entire list once, where n is the number of nodes in thet list. the spce complexity is the O(1) because we using only the two pointers, regardless of the size of the input list.
# the floyd's Tortoise and Hare algorithm
def has_cycle_floyd(head: ListNode) -> bool:
    if not head:
        return False
    slow = head
    fast = head
    while fast and fast.next: # we are trying to ensure that the fast pointer and the next node of the fast pointer is not null
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def create_linked_list(values: list[int], pos: int) -> ListNode:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    if pos != -1:
        cycle_start_node = head # we will use this variable to keep track of teh node where the cycle should start
        for _ in range(pos):
            cycle_start_node = cycle_start_node.next
            current.next = cycle_start_node
    return head
    


# test interface 
if __name__ == "__main__":
    #create linked list with cycle
    head_with_cycle = create_linked_list([3,2,0, -4], 1) 
    # create linked list without cycle
    head_without_cycle = create_linked_list([1,2],-1)
    # test the has_cycle function
    print("testing the naive approach:")
    print(has_cycle(head_with_cycle))
    print(has_cycle(head_without_cycle))
    print("testing the optimal approach;")
    print(has_cycle_floyd(head_with_cycle))
    print(has_cycle_floyd(head_without_cycle))