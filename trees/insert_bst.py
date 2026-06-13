class TreeNode:
    def __init__(self, value: int, left: "TreeNode" = None, right: "TreeNode" = None):
        self.value = value
        self.left = left
        self.right = right

def insert_into_bst(root: TreeNode, value: int) -> TreeNode:
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert_into_bst(root.left, value)
    if value > root.value:
        root.right = insert_into_bst(root.right, value)
    return root

def print_tree_inorder(node: TreeNode | None) -> None:
    # helper ro verify BST preservation(In order traversal of a BST is always sorted)
    if not node:
        return
    print_tree_inorder(node.left)
    print(node.value, end= "  ")
    print_tree_inorder(node.right)

if __name__ == "__main__":
    # Assemble baseline tree
    #      4
    #     / \
    #    2   7
    baseline_root = TreeNode(4, left=TreeNode(2), right=TreeNode(7))
    
    print("In-order traversal before insertion:")
    print_tree_inorder(baseline_root)  # Expected output: 2 4 7
    print("\n")
    
    # Execute insertion of element 5
    updated_root = insert_into_bst(baseline_root, 5)
    
    print("In-order traversal after inserting 5:")
    print_tree_inorder(updated_root)   # Expected output: 2 4 5 7 (Perfectly sorted)
    print()