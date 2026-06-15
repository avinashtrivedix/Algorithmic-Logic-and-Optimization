# because recursion inherently forces depth first dive, we mus abondon recursion for this problem
# to track nodes horizontallu, we use an iteratiev approach pwere by a Quieie data structure. which operates on a first in first out fifo basis.
# to separate the nodes into distinct sublists for each level, we use level size snapsot trick:
# place the root node insid a double ended queue (collections.dequeue)

from collections import deque

class TreeNode:
    def __init__(self, value: int, left: "TreeNode" = None, right: "TreeNode" = None):
        self.value = value
        self.left = left
        self.right = right

def level_order(root: TreeNode | None) -> list[list[int]]:
    """
    performs a level order (BFS) traversal on a binary tree.
    time complexity: O(n): every node is enqueued and dequeued exactly once.
    space complexity: O(w): where is the maximum width id the tree.
    """
    if root is None:
        return []
    results = []
    queue = deque([root])

    # loop throgh each horizontal tier of the tree.
    while queue:
        # capture a snapshot of how many nodes are on this specific level
        level_size = len(queue)
        current_level = []

        #process exactly the nodes belonging to this tier
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        results.append(current_level)

    return results

if __name__ == "__main__":
    # Assemble test layout
    #      3
    #     / \
    #    9  20
    #      /  \
    #     15   7
    tree = TreeNode(3,
        left=TreeNode(9),
        right=TreeNode(20, left=TreeNode(15), right=TreeNode(7))
    )
    
    # Execute breadth-first audit
    traversal_matrix = level_order(tree)
    print(f"Level Order Results: {traversal_matrix}")
    # Expected: [[3], [9, 20], [15, 7]]

