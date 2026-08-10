# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        Consider, when you have tree, you have a pointer to left and then right, so what that means for branches is that all values below are tied to the parents
        So if you switch after the root, then so the branches follow, so do a recursive approach that might not be best for stack but next level would be an iterative DFS
        Remember that BFS goes by outside level, DFS goes by depth so whenever we reach 4, we go back to the 2 which is the parent, and go onto the right element
        Thus im happy because I understand BST
        def not super straightforward, but good learning

        '''


        # base case 
        if not root:
            return None 
        
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root 
