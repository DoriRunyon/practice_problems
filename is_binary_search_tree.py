
"""

>>> A = BinaryTreeNode(4)
>>> B = A.insert_left(2)
>>> C = A.insert_right(6)
>>> D = A.left.insert_left(1)
>>> E = A.left.insert_right(3)
>>> F = A.right.insert_left(5)
>>> G = A.right.insert_right(7)

>>> A.is_binary_search_tree()
True


>>> H = BinaryTreeNode(7)
>>> I = H.insert_left(5)
>>> J = I.insert_right(6)
>>> K = J.insert_left(4)

>>> H.is_binary_search_tree()
False

"""


class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right





if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED!\n"


