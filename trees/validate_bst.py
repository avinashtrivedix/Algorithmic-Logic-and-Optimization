class TreeNode:
    def __init__(self, value: int, left: "TreeNode" = None, right: "TreeNode" = None):
        self.value = value
        self.left = left
        self.right = right

def is_valid_bst(root: TreeNode | None)-> bool:
    # validate a bst by enforcing global range contraints on every node
    # time complexity - O(n)
    # Space complexity - o(h)

    return _validate(root, float('-inf'),float('inf'))

def _validate(node: TreeNode | None, low: float, high: float) ->bool:
    # an empty tree is valid
    if not node:
        return True
    
    # check if the current value violates the current boundaries
    if not (low < node.value < high):
        return False
    

    # recursive step: check children with uddated boundaries
    # when going left, the current value becomes the new HIGH limit
    # when going right, the current value becomes the new low limit

    return _validate(node.left, low, node.value) and _validate(node.right, node.value, high)


if __name__ == "__main__":
    # Test Case 1: Valid BST
    valid_root = TreeNode(5, left=TreeNode(3), right=TreeNode(7))
    print(f"Valid Tree Test: {is_valid_bst(valid_root)}") # Expected: True

    # Test Case 2: Invalid BST (The Trap)
    #      5
    #     / \
    #    4   7
    #       /
    #      2  <-- This 2 is smaller than the root 5! (Invalid)
    invalid_root = TreeNode(5, 
        left=TreeNode(4), 
        right=TreeNode(7, left=TreeNode(2))
    )
    print(f"Invalid Tree Test: {is_valid_bst(invalid_root)}") # Expected: False