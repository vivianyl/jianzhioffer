## 二叉树的基本操作
def binary_tree(root):
    return [root, [], []]


def insert_left(root, newbran):
    t = root.pop(1)
    if t:
        root.insert(1, [newbran, t, []])
    else:
        root.insert(1, [newbran, [], []])
    return root


def insert_right(root, newbran):
    t = root.pop(2)
    if t:
        root.insert(2, [newbran, [], t])
    else:
        root.insert(2, [newbran, [], []])
    return root


def get_left(root):
    return root[1]


def get_right(root):
    return root[2]


def get_root_val(root):
    return root[0]


def set_root_val(root, val):
    root[0] = val




## 二叉树的遍历
# 有三种遍历方式，不同在于每个结点的访问顺序
# 先序遍历（preorder，根左右）
# 中序遍历（inorder, 左根右）
# 后序遍历（postorder,左右根）

# 使用递归遍历
def preorder(tree):
    if tree:
        print(get_root_val(tree))
        print(get_left(tree))
        print(get_right(tree))





if __name__ == "__main__":
    x = binary_tree('a')
    insert_left(x, 'b')
    insert_right(x, 'c')
    insert_right(get_right(x), 'd')
    print(x)