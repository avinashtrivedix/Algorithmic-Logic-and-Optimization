# Binary Search tree to leverage their ordered nature to validate the tree structure.
# problem - validate the binary search tree.
# the story - Given the root of binary tree, determine if it is a valid bst,, 
# valid bst is defined as follows: 
# the left subtree only contains the nodes with keys less than the node's keys
# the right subtree of a node contains only nodes with keys greater that than the nodes keys,
# both the left and right subtree must also also be valid binary search trees.
# common mistake is just checking if node.left.val < node.val < nide.right.val
# that fails because teh left subtree can have a node that is greater than the root node, 

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: TreeNode | None) -> bool:
    def validate(node: TreeNode | None, low : float, high : float) -> bool:
        # Base case: empty node is valid Bst
        if not node:
            return True
        
        # check if the current node value is withiin the valid range
        if not (low < node.val < high):
            return False
        
        # recusively update left and righ subtree with updated ranges
        return validate(node.left, low, node.val) and validate(node.right, node.val, high)
    return validate(root, float('-inf'), float('inf'))

if __name__ == "__main__":
    # Construct a valid BST:
    #      2
    #     / \
    #    1   3
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    
    result = is_valid_bst(root)
    print(f"Is valid BST?: {result}")
    
    assert result == True, "Test Failed"
    print("Success: Validate Binary Search Tree verified.")