# Uses python3
import sys
import time


# operations: 0: +1, 1: x2, 2: x3


# from 1 to num:
def DpCalculator(num):
    # start_time = time.time()
    MinNumOpt = [0, 0]  # num 0: 0, num 1: 0
    if num <= 1:
        return MinNumOpt

    for m in range(2, num + 1):  # m: 0~num - 2
        MinNumOpt.append(m)
        NumOpt = [m, m, m]
        if m % 2 == 0:
            NumOpt[0] = int(MinNumOpt[int(m / 2)] + 1)
        if m % 3 == 0:
            NumOpt[1] = int(MinNumOpt[int(m / 3)] + 1)
        NumOpt[2] = int(MinNumOpt[int(m - 1)] + 1)
        minopt, minindex = m, 0
        for i in range(3):
            if minopt > NumOpt[i]:
                minopt = NumOpt[i]
                minindex = i
        if MinNumOpt[m] > minopt:
            MinNumOpt[m] = minopt

    # print(time.time() - start_time)
    return MinNumOpt


if __name__ == '__main__':
    # read money
    n = [int(x) for x in input().split()][0]
    MinNumOpt = DpCalculator(n)
    # print(n, MinNumOpt)
    # calculate the intermediate numbers: print(x, end=' ')
    num = n
    intermediate_n = [num]
    while num != 1:
        # print(num)
        NumOpt = [num, num, num]
        if num % 2 == 0:
            NumOpt[0] = MinNumOpt[int(num / 2)] + 1
        if num % 3 == 0:
            NumOpt[1] = MinNumOpt[int(num / 3)] + 1
        NumOpt[2] = MinNumOpt[num - 1] + 1
        minopt, minindex = num, 0
        for i in range(3):
            if minopt > NumOpt[i]:
                minopt = NumOpt[i]
                minindex = i
        # print(minopt, minindex)
        if 0 == minindex:
            num = int(num / 2)
            intermediate_n.append(num)
        elif 1 == minindex:
            num = int(num / 3)
            intermediate_n.append(num)
        elif 2 == minindex:
            num -= 1
            intermediate_n.append(num)
    # intermediate_n.append(1)
    if n == 1:
        print(0)
        print(1)
    else:
        print(MinNumOpt[n])
        intermediate_n.reverse()
        for v in intermediate_n:
            print(v, end=' ')