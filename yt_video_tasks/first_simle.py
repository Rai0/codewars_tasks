# [1, 2, 2, [23, 4, [3, 2]]] -> [1, 2, 2, 23, 4, 3, 2]
n = [1, 2, 2, [23, 4, [3, 2], 4, 1], 3]
open_n = []


def list_opener (n):
    for i in n:
        if type (i) == list:
            list_opener (i)
        else:
            open_n.append (i)


if __name__ == '__main__':
    list_opener (n)
    print (open_n)