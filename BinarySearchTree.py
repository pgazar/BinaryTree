# creating a Binary Search Tree

class BST:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def insert(self,val):
        if self.data is None:
            self.data = val

        if self.data == val:
            return
        
        if self.data > val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = BST(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = BST(val)
