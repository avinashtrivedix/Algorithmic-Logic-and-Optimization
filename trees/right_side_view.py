from collections import deque
class TreeNode:
    def __init__(self, value: int, left: "TreeNode" = None, right: "TreeNode" = None):
        self.value = value
        self.left = left
        self.right = right

def right_side_view(root: TreeNode| None) -> list[int]:
    """
    Returns the value id the nodes visible from the right side of the trree
    Time Complexity : O(n) - Every node is processed once
    Space COmplexity : O(w) - Ques stores at most maximum width of the tree.
    """
    if root is None:
        return []
    
    visible_nodes = []
    queue = deque([root]) # happens once. you initialize only once.
    while queue:
        # Happens at the start of every level.
        # This line dynamically measures the queue right after the previous level completely finished trading itself for its children.
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
        
            if i == level_size - 1:
                visible_nodes.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return visible_nodes


if __name__ == "__main__":
    # Assemble test tree:
    #       1
    #     /   \
    #    2     3
    #     \     \
    #      5     4
    tree = TreeNode(1,
        left=TreeNode(2, right=TreeNode(5)),
        right=TreeNode(3, right=TreeNode(4))
    )
    
    view_output = right_side_view(tree)
    print(f"Right Side View: {view_output}")  # Expected: [1, 3, 4]