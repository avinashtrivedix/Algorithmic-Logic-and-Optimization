# given the root of binary tree , return it's maximum depth. a binary tree's maximum depth is it's number of nodes alongs the longest path from the root node doen to the farthest leaf node.
# the logic: Trees are naturally recursive structure. If the node is None the depth is 0
# recursively calculate the maximum depth of the left subtree, recursively calculate the max depth of right sub tree
# the maximum depth from the current node is simply 1 for the current node itself. plus the greater of left and right subtree depths.

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: TreeNode | None) -> int:
    # Base case: if the node is empty, depth is zero
    if root is None:
        return 0
    
    # recursively fond the depth of the left and right subtrees.
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    # current depth is 1 plus the masx of the 2 subtree depths
    return 1 + max(left_depth, right_depth)


if __name__ == "__main__":
    # Construct a binary tree:
    #      3
    #     / \
    #    9  20
    #      /  \
    #     15   7
    root = TreeNode(3)
    root.left = TreeNode(0)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))
    
    result = max_depth(root)
    print(f"Maximum Tree Depth: {result}")
    
    assert result == 3, "Test Failed"
    print("Success: Maximum Depth of Binary Tree verified.")