class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        lt = []
        return self.find(root, k, lt)

    def find(self, root: TreeNode, k, lt):
        if root is None:
            return False
        if (k - root.val) in lt:
            return True
        lt.append(root.val)
        return self.find(root.left, k, lt) or self.find(root.right, k, lt)


if __name__ == '__main__':
    so = Solution
    print(so.findTarget(so, [5, 3, 6, 2, 4, None, 7], 9))
