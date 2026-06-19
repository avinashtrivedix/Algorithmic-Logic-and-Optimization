# given the roots of t20 binary tree, root and sub root, return True  if there is a subtree of root with the same structure and node values of subroot.
# double recursions/ nested recursion/ interlockinf recursion. 
# - not simply mean a funcrion makes two recursion calls inside. like traversing left and right branches in standard dfs.
# instead it means you have 2 completely separate recursive function inside itself.
# two disinct engines

class TreeNode:
    def __init__(self, value: int, left: "TreeNode" = None, right : "TreeNode" = None):
        self.value = value
        self.left = left
        self.right = right

def is_subtree(root: TreeNode | None, subroot: TreeNode| None) -> bool:
    """
    check if subroot is structurally and identically a subtree of root.
    
    """
    if not subroot:
        return True
    if not root:
        return False
    
    #identity verification step
    if _is_identical(root, subroot):
        return True
    return is_subtree(root.left, subroot) or is_subtree(root.right, subroot)


def _is_identical(t1: TreeNode | None, t2: TreeNode| None) -> bool:
    # helper funtion to identify if two binary trees are ablsolute structural clone.
    # an empty space in a tree is reppresented by None(or null)
    # if nodes run out of nodes the variables (t1 or t2) becomes None.
    if not t1 and not t2 :
        return True 
    if not t1 or not t2 or  t1.value != t2.value :
        return False
    
    return _is_identical(t1.left, t2.left) and _is_identical(t1.right, t2.right)


if __name__ == "__main__":
    # Build Sub Tree:
    #      4
    #     / \
    #    1   2
    sub_tree = TreeNode(4, left=TreeNode(1), right=TreeNode(2))

    # Build Main Tree:
    #      3
    #     / \
    #    4   5
    #   / \
    #  1   2
    main_tree = TreeNode(3,
        left=TreeNode(4, left=TreeNode(1), right=TreeNode(2)),
        right=TreeNode(5)
    )

    print(f"Subtree Verification Result: {is_subtree(main_tree, sub_tree)}")  # Expected: True