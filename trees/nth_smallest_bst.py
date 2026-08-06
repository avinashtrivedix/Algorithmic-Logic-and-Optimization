# given a root is bst and an an integer k , return the kth smallest element in teh bst.
# the logic: A fundamental property if bst id that in order travers, (left -> root -> right) visits every single node in strictly ascentding srted order.
# Intead of storing all the elements in an array and then returning the kth element,
# we simulate an in order traversal using the stack and 
# decrement k everytime you pop or visit the node,
# the moment k ==0, you have found the exact target valueu without needing to traverse the rest of the tree.

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root : TreeNode|None, k: int) -> int:
    stack = []
    curr = root

    while curr or stack:
        # reach the left most node of the current subtree
        while curr:
            stack.append(curr)
            curr = curr.left

        # pop the top node from the stack
        curr = stack.pop()
        k -= 1

        if k == 0:
            return curr.val
        
        # move to the right subtree
        curr = curr.right

    return -1  # This line is just a safeguard; in a valid BST with k within bounds, we should never reach here.

if __name__ == "__main__":
    # Construct a BST:
    #       5
    #      / \
    #     3   6
    #    / \
    #   2   4
    #  /
    # 1
    root = TreeNode(5)
    root.left = TreeNode(3, TreeNode(2, TreeNode(1), None), TreeNode(4))
    root.right = TreeNode(6)
    
    k_val = 3
    result = kthSmallest(root, k_val)
    print(f"The {k_val}-th smallest element is: {result}")
    
    assert result == 3, "Test Failed"
    print("Success: Kth Smallest Element in BST verified.")