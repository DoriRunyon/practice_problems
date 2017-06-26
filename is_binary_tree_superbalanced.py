"""

>>> A = BinaryTreeNode('A')
>>> B = BinaryTreeNode('B')
>>> C = BinaryTreeNode('C')
>>> A.left = B
>>> A.right = C

>>> A.is_superbalanced()
True


>>> D = BinaryTreeNode('D')
>>> E = BinaryTreeNode('E')
>>> F = BinaryTreeNode('F')
>>> G = BinaryTreeNode('G')
>>> H = BinaryTreeNode('H')
>>> D.left = E
>>> D.right = F
>>> E.left = G
>>> G.left = H

>>> D.is_superbalanced()
False

"""


#binary tree node class - given by Interview Cake
class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


    #my solution
    def is_superbalanced(self):

        leaf_node_present = None

        nodes_to_check =[(self, 0)]

        while nodes_to_check:

            current_node = nodes_to_check.pop()

            if leaf_node_present:
                if current_node[1] - leaf_node_present >= 2:
                    return False

            if not current_node[0].left and not current_node[0].right:
                leaf_node_present = current_node[1]

            else:

                if current_node[0].left:
                    nodes_to_check.append((current_node[0].left, current_node[1]+1))

                if current_node[0].right:
                    nodes_to_check.append((current_node[0].right, current_node[1]+1))

        return True

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED!\n"
