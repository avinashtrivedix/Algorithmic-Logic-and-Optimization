class TreeNode: 
    def __init__ (self, value: int, left : "TreeNode" = None, right : "TreeNode" = None):
        self.value = value
        self.left = left
        self.right = right

def max_path_sum(root: TreeNode | None) -> int:
    """
    compute the maximum path sum across any interconnected node sequence
    Time Complexity : O(n) - every node is evaluated exactly once
    space complexity : O(h) - stack allocation scale matches overall height
    """

    global_max = float("-inf")
    def _get_max_gain(node: TreeNode | None) -> int:
        nonlocal global_max
        if not node:
            return 0
        
        # extract maximum branch gains, clamping negative paths to 0
        left_gain = max(0, _get_max_gain(node.left))
        right_gain = max(0, _get_max_gain(node.right))

        # measure the complete path sum passing through the current node acting as a pivot
        current_price = node.value + left_gain + right_gain

        # challenge the global record holder
        global_max = max(global_max, current_price)

        # return the maximum single branch path gain up to the parent node
        return node.value + max(left_gain, right_gain)
    
    _get_max_gain(root)
    return global_max


if __name__ == "__main__":
    # Assemble test tree containing negative root penalty:
    #       -10
    #       /  \
    #      9    20
    #          /  \
    #         15   7
    tree = TreeNode(-10,
        left=TreeNode(9),
        right=TreeNode(20, left=TreeNode(15), right=TreeNode(7))
    )

    calculated_max = max_path_sum(tree)
    print(f"Calculated Maximum Path Sum: {calculated_max}")  # Expected: 42