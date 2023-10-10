class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level = 0
		
        def reverseHelper(left, right, level):
            if level%2==1:
                left.val, right.val = right.val, left.val
            if left.left:
                reverseHelper(left.left, right.right, level+1)
                reverseHelper(left.right, right.left, level+1)
        
        if root.left:
            reverseHelper(root.left, root.right, level+1)
        
        return root
                
               