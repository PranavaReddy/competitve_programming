import unittest

def delete_node_to_delete(node_to_delete):

    ptr = node_to_delete.next
    if ptr:
        node_to_delete.next = ptr.next
        node_to_delete.value = ptr.value

    else:
        raise ValueError("cannot delete node")















# Tests

class Test(unittest.TestCase):

    class LinkedListnode_to_delete(object):

        def __init__(self, value, next=None):
            self.value = value
            self.next  = next

        def get_values(self):
            node_to_delete = self
            values = []
            while node_to_delete is not None:
                values.append(node_to_delete.value)
                node_to_delete = node_to_delete.next
            return values

    def setUp(self):
        self.fourth = Test.LinkedListnode_to_delete(4)
        self.third = Test.LinkedListnode_to_delete(3, self.fourth)
        self.second = Test.LinkedListnode_to_delete(2, self.third)
        self.first = Test.LinkedListnode_to_delete(1, self.second)

    def test_node_to_delete_at_beginning(self):
        delete_node_to_delete(self.first)
        actual = self.first.get_values()
        expected = [2, 3, 4]
        self.assertEqual(actual, expected)

    def test_node_to_delete_in_middle(self):
        delete_node_to_delete(self.second)
        actual = self.first.get_values()
        expected = [1, 3, 4]
        self.assertEqual(actual, expected)

    def test_node_to_delete_at_end(self):
        with self.assertRaises(Exception):
            delete_node_to_delete(self.fourth)

    def test_one_node_to_delete_in_list(self):
        unique = Test.LinkedListnode_to_delete(1)
        with self.assertRaises(Exception):
            delete_node_to_delete(unique)


unittest.main(verbosity=2)