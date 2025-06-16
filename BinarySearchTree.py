class BinarySearchTree:
    def __init__(self, root):
        self.root = self.BTN(root)

    class BTN:
        def __init__(self, element, left=None, right=None):
            self.element = element
            self.left = left
            self.right = right

    def height(self, node=-1):
        if node == -1:
            node = self.root
        if node == None:
            return 0

        leftHeight = self.height(node.left)
        rightHeight = self.height(node.right)
        return 1 + max(leftHeight, rightHeight)

    def add(self, element):
        current = self.root

        while current != None:
            if element < current.element:
                if (current.left == None):
                    current.left = self.BTN(element)
                    break
                current = current.left
            elif element > current.element:
                if (current.right == None):
                    current.right = self.BTN(element)
                    break
                current = current.right
            else:
                return -1
        
        return 1

    def remove(self, element):
        #find node
        current = self.root
        prev = None
        
        while current.element != element:
            prev = current
            if element < current.element:
                #element not found
                if current.left == None:
                    return -1
                current = current.left
            elif element > current.element:
                #element not found
                if current.right == None:
                    return -1
                current = current.right

        #case 1 - leaf node
        if current.left == None and current.right == None:
            if prev.left == current:
                prev.left = None
            else:
                prev.right = None

        #case 2 - single child
        elif (current.left is None) ^ (current.right is None):
            if current.left != None and prev.right == current:
                prev.right = current.left
            
            elif current.right != None and prev.right == current:
                prev.right = current.right

            elif current.left != None and prev.left == current:
                prev.left = current.left

            else:
                prev.left = current.right

        #case 3 - two children
        else:
            #find inorder successor
            successor = current
            while successor is not None:
                if successor.element == current.element:
                    successor = successor.right
                else:
                    if successor.left is None:
                        break
                    successor = successor.left
            
            self.remove(successor.element)
            current.element = successor.element

                
        return 1
