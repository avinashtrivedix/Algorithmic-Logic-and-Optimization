class TreeNode:
    def __init__(self, value:int, left : "TreeNode" = None, right: "TreeNode" = None):
        self.value = value
        self.left = left
        self.right = right

def is_balanced(root: TreeNode | None) -> bool:
    # checks if a binary tree is height_balanced in O(n) time.
    # return True if balanced, False otherwise.
    # if the helper function returns -1 the tree is unbalanced
    return _check_height(root) != -1

def _check_height(node: TreeNode | None) -> int:
    # helper function that returns the height of the node if balanced, or -1 if any subtree is unbalanced
    if node is None:
        return 0
    
    # check the left subtree
    left_height = _check_height(node.left)
    if left_height == -1:
        return -1
    
    # check the right subtree
    right_height = _check_height(node.right)
    if right_height == -1:
        return -1
    
    # check the balanced condition at the current node
    if abs(left_height - right_height) > 1:
        return -1
    
    return max(left_height, right_height) + 1

if __name__ == "__main__":
    balanced_tree = TreeNode(3,left =TreeNode(9), right = TreeNode(20, left = TreeNode(15, right =TreeNode(7))))
    print(f"Balanced Tree Check: {is_balanced(balanced_tree)}")  # Expected: True

    # Test Case 2: Unbalanced Tree
    unbalanced_tree = TreeNode(1,
        left=TreeNode(2, left=TreeNode(3, left=TreeNode(4), right=TreeNode(4)), right=TreeNode(3)),
        right=TreeNode(2)
    )
    print(f"Unbalanced Tree Check: {is_balanced(unbalanced_tree)}")  # Expected: False