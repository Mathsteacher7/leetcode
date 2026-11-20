class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(root: TreeNode | None, k: int) -> int:
    answer = None
    count = 0

    def add_to_list(node: TreeNode):
        nonlocal count, answer
        if node is None or answer is not None:
            return
        add_to_list(node.left)
        if answer is not None:
            return
        count += 1
        if count == k:
            answer = node.val
        add_to_list(node.right)

    add_to_list(root)
    return answer
