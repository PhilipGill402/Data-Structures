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
                current = current.left
            elif element > current.element:
                current = current.right
            else:
                return None
        
        current = self.BTN(element)