class TreeNode():
    def innt(self, val = 0,left = None ,right = None):
        self.val = val
        self.left = left
        self.right = right

def is_same_tree(p: TreeNode | None, q: TreeNode | None) -> bool:
    # base case 1 :  both nodes are None, meaning we matched down this path
    if not p and not q:
        return True
    
    # Base Case 2 : Node is None or values dont match
    if not p or not p or p.val != q.val:
        return False
    
    # recursively check both left and right
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


if __name__ == "__main__":
    # Tree 1: [1, 2, 3]
    tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
    
    # Tree 2: [1, 2, 3]
    tree2 = TreeNode(1, TreeNode(2), TreeNode(3))
    
    result = is_same_tree(tree1, tree2)
    print(f"Are the trees identical?: {result}")
    
    assert result == True, "Test Failed"
    print("Success: Same Tree verification passed.")