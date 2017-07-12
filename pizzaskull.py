
#some functions for Andy's game

from pprint import pprint

A = "A"
B = "B"
C = "C"
D = "D"

matrix = [
            [A, B, C, B],
            [C, A, A, B],
            [A, A, A, B],
            ]

matrix2 = [
            [A, B, C, D, C, C, C],
            [C, A, A, B, A, C, D],
            [A, A, A, B, A, A, D],
            ]

matrix3 = [
            [A, D, C, B, C, D, D],
            [C, A, A, D, A, C, D],
            [A, A, A, A, A, A, D],
            ]



def find_matches_of_three2(matrix):

    x_axis = len(matrix[0])
    y_axis = len(matrix)

    bubbles_to_remove_v = []
    bubbles_to_remove_h = []
    bubbles_to_remove = []

    for i in range(y_axis):
        checking_for_three = []
        bubbles_to_remove_v = []
        checking_for_three = [matrix[i][0]]
        bubbles_to_remove_v.append((matrix[i][0], i, 0))
        for j in range(1, x_axis):
            if matrix[i][j] not in checking_for_three:
                checking_for_three = []
                bubbles_to_remove_v = []
            checking_for_three.append(matrix[i][j])
            bubbles_to_remove_v.append((matrix[i][j], i, j))

            if len(checking_for_three) > 2:
                bubbles_to_remove += bubbles_to_remove_v
                print "Found a horizontal match! Three of: ", checking_for_three[0]

    for i in range(x_axis):
        checking_for_three = []
        bubbles_to_remove_h = []
        checking_for_three = [matrix[0][i]]
        bubbles_to_remove_h.append((matrix[0][i], 0, i))
        for j in range(1, y_axis):
            if matrix[j][i] not in checking_for_three:
                checking_for_three = []
                bubbles_to_remove_h = []
            checking_for_three.append(matrix[j][i])
            bubbles_to_remove_h.append((matrix[j][i], j, i))

            if len(checking_for_three) > 2:
                bubbles_to_remove += bubbles_to_remove_h
                print "Found a vertical match! Three of: ", checking_for_three[0]

    print bubbles_to_remove
    return bubbles_to_remove

def find_four_surrounding_bubbles(matrix, bubble):

    x_axis = len(matrix)
    y_axis = len(matrix[0])

    x = bubble[0]
    y = bubble[1]

    surrounding_coord = []

    if y > 0:
        bottom = (x, y-1)
        surrounding_coord.append(bottom)

    if (y + 1) < y_axis:
        top = (x, y+1)
        surrounding_coord.append(top)

    if x > 0:
        left = (x-1, y)
        surrounding_coord.append(left)
  
    if (x + 1) < x_axis:
        right = (x+1, y)
        surrounding_coord.append(right)

    return surrounding_coord


def remove_dups(matrix, coordinates_to_remove):

    print "first matrix"
    pprint(matrix)
    for coordinate in coordinates_to_remove:
        value = coordinate[0]
        bubble = (coordinate[1], coordinate[2])
        matrix[coordinate[1]][coordinate[2]] = " "
        surrounding_coord = find_four_surrounding_bubbles(matrix, bubble)
        for coordinate in surrounding_coord:
            if matrix[coordinate[0]][coordinate[1]] == value:
                matrix[coordinate[0]][coordinate[1]] = " "

    print "************"
    print "second matrix"
    pprint(matrix)
    return matrix

print "MATRIX 1 **************************************"
coordinates_to_remove = find_matches_of_three2(matrix)
remove_dups(matrix, coordinates_to_remove)

print "MATRIX 2 **************************************"
coordinates_to_remove = find_matches_of_three2(matrix2)
remove_dups(matrix2, coordinates_to_remove)

print "MATRIX 3 **************************************"
coordinates_to_remove = find_matches_of_three2(matrix3)
remove_dups(matrix3, coordinates_to_remove)