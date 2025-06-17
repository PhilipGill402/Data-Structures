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
        if node is None:
            return 0

        leftHeight = self.height(node.left)
        rightHeight = self.height(node.right)
        return 1 + max(leftHeight, rightHeight)

    def add(self, element):
        current = self.root

        while current is not None:
            if element < current.element:
                if (current.left is None):
                    current.left = self.BTN(element)
                    break
                current = current.left
            elif element > current.element:
                if (current.right is None):
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
                if current.left is None:
                    return -1
                current = current.left
            elif element > current.element:
                #element not found
                if current.right is None:
                    return -1
                current = current.right

        #case 1 - leaf node
        if current.left is None and current.right is None:
            #node to be deleted is the root
            if prev is None:
                self.root = None
            elif prev.left == current:
                prev.left = None
            else:
                prev.right = None

        #case 2 - single child
        elif (current.left is None) ^ (current.right is None):
            #node to be deleted is the root
            if prev is None:
                if self.root.left is not None:
                    self.root = self.root.left
                else:
                    self.root = self.root.right
                
            elif current.left is not None and prev.right == current:
                prev.right = current.left
            
            elif current.right is not None and prev.right == current:
                prev.right = current.right

            elif current.left is not None and prev.left == current:
                prev.left = current.left

            else:
                prev.left = current.right

        #case 3 - two children
        else:
            #find inorder successor
            successor_parent = current
            successor = current.right
            while successor.left is not None:
                successor_parent = successor
                successor = successor.left
            
            current.element = successor.element
            #if successor is current.right then we just remove successor from the tree
            if successor_parent = current:
                successor_parent.right = successor.right
            #if successor has a right subtree then it is added to its parents left subtree replacing successor
            else:
                successor_parent.left = successor.right

                
        return 1

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.element)
        self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.element)

    def preorder(self, node):
        if node is None:
            return
        print(node.element)
        self.preorder(node.left)
        self.preorder(node.right)
