def is_superbalanced(binarytree):

    leaf_node_present = None

    nodes_to_check =[(binarytree, 0)]

    while nodes_to_check:

        current_node = nodes_to_check.pop()

        if leaf_node_present:
            if current_node[1] - leaf_node_present >= 2:
                return False

        if not current_node.left and not current_node.right:
            leaf_node_present = current_node[1]

        else:

            if current_node[0].left:
                nodes_to_check.append[(current_node[0].left, current_node[1]+1)]

            if current_node[0].right:
                nodes_to_check.append[(current_node[0].right, current_node[1]+1)]

    return True