class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def height(root):
    if not root:
        return 0

    return max(height(root.left), height(root.right)) + 1



def checkHeightBalanced(root):
    if not root:
        return True
    
    lh = height(root.left)
    rh = height(root.right)

    if (abs(lh - rh) > 1) and not  checkHeightBalanced(root.left) and not checkHeightBalanced(root.right):
        return True

    return False


if __name__ == "__main__":
    root = Node(1) 
    root.left = Node(2) 
    root.right = Node(3) 
    root.left.left = Node(4) 
    root.left.right = Node(5) 
    root.left.left.left = Node(8) 
    root.left.left.left.left = Node(8)


    if checkHeightBalanced(root): 
        print("Tree is balanced") 
    else: 
        print("Tree is not balanced") 