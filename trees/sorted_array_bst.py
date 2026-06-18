# because the array is already sorted we are going to leverage a clean divide and conquer algorithm.
# to ensure that the Tree is balanced we have to make sure that the root must be the element sitting in the middle of an array.

class TreeNode:
    def __init__(self, value: int, left: "TreeNode" = None, right: "TreeNode" = None):
        self.value = value
        self.left = left
        self.right = right

def sorted_array_to_bst(nums: list[int]) -> TreeNode | None:
    """
    converts a sorted array into a height balanced bst using divide and conquer pointers.
    time complexity: O(n) Every element in the array is transformed into exactly one node.
    space complexity: O(logn) -  the recursion stack depth is bounded by the balanced height.
    """
    def _build_tree_(left: int, right: int) -> TreeNode | None:
        #base case
        if left > right:
            return None
        # find the exact middle indexr of the current window segment
        mid = (left+right)//2
        # create the parent node from the middle value
        node =TreeNode(nums[mid])
        #recursively build the left arm using elements
        node.left = _build_tree_(left, mid -1)
        #recusively build the right arm using elements to the right
        node.right = _build_tree_(mid+1, right)
        #return this subtree node back to it's parent pointer.
        return node
    
    return _build_tree_(0, len(nums) - 1)

def print_tree_inorder(node: TreeNode | None) -> None:
    """helper utility to verify BST sorting order preservation."""
    if not node :
        return
    print_tree_inorder(node.left)
    print(node.value, end = " ")
    print_tree_inorder(node.right)

if __name__ == "__main__":
    sorted_inputs = [-10, -3, 0, 5,9]
    bst_root = sorted_array_to_bst(sorted_inputs)
    print("in order validation (must be sorted):")
    print_tree_inorder(bst_root)
    print("\n")
    print(f"verified balanced root Node: {bst_root.value}")
