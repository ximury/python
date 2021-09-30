from idlelib.tree import TreeNode

from pyasn1.compat.octets import null


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            print(root.children)
            left_height = height(root.left)
            right_height = height(root.right)
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            else:
                return max(left_height, right_height) + 1

        return height(root) >= 0


so = Solution()
tree_node_a = TreeNode(null, null, item=3)
tree_node_b = TreeNode(null, parent=tree_node_a, item=9)
tree_node_c = TreeNode(null, parent=tree_node_a, item=20)
tree_node_d = TreeNode(null, parent=tree_node_b, item=null)
tree_node_e = TreeNode(null, parent=tree_node_b, item=null)
tree_node_f = TreeNode(null, parent=tree_node_c, item=15)
tree_node_g = TreeNode(null, parent=tree_node_f, item=7)

# tree_node_a.left = tree_node_b
# tree_node_a.right = tree_node_c
# tree_node_b.left = tree_node_d
# tree_node_b.right = tree_node_e
# tree_node_c.left = tree_node_f
# tree_node_c.right = tree_node_g

print(so.isBalanced(tree_node_a))
