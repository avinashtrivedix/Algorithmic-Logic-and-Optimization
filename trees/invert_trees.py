# we are leaving the flat linear world of arrays, string, linked lists, stacks behind. we are escalating to non linear datastructure starting with trees.
#in linear structures every data element had a single next relationship. it moved forward or backward in a straigh line, In a Tree single data node can branch out into multiple paths simultaneaously. 
# the law if binary tree
# a biary tree is a tree data structure composed of nodes, where each node has at most two children reference (typically as lef and righ)
# we are going to invert a binary tree, the left and right children of all nodes in the tree are swapped.

class TreeNode:
    def __init__(self, value: int, left: "TreeNode" = None, right: "TreeNode" = None):
        self.value = value
        self.left = left
        self.right = right

def invert_tree(node: TreeNode) -> TreeNode:
    if node is None:
        return None
    
    #swap the left and the right children
    node.left, node.right = node.right, node.left
    # recusively invert the left and right subtrees
    invert_tree(node.left)
    invert_tree(node.right) 
    return node

# function to create a binary tree from a list of values (for testing purposes)
# instead of expliting writing TreeNode objects, we can use a helper function to create a helper function to create a binary tree from a listof values. this function will take a list of values and create a binary tree.

def create_binary_tree(values: list) -> TreeNode:
    if not values:
        return None
    nodes = [TreeNode(value) for value in values]
    for i in range(len(values)):
        left_index = 2 * i + 1 # the left child of a node at index 2i +1  . why ? this is the common invention.      
        right_index = 2 * i + 2
        if left_index < len(values):
            nodes[i].left = nodes[left_index]
        if right_index < len(values):
            nodes[i].right = nodes[right_index]
    return nodes[0]

def display_tree(node: TreeNode, level: int = 0, prefix: str = "Root:"):
    if node is not None:
        display_tree(node.right, level +1, "r--")
        print("  "* level +prefix + str(node.value))
        display_tree(node.left, level + 1, "l--")



if __name__ == "__main__":
    values = [1, 2, 3, 4, 5, 6, 7]
    root = create_binary_tree(values)
    inverted_root = invert_tree(root)
    print("riginal tree")
    display_tree(root)
    print("\nInverted tree")
    display_tree(inverted_root)