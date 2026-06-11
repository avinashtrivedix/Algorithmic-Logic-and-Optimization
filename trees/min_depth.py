class TreeNode:
    def __init__(self, value: int, left: "TreeNode" = None, right: "TreeNode" = None):
        self.value = value
        self.left = left
        self.right = right

def min_depth(root: TreeNode | None) -> int:
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    if root.right is None:
        return min_depth(root.left)+ 1
    if root.left is None:
        return min_depth(root.right) + 1
    return min(min_depth(root.left), min_depth(root.right)) + 1


if __name__ == "__main__":
    # Test Case 1: Standard Balanced Split
    #      3
    #     / \
    #    9  20
    balanced_tree = TreeNode(3, left=TreeNode(9), right=TreeNode(20))
    print(f"Balanced Tree Min Depth: {min_depth(balanced_tree)}")  # Expected: 2
    
    # Test Case 2: The Single-Child Skew Trap
    #    1
    #   /
    #  2
    skewed_tree = TreeNode(1, left=TreeNode(2))
    print(f"Skewed Tree Min Depth: {min_depth(skewed_tree)}")      # Expected: 2