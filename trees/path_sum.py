class NodeTree:
    def __init__(self, value:int, left: "TreeNode" = None, right: "TreeNode" = None):
        self.value = value
        self.left = left
        self.right = right

   
    
def has_path_sum(root: NodeTree | None, Target_sum: int) -> bool:
    # given the root of a binary tree and an integer target_sum, return True. if the tree has a root to leaf path cush that all the valies a;ong the path equales the target sum.
    # time complexity - O(n) and space complexity for the call stack is going to be the height
    #base case - if if we stem of the tree into an empty sapce, no pasth exists
    if root is None:
        return False
    
    # processing the current nodoe state by subtracting it from it's value from our goal.
    remaining_sum = Target_sum - root.value

    # leaf validation check: if at an absolute leaf, check if the target hit zero.
    if root.left is None and root.right is None:
        return remaining_sum == 0
    
    return has_path_sum(root.left, remaining_sum) or (root.right , remaining_sum)

if __name__ == "__main__":
    test_tree = NodeTree(5,
    left=NodeTree(4, left=NodeTree(11, left=NodeTree(7), right=NodeTree(2))),
    right=NodeTree(8, left=NodeTree(13))
)
    
    # Validation evaluations
    print(f"Target 22 Verification: {has_path_sum(test_tree, 22)}")  # Expected: True
    print(f"Target 26 Verification: {has_path_sum(test_tree, 26)}")  # Expected: True
    print(f"Target 50 Verification: {has_path_sum(test_tree, 50)}")  # Expected: False
