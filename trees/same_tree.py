class TreeNode:
    def __init__(self, value: int, left: "TreeNode" = None, right: "TreeNode" = None):
        self.value = value
        self.left = left
        self.right = right

def is_same_tree(p: TreeNode | None, q: TreeNode | None) -> bool: # | is the unionr operator, either one type or the other.
    # deternmines if 2  binary trees are structurally identical with matching values.
    # time complexity : O(min(m,n)) - where m and n are teh numbers of nodes in the trees.
    # space complexity : O(min(h1, h2)) - call stach space dictated the shorter tree height.

    #step 1 : to check if both are empty
    if p is None and q is None:
        return True
    
    #step 2 : To check if one is empty and one is alive.
    if p is None or q is None:
        return False
    
    # if we passes step 2 that means both p and q are real
    #step 3 : to check if the values dont match.
    if p.value != q.value:
        return False
    
    # step 4 : the sub-problem delegation.
    # if we passed the step 3it means the current nodes are an perfeect match. now we want to force the function to perform this check on their children. the whole tree is valid only if the left sides match and the right sides match.
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


if __name__ == "__main__":
    t1 = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
    t2 = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
    t3 = TreeNode(1, left=TreeNode(2), right=TreeNode(4)) # Value mismatch at right leaf
    
    print(f"Verification 1 (Identical Match): {is_same_tree(t1, t2)}")  # Expected: True
    print(f"Verification 2 (Value Mismatch): {is_same_tree(t1, t3)}")    # Expected: False