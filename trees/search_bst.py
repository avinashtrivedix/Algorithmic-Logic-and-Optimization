# bst property - bst is a binary tree with a strict mathematical ordering rule applied to every single  node.- 
# the ledt subtree of node contains only nodes with values strictly less that parents node values.
# the right subtree of node contails only nodes with value strictly greater than the parent nodes' value
# Both the left left and the right subtree must also be binary search

# given the root of a binary search tree and an integer value val, find the node in the bst whose value equals val and return the entire subtree rooted at that node.
# and the entire subtree rooted at that node.

class TreeNode:
    def __init__(self, value: int, left: "TreeNode" = None, right: "TreeNode"  = None ):
        self.value = value
        self.left = left
        self.right = right

# the binary strategy - time average - O(logn), space - O(h) 
# because the tree is pre sorted by design , if you if your target is smaller, 
# you completely discard the right half of the tree and move left. 
# if your target is smaller and you you completetly discard the left half 
# of the tree and move right. this mirriors binary search on an array.

def search_bst(root : TreeNode | None, val: int) -> TreeNode | None:
    if root is None:
        return None
    if root.value == val:
        return root
    if val < root.value:
        return search_bst(root.left, val)
    if val > root.value:
        return search_bst(root.right, val)
    

if __name__ == "__main__":
    bst_root = TreeNode(4,
        left=TreeNode(2, left=TreeNode(1), right=TreeNode(3)),
        right=TreeNode(7)
    )
    
    # Execute lookups
    result_node = search_bst(bst_root, 2)
    print(f"Target 2 Found: {result_node is not None}")
    if result_node:
        print(f"Subtree Root Value: {result_node.value}")  # Expected: 2
        print(f"Subtree Left Child: {result_node.left.value}")  # Expected: 1
        
    missing_node = search_bst(bst_root, 5)
    print(f"Target 5 Found: {missing_node is not None}")  # Expected: False