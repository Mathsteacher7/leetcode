def isSameTree(p, q) -> bool:
    if p is None and q is None:
        return True
    elif p is None or q is None or p.val != q.val:
        return False
    else:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
