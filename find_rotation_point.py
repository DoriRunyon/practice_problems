
#Interview cake problem

"""
>>> words = ['undulate', 'xenoepist', 'asymptote']

>>> words2 = ['ptolemaic', 'retrograde', 'supplant', 'undulate', 'xenoepist', 'asymptote', 'babka', 'banoffee', 'engender', 'karpatka', 'othellolagkage']

>>> words3 = ['ptolemaic', 'retrograde', 'supplant', 'undulate', 'xenoepist', 'zone', 'asymptote', 'babka']

>>> words4 = ['supplant', 'argue', 'asia', 'asymptote', 'babka', 'banoffee', 'engender', 'karpatka', 'othellolagkage']

>>> words5 = ['xenoepist', 'asymptote', 'babka', 'banoffee', 'engender', 'karpatka', 'othellolagkage']

>>> words6 = ['ptolemaic', 'retrograde', 'supplant', 'undulate', 'xenoepist', 'xwt', 'abs', 'argue', 'asia', 'asymptote', 'babka', 'banoffee', 'engender', 'karpatka', 'othellolagkage']

>>> words7 = ['ptolemaic', 'argue', 'asia', 'asymptote', 'babka', 'banoffee', 'engender', 'karpatka', 'othellolagkage']

>>> words8 = ['lazy', 'loopy', 'babka', 'banoffee', 'engender', 'karpatka', 'othellolagkage']

>>> words9 = ['lazy', 'loopy', 'razor', 'dar', 'drat', 'engender', 'karpatka', 'zippy']

>>> find_rotation_point(words)
2

>>> find_rotation_point(words2)
5

>>> find_rotation_point(words3)
6

>>> find_rotation_point(words4)
1

>>> find_rotation_point(words5)
1

>>> find_rotation_point(words6)
6

>>> find_rotation_point(words7)
1

>>> find_rotation_point(words8)
2

>>> find_rotation_point(words9)
3

"""

def find_rotation_point(word_list, index_start=0):

    if len(word_list) <= 3:
        words = []
        for i in range(len(word_list)):
            words.append((word_list[i], i))
        words = sorted(words)
        return index_start + words[0][1]

    mid_point = len(word_list)/2

    first_list = word_list[:mid_point]
    second_list = word_list[mid_point:]

    first_list_first_word = first_list[0]
    first_list_second_word = first_list[-1]
    second_list_first_word = second_list[0]
    second_list_second_word = second_list[-1]

    alphabetize = sorted([first_list_second_word, first_list_second_word, second_list_first_word, second_list_second_word])

    if alphabetize[0] == first_list_first_word or alphabetize[0] == first_list_second_word:
        return find_rotation_point(first_list, index_start=index_start)
    elif alphabetize[0] == second_list_first_word or alphabetize[0] == second_list_second_word:
        return find_rotation_point(second_list, index_start=index_start+mid_point)

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED!\n"