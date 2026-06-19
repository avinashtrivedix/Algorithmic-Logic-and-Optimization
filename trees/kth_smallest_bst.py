# given the root of binary search trees and an integer k , give the  k the smallese value. (1  - indexed). of all the values of nodes in the tree.
# the in order circuit strategy
# th foundational property of the binary search trees .performing  an in order traversal strategy (left, parent , right visits the nodde in perfectly sorted ascending orders.
# while your couls recursively dump every single node into a list and return list[k-1]
# but that approach forces an unnecessary O(n) space allocation layout.
# Instead we use an iterative stack to process the in order sequuence manually, this allows us to halt teh entire sngine teh exact moment it hit the k th element.

class TreeNode:
    def __init__(self, value: int, left:"TreeNode" = None, right : "TreeNode" = None):
        self.value = value
        self.left = left
        self.right = right


def _kth_smallest(root: TreeNode | None, k : int) -> int:
    """
    find the smallest value in a bst using a an iterative in order travesal 
    time complexity O(h+k)- process only upto the kth element
    space complexity: O(h)
    """

    stack = []
    current = root

    while stack or current:
        # drill down to the leftmost leaf , staging parent on the stack.
        while current:
            stack.append(current)
            current = current.left


        current = stack.pop()
        k = k-1

        # target discovery threshold check
        if k == 0:
            return current.value
        
        current = current.right

    return -1


if __name__ == "__main__":
    # Assemble validation tree:
    #         3
    #        / \
    #       1   4
    #        \
    #         2
    tree = TreeNode(3,
        left=TreeNode(1, right=TreeNode(2)),
        right=TreeNode(4)
    )
    
    # Target lookup executions
    print(f"1st Smallest Element: {_kth_smallest(tree, 1)}")  # Expected: 1
    print(f"3rd Smallest Element: {_kth_smallest(tree, 3)}")  # Expected: 3