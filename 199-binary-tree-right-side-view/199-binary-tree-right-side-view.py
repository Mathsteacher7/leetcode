from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(root: TreeNode | None) -> list[list[int]]:
    result = []
    if not root:
        return result
    queue = deque([root])
    while queue:
        right_most = None
        for _ in range(len(queue)):
            node = queue.popleft()
            right_most = node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(right_most)
    return result
