from collections import deque

class TreeNode:
    def __init__(self, value: int, left: "TreeNode" = None, right: "TreeNode" = None):
        self.value = value
        self.left = left
        self.right = right

def zigzag_level_order(root: TreeNode | None) -> TreeNode:
    """
    performs an alternating zigzag level-order traversal on a binary tree
    Time-complexity: O(n) - Every Node is processed exactly once.
    space-complexity: O(n) - output allocation matches node count.
    """

    if root is None:
        return []
    
    results = []
    queue = deque([root])
    left_to_right = True

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range (level_size):
            node = queue.popleft()
            current_level.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if not left_to_right:
            current_level.reverse()


        results.append(current_level)
        left_to_right = not left_to_right

    return results

if __name__ == "__main__":
    tree = TreeNode(3,
        left=TreeNode(9),
        right=TreeNode(20, left=TreeNode(15), right=TreeNode(7))
    )
    
    zigzag_output = zigzag_level_order(tree)
    print(f"Zigzag Order Results: {zigzag_output}")
    # Expected: [[3], [20, 9], [15, 7]]