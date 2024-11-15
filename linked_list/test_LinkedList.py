import unittest
from LinkedList import LinkedList, Node
from unittest.mock import patch
import io

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()

    def test_append(self):
        self.ll.append(1)
        self.assertEqual(self.ll.head.data, 1)
        self.ll.append(2)
        self.assertEqual(self.ll.head.next.data, 2)

    def test_prepend(self):
        self.ll.prepend(1)
        self.assertEqual(self.ll.head.data, 1)
        self.ll.prepend(2)
        self.assertEqual(self.ll.head.data, 2)
        self.assertEqual(self.ll.head.next.data, 1)

    def test_delete_with_value(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)
        self.ll.delete_with_value(2)
        self.assertEqual(self.ll.head.next.data, 3)
        self.ll.delete_with_value(1)
        self.assertEqual(self.ll.head.data, 3)

    def test_find(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)
        self.assertEqual(self.ll.find(2).data, 2)
        self.assertIsNone(self.ll.find(4))

    def test_print_list(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.ll.print_list()
            self.assertEqual(fake_out.getvalue().strip(), "1\n2\n3")

if __name__ == '__main__':
    unittest.main()