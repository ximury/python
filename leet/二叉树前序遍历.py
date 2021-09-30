from idlelib.tree import TreeNode
from typing import List

# 递归
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def preorder(root:TreeNode):
            if not root:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)

        res = list()
        preorder(root)
        return res

# 迭代
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = list()
        if not root:
            return res

        stack = []
        node = root
        # stack不为空，或者node不等于nil
        while stack or node:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return res

# 迭代
class Solution:
    # stack其实充当的是先进先出的队列，不是模仿栈行为
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:
            return ans
        stack = [root]
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ans