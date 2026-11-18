class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: TreeNode | None) -> bool:
    def check(current: TreeNode, low: float, high: float) -> bool:
        if current is None:
            return True
        if low < current.val < high:
            return check(current.left, low, current.val) and check(
                current.right, current.val, high
            )
        return False

    return check(root, float("-inf"), float("inf"))
