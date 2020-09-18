class BinaryTree(object):
    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, newbran):
        if self.left_child:
            t = BinaryTree(newbran)
            t.left_child = self.left_child
            self.left_child = t
        else:
            self.left_child = BinaryTree(newbran)

    def insert_right(self, newbran):
        if self.right_child:
            t = BinaryTree(newbran)
            t.right_child = self.right_child
            self.right_child = t
        else:
            self.right_child = BinaryTree

    def get_left(self):
        return self.left_child

    def get_right(self):
        return self.right_child

    def get_root_val(self):
        return self.key

    def set_root_val(self, val):
        self.key = val



if __name__ == "__main__":
    x = BinaryTree('a')
    x.insert_left('b')
    x.insert_right('c')
    x.get_left().insert_left('d')
    print(x)

