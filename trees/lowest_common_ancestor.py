class TreeNode:
    def __init__(self, value: int, left: "TreeNode" = None, right: "TreeNode" = None,):
        self.value = value
        self.left = left
        self.right = right

def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # given the 2 target nodes find the lowest common ancestors.
    # time complexity average = O(logn) in the if the tree is average. nad step down one path, and completely discard the half of it
    # but if you tree is skewed essentially becoming the linked list, which is the worst case
    # you might have to visisit every single node once. in that case time complesity becomes O(n)
    #  space complexity - O(h) - due to memory consumed by recusive call stack
    if root is None or root == p or root == q:
        return root
    if p.value < root.value and q.value < root.value:
        return lowest_common_ancestor(root.left, p, q)
    if p.value > root.value and q.value > root.value:
        return lowest_common_ancestor(root.right, p, q)
    return root

if __name__ == "__main__":
    node_0 = TreeNode(0)
    node_3 = TreeNode(3)
    node_5 = TreeNode(5)
    node_4 = TreeNode(4, left=node_3, right=node_5)
    node_2 = TreeNode(2, left=node_0, right=node_4)
    node_8 = TreeNode(8)
    bst_root = TreeNode(6, left=node_2, right=node_8)

    # Test Case 1: Split paths (p=2, q=8) -> Should return 6
    lca_1 = lowest_common_ancestor(bst_root, node_2, node_8)
    print(f"LCA of 2 and 8: {lca_1.value}")  # Expected: 6

    # Test Case 2: Descendant of self (p=2, q=4) -> Should return 2
    lca_2 = lowest_common_ancestor(bst_root, node_2, node_4)
    print(f"LCA of 2 and 4: {lca_2.value}")  # Expected: 2