# Given the root is binary tree check if is mirror of itself or not

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def is_symmetric(root : TreeNode | None):
    if not root:
        return True
    
    def is_mirror(t1: TreeNode | None, t2: TreeNode | None) -> bool:
        #Base Cases :
        if not t1 and not t2:
            return  True
        if not t1 or not t2 or t1.val != t2.val:
            return False
        # Recursive check
        return is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left)
    
    return is_mirror(root.left, root.right)


if __name__ == "__main__":
    # Construct a symmetric tree:
    #       1
    #     /   \
    #    2     2
    #   / \   / \
    #  3   4 4   3
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(3), TreeNode(4))
    root.right = TreeNode(2, TreeNode(4), TreeNode(3))
    
    result = is_symmetric(root)
    print(f"Is the tree symmetric?: {result}")
    
    assert result == True, "Test Failed"
    print("Success: Symmetric Tree verification passed.")