import unittest
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
class Height:
    def __init__(self):
        self.height = 0
def is_balanced(root, height):
    lh = Height()
    rh = Height()
    if root is None:
        return True
    l = is_balanced(root.left, lh)
    r = is_balanced(root.right, rh)
    height.height = max(lh.height, rh.height) + 1
 
    if abs(lh.height - rh.height) <= 1:
        return l and r
    return False

class Test(unittest.TestCase):

    class BinaryTreeNode(object):

        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def insert_left(self, value):
            self.left = Test.BinaryTreeNode(value)
            return self.left

        def insert_right(self, value):
            self.right = Test.BinaryTreeNode(value)
            return self.right
      


    def test_full_tree(self):
        height = Height()
        tree = Test.BinaryTreeNode(5)
        left = tree.insert_left(8)
        right = tree.insert_right(6)
        left.insert_left(1)
        left.insert_right(2)
        right.insert_left(3)
        right.insert_right(4)
        result = is_balanced(tree,height)
        self.assertTrue(result)

    def test_both_leaves_at_the_same_depth(self):
        height = Height()
        tree = Test.BinaryTreeNode(3)
        left = tree.insert_left(4)
        right = tree.insert_right(2)
        left.insert_left(1)
        right.insert_right(9)
        result = is_balanced(tree,height)
        self.assertTrue(result)

    def test_leaf_heights_differ_by_one(self):
        height = Height()
        tree = Test.BinaryTreeNode(6)
        left = tree.insert_left(1)
        right = tree.insert_right(0)
        right.insert_right(7)
        result = is_balanced(tree,height)
        self.assertTrue(result)

    def test_leaf_heights_differ_by_two(self):
        height = Height()
        tree = Test.BinaryTreeNode(6)
        left = tree.insert_left(1)
        right = tree.insert_right(0)
        right_right = right.insert_right(7)
        right_right.insert_right(8)
        result = is_balanced(tree,height)
        self.assertFalse(result)

    def test_three_leaves_total(self):
        height = Height()
        tree = Test.BinaryTreeNode(1)
        left = tree.insert_left(5)
        right = tree.insert_right(9)
        right.insert_left(8)
        right.insert_right(5)
        result = is_balanced(tree,height)
        self.assertTrue(result)

    def test_both_subtrees_superbalanced(self):
        height = Height()
        tree = Test.BinaryTreeNode(1)
        left = tree.insert_left(5)
        right = tree.insert_right(9)
        right_left = right.insert_left(8)
        right.insert_right(5)
        right_left.insert_left(7)
        result = is_balanced(tree,height)
        self.assertFalse(result)

    def test_only_one_node(self):
        height = Height()
        tree = Test.BinaryTreeNode(1)
        result = is_balanced(tree,height)
        self.assertTrue(result)

    def test_linked_list_tree(self):
        height = Height()
        tree = Test.BinaryTreeNode(1)
        right = tree.insert_left(2)
        right_right = right.insert_right(3)
        right_right.insert_right(4)
        result = is_balanced(tree,height)
        self.assertTrue(result)


unittest.main(verbosity=2)