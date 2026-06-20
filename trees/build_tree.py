# given two integer arrays preorder and inrder where is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree.
class TreeNode:
    def __init__(self, value: int, left: "TreeNode" = None, right: "TreeNode" = None) -> "TreeNode":
        self.value = value
        self.left = left
        self.right = right

def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    """
    Builds a binary tree from preorder and inorder traversal arrays
    time complexity : O(n) maps the construction + O(1) lookups per node
    space complexity : O(n) - space allocated for the hash map tracking array indices
    """

    # map values to their indices in the inorder array for O(1) lookups
    inorder_map = {val : idx for idx, val in enumerate(inorder)}
    pre_idx = 0
    def _array_to_tree(left : int, right : int) -> TreeNode | None:
        nonlocal pre_idx

        # base case: No elements left in the current partition window
        if left > right:
            return None
        
        # Grab the current root value using the pre_idx tracker
        root_val = preorder[pre_idx]
        root = TreeNode(root_val)
        pre_idx += 1

        #split the inorder array into left and right subtree
        mid = inorder_map[root_val]

        # recusively build the subtree (left must be built first)
        root.left = _array_to_tree(left, mid-1)
        root.right = _array_to_tree(mid+1, right)

        return root
    
    return _array_to_tree(0, len(inorder) - 1)


def print_level_order(root: TreeNode | None) -> None:
    """
    Helper layout utility to verify structure via level-order output.
    """
    if not root:
        return
    from collections import deque
    queue = deque([root])
    results = []
    while queue:
        node = queue.popleft()
        if node:
            results.append(node.value)
            queue.append(node.left)
            queue.append(node.right)

        else:
            results.append(None)

        # Trim trailing Nones for clean presentation 
        while results and results[-1] is None:
            results.pop()
        print(results)

if __name__ == "__main__":
    preorder_data = [3, 9, 20, 15, 7]
    inorder_data = [9, 3, 15, 20, 7]

    constructed_root = build_tree(preorder_data, inorder_data)
    
    print("Level Order Verification of Constructed Tree:")
    print_level_order(constructed_root)  # Expected: [3, 9, 20, None, None, 15, 7]    
