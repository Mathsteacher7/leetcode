class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(root: TreeNode | None, k: int) -> int:
    num_list = []

    def add_to_list(node: TreeNode):
        if node is None:
            return
        add_to_list(node.left)
        num_list.append(node.val)
        add_to_list(node.right)

    add_to_list(root)
    return num_list[k - 1]
