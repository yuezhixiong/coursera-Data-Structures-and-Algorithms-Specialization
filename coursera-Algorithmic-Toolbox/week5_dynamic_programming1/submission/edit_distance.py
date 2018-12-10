# Uses python3
import sys
import time


def min_data(data_list):
    min_d = data_list[0]
    for i in range(len(data_list)):
        if min_d > data_list[i]:
            min_d = data_list[i]
    return min_d


def edit_distance(s, t):
    n, m = len(s), len(t)
    # print(n, m)
    D = []   # n * m
    for i in range(n + 1):
        D.append([])
        for j in range(m + 1):
            D[i].append(0)
    for i in range(n + 1):
        D[i][0] = i
    for j in range(m + 1):
        D[0][j] = j

    for j in range(1,  m + 1):
        for i in range(1, n + 1):
            insertion = D[i][j - 1] + 1
            deletion = D[i - 1][j] + 1
            match = D[i - 1][j - 1]
            mismatch = D[i - 1][j - 1] + 1
            if s[i - 1] == t[j - 1]:
                D[i][j] = min_data([insertion, deletion, match])
            else:
                D[i][j] = min_data([insertion, deletion, mismatch])
    return D[n][m]


if __name__ == '__main__':
    # read string 1
    s = [x for x in input()]
    # read string 2
    t = [x for x in input()]
    print(edit_distance(s, t))