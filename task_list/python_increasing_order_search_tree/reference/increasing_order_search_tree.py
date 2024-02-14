class TreeNode:
    def __init__(self, value: int = 0, left: None | TreeNode = None, right: None | TreeNode = None) -> None:
        self.val = value
        self.left = left
        self.right = right


def increasing_binary_search_tree(root: TreeNode) -> TreeNode:
    dummy = tail = TreeNode()
    node = root

    stack = []
    while stack or node is not None:
        while node is not None:
            stack.append(node)
            node = node.left
        node = stack.pop()

        tail.right = node
        tail = node
        node.left = None

        node = node.right

    return dummy.right
