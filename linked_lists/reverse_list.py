#linked list is a linear compbination of the data elements callsed nodes. 
# these nodes are scattered randomly across your memory.
#unlike the array, where all elemesnts sit next to each other in a contigious block of computer memory.
# this allows for instant lookups using an indext.
# in linked list they do not know where overall list start or ends. 
# a node only knows two things:
# 1. It's own data value
# 2. a memory address address of the very next node. (next)
# the linkekd list ends a node points to null (None in python)

# this is how we represent a single node in python
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode" = None):
        self.val = val
        self.next = next

# given the head of a singly linked list, 
# reverse the list in-place and return the new head of the reversed list.

# noob method - copy the values in python list and build a new linked list.
def noob_reverse_list(head: ListNode) -> ListNode:
    values = []
    current = head
    # extract all the values into a standard python list
    while current:
        values.append(current.val)
        current = current.next 

    new_head = None
    for val in reversed(values):

        new_head = ListNode(val, new_head)
    return new_head

# the optimal sloution - reverse the list in place by manipulating the next pointers of the nodes.
# what do you mean by manipulating the next pointers of the nodes?
# we will use three poiters in this solution, prev, current and next.
def reverse_list(head: ListNode) -> ListNode:
    prev = None
    current = head
    while current:
        next_node = current.next # store the next node
        current.next = prev
        prev = current
        current = next_node
    return prev # at the end of the loop prev will be the new head of the reversed list

# is this solution giving us the reversed list or just the head of the reversed list?
# this solution is giving us the head of the reversed list. we can travese the reversed list starting from the new head and print the values to verify that the list is indeed reversed.
# the time complexity of this solutuion is O(n) because we need to travese the entire list once, where n is the number of nodesin the list. the space complexity ids O(1) because we are using only a constand amount of extra space for the three pointers, regardless of the size of the input list.
# this is how we can test the solution:
if __name__ == "__main__":
    # creating a linked list 
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    # reversing the linked list
    new_head = reverse_list(head)
    # travesing the reversed list and printing the values
    current = new_head
    while current:
        print(current.val)
        current = current.next

# is there an optimal and better way to create a linked list then to endlessly write head.next = ListNode(val) for each value in the list?
# yes we can create a helper function that talkes a list of values and creates a linked list from those values.
def create_linked_list(values: list) -> ListNode:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


