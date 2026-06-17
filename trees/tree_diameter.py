""" 
Definition - the diameter of the binary tree is the length of the loongest 
path between any two nodes in a tree. This path may or may not pass 
through the root. the length if a path between two nodes is represented 
by the number of edges between them.
Time Complexity: O(n) - Every node is evaluated exactly once.
spce_complexity: O(n) - stack allocation scale matches overall tree height.
"""

class TreeNode:
    def __init__(self, value: int, left: "TreeNode" = None, right: "TreeNode" = None):
        self.value = value
        self.left = left 
        self.right = right

def diameter_of_binary_tree(root: TreeNode | None) -> int:
    max_diameter = 0
    def _calculate_height(node: TreeNode | None) -> int:
        nonlocal max_diameter
        if not node:
            return 0
        
        # extract the maximum down-branch depths recursively
        left_height = _calculate_height(node.left)
        right_height = _calculate_height(node.right)

        # update the global record by local path limits
        max_diameter = max(max_diameter, left_height+ right_height)

        return max(left_height, right_height) + 1
    

    _calculate_height(root)
    return max_diameter

if __name__ == "__main__":
    # Assemble validation tree:
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5
    tree = TreeNode(1,
        left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
        right=TreeNode(3)
    )
    
    calculated_diameter = diameter_of_binary_tree(tree)
    print(f"Calculated Tree Diameter: {calculated_diameter}")  # Expected: 3