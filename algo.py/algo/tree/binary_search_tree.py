# Binary Search Tree
#
# 1. the key in each node >= any keys in the left sub-tree
# 2. the key in each node <= any keys in the right sub-tree
# 3. the leaves contain no key

from collections import deque

class BinarySearchTree:
    #
    def __init__(self, root = None):
        assert root is None or _is_bst(root)
        self._root = root
    #
    @classmethod
    def from_preorder(cls, key_value_pairs):
        return BinarySearchTree(_from_preorder(key_value_pairs))
    @classmethod
    def from_inorder(cls, key_value_pairs):
        return BinarySearchTree(_from_inorder(key_value_pairs))
    #
    @property
    def root(self):
        return self._root
    #
    def __contains__(self, key):
        return _search(self._root, key) is not None
    def __getitem__(self, key):
        node = _search(self._root, key)
        if node is None:
            raise IndexError()
        return node.value
    def __setitem__(self, key, value):
        self.insert(key, value)
    def __delitem__(self, key):
        self.remove(key)
    def insert(self, key, value):
        self._root = _insert(self._root, key, value)
    def remove(self, key):
        self._root = _remove(self._root, key)
    def preorder(self):
        from binary_tree import preorder
        for node in preorder(self.root):
            yield (node.key, node.value)
    def inorder(self):
        from binary_tree import inorder
        for node in inorder(self.root):
            yield (node.key, node.value)
    def postorder(self):
        from binary_tree import postorder
        for node in postorder(self.root):
            yield (node.key, node.value)
    def levelorder(self):
        from binary_tree import levelorder
        for node in levelorder(self.root):
            yield (node.key, node.value)

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

def _search(root, key):
    if root is None or key == root.key:
        return root
    elif key < root.key:
        return _search(root.left, key)
    else: # key > root.key
        return _search(root.right, key)

def _insert(root, key, value):
    if root is None:
        # return a new node if the tree is empty
        return Node(key, value)
    elif key < root.key:
        # recurse down left subtree
        root.left = _insert(root.left, key, value)
    elif key > root.key:
        # recurse down right subtree
        root.right = _insert(root.right, key, value)
    elif key == root.key:
        # update value
        root.value = value
    # return the (unchanged) node
    return root

def _remove(root, key):
    if root is None:
        raise IndexError()
    elif key < root.key:
        root.left = _remove(root.left, key)
    elif key > root.key:
        root.right = _remove(root.right, key)
    else: # key == root.key
        # root with only one child or no child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        # root with two children:
        # 1. find inorder successor
        tmp = root.right
        if tmp.left is not None:
            tmp = tmp.left
        # 2. replace the content of root node
        root.key, root.value = tmp.key, tmp.value
        # 3. delete the inorder successor
        root.right = _remove(root.right, tmp.key)
    return root

def _is_bst(root):
    if root is None:
        return False
    def check(t, lo, hi):
        if t is None:
            return True
        if t.key < lo or t.key > hi:
            return False
        return check(t.left, lo, t.key) and check(t.right, t.key, hi)
    def find_min(t):
        if t.left is None:
            return t.key
        else:
            return find_min(t.left)
    def find_max(t):
        if t.right is None:
            return t.key
        else:
            return find_max(t.right)
    return check(root, find_min(root), find_max(root))

def _from_preorder(key_value_pairs):
    def build_subtree(kv, lo, hi):
        if len(kv) == 0:
            return None
        (key, value) = kv.popleft()
        if lo <= key and key <= hi:
            node = Node(key, value)
            node.left = build_subtree(kv, lo, key)
            node.right = build_subtree(kv, key, hi)
            return node
        else:
            kv.appendleft((key, value))
            return None
    q = deque(key_value_pairs)
    return build_subtree(q, min(map(lambda x: x[0], q)), max(map(lambda x: x[0], q)))

def _from_inorder(key_value_pairs):
    n = len(key_value_pairs)

if __name__ == "__main__":
    preorder = [(10, 'A'), (5, 'B'), (1, 'C'), (7, 'D'), (40, 'E'), (50, 'F')]
    bst = BinarySearchTree.from_preorder(preorder)
    print(str(list(bst.preorder())))
    print(str(list(bst.inorder())))
    print(str(list(bst.postorder())))
    print(str(list(bst.levelorder())))
    bst[6] = 'ABC'
    print(str(list(bst.inorder())))
    del bst[10]
    print(str(list(bst.inorder())))