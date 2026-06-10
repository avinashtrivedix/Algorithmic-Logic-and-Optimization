class TreeNode:
    def __init__(self, value: int, left: "TreeNode" = None, right: "TreeNode" = None):
        self.value = value
        self.left = left
        self.right = right

def max_depth(root: TreeNode | None) -> int:
    # computing th emaximum depth of binary tree using a bottom up recursive approach.
    #time complexity: O(n) every node visited exactly once.
    # space complexity : O(h) - call stack space proportional to the height of tree.
    if root is None: # into the nothingness
        return 0 # we check the root the active variable not th eclass name Tree node, treeNode is the class name, idiot
    
    # recursive ca se: delegating th e work dow the left and the right branches.
    left_side_depth = max_depth(root.left)
    right_side_depth = max_depth(root.right)

    # Bubble up calculation: Take the tallest branch and add 1 for the current node
    return max(left_side_depth, right_side_depth) +1

if __name__ == "__main__":
    # Assemble the kingdom layout manually
    leaf_9 = TreeNode(9)
    leaf_15 = TreeNode(15)
    leaf_7 = TreeNode(7)
    parent_20 = TreeNode(20, left=leaf_15, right=leaf_7)
    root_node = TreeNode(3, left=leaf_9, right=parent_20)
    
    # Fire the calculation engine
    print(f"Verified Maximum Depth: {max_depth(root_node)}")  # Output: 3