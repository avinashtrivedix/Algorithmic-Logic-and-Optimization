# Serialization - the process of converting data structure or object into sequqence 
# of bits so that it can be store in a file or memory buffer, or transmitted across 
# a network connection link to be reconstructed later in the same or another computer environment
# design an algorthm to serialize of deserialize a binary tree.
# theres is no restriction on how your serialization/desirialization algorithm should work. 
# you just need to ensure that a binary tree can be serialized to a string and this 
# and this string can be desiralized to the original tree structure.

from collections import deque

class TreeNode:
    def __init__(self, value: int, left: "TreeNode" = None, right: "TreeNode" = None):
        self.value = value
        self.left = left
        self.right = right

class Codec:
    """
    serialize and desirialize binary tree structur using a level order BFS traversal.
    Time COmplexity : O(n) - Every node and null marker is processed exatly once.
    space complexity : O(n) - Queues and token lists scale linearly with total node count
    """

    def serialize(self, root: TreeNode | None) -> str:
        # encode a tree structure into a single delimited string layout.
        if not root:
            return "N"
        
        queue = deque([root])
        result = []

        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.value))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("N")

        return ",".join(result)
    
    def deserialize(sle, data:str) -> TreeNode | None:
        """decode your encoded string back into an in memory binary tree fromework"""
        if data == "N":
            return None
        
        tokens = data.split(",")
        root = TreeNode(int(tokens[0]))
        queue = deque([root])
        i = 1

        while queue:
            parent = queue.popleft()

            if tokens[i] != "N":
                parent.left = TreeNode(int(tokens[i]))
                queue.append(parent.left)
            i += 1

            if tokens[i] != "N":
                parent.right = TreeNode(int(tokens[i]))
                queue.append(parent.right)
            i += 1
        return root
    

if __name__ == "__main__":
    # Assemble test tree:
    #         1
    #        / \
    #       2   3
    #          / \
    #         4   5
    original_tree = TreeNode(1,
        left=TreeNode(2),
        right=TreeNode(3, left=TreeNode(4), right=TreeNode(5))
    )

    codec = Codec()

    # 1. Execute serialization transform
    serialized_string = codec.serialize(original_tree)
    print("Serialized Tree State String Output:")
    print(f"'{serialized_string}'\n")

    # 2. Execute deserialization recovery
    reconstructed_root = codec.deserialize(serialized_string)

    # 3. Verify object equality by re-serializing the clone
    validation_string = codec.serialize(reconstructed_root)
    print("Re-Serialized Clone State Verification:")
    print(f"'{validation_string}'")

    assert serialized_string == validation_string, "Architecture Error: Structs mismatch!"
    print("\n[System Alert]: Verification match confirmed. Serialization engine operating optimally.")