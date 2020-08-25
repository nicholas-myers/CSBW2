# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def isBalanced(root):
    h = 0
    
    def goLeft(node):
        if node.left:
            getHeight(node.left)
            h += 1
        else:
            return h
        return
    def goRight(node):
        if node.right:
            getHeight(node.right)
            h += 1
        else:
            return h
        return
    
    left_h = goLeft(root)
    right_h = goLeft(root)
    
    if left_h - right_h > 1:
        return False
    else: 
        return True
        