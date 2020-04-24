

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def bstFromPreorder(pre):
    stack = []
    root = TreeNode(pre[0])

    stack.append(root)
    i = 1
    size = len(pre)

    while i < size:
        temp = None

        while (len(stack) > 0 and pre[i] > stack[-1].val):
            temp = stack.pop()

        if temp is None:
            temp = stack[-1]
            temp.left = TreeNode(pre[i])
            stack.append(temp.left)
        else:
            temp.right = TreeNode(pre[i])
            stack.append(temp.right)
        i+=1
    return root

def printInorder(node):  
    if (node == None):  
        return
    print(node.val, end = " ")     
    printInorder(node.left) 
    
    printInorder(node.right)

root = bstFromPreorder([8,5,1,7,10,12]) 
printInorder(root)