# building a tree from serialization or traversing its structured layers. Let's tackle level order traversal. which transitions us from depth first recustion to the breadth first queue  traversal. 
# given the root of the binary tree, return order level traversal of the of ot's nodes values , ie. from level to left to righ level by vel.
# inlike depth first search recursive deapth first search, which goes from depp down in to a single path 
# initialize a wuen and add root note onto it. 
#Wwhile the que is not empty append the the value of the nodes exactly in that orer and and a dd root node onto it , while root node is not empty.
#popping node from th e front and append each levels values list in the final result.

from collections import deque

class TreeNode:
    def __init__(self, val =0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
def level_order(root : TreeNode | None) -> list[list[int]]:
    if not root:
        return []
    
    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result


if __name__ == "__main__":
    # Construct a binary tree:
    #      3
    #     / \
    #    9  20
    #      /  \
    #     15   7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))
    
    result = level_order(root)
    print(f"Level order traversal: {result}")
    
    assert result == [[3], [9, 20], [15, 7]], "Test Failed"
    print("Success: Level Order Traversal verified.")