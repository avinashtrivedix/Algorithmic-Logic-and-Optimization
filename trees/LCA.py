#Given a BST, find the lowest common ancestor node of two given nodes p and q. The lowest common ancestor is defined between two nodes p and q as the lowest node in the tree that has both p and q as descendents
# we allow a node to be descendent to be itself
# The logic : 
# you start at the root, look at the values of p and q, if both are greater than the current node, then the LCA must be in the right subtree.
# if both are less than the current node, then the LCA must be in the left left subtree. 
# if one is lees than and the other is greater than current node, then the current node is the LCA.


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root: TreeNode | None, p: TreeNode, q: TreeNode) -> TreeNode | None:
    curr = root
    while curr:
        # Both P and q are in the left subtree
        if p.val > curr.val and q.val > curr.val:
            curr = curr.right
        # Both p and q are in teh left subtree
        elif p.val < curr.val and q.val < curr.val:
            curr = curr.left
        else:
            return curr
    return None


if __name__ == "__main__":
    # Construct a BST:
    #         6
    #       /   \
    #      2     8
    #     / \   / \
    #    0   4 7   9
    #       / \
    #      3   5
    
    node3 = TreeNode(3)
    node5 = TreeNode(5)
    node4 = TreeNode(4, node3, node5)
    node0 = TreeNode(0)
    node2 = TreeNode(2, node0, node4)
    
    node7 = TreeNode(7)
    node9 = TreeNode(9)
    node8 = TreeNode(8, node7, node9)
    
    root = TreeNode(6, node2, node8)
    
    # Test Case 1: LCA of 2 and 8 should be 6
    p = node2
    q = node8
    result1 = lowest_common_ancestor(root, p, q)        
    print(f"LCA of {p.val} and {q.val} is: {result1.val}")
    assert result1.val == 6, "Test 1 Failed"            #An assrtion means, make sure that condiotion is true, if not truem stop the program and show this message.
    
    # Test Case 2: LCA of 2 and 4 should be 2
    p = node2
    q = node4
    result2 = lowest_common_ancestor(root, p, q)
    print(f"LCA of {p.val} and {q.val} is: {result2.val}")
    assert result2.val == 2, "Test 2 Failed"
    
    print("Success: Lowest Common Ancestor of BST verified.")