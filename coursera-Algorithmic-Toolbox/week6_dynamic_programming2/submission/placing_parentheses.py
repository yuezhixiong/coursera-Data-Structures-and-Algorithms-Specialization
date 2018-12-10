# Uses python3


def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    #write your code here
    operations = []
    numbers = []
    number = ''
    for each in dataset:
        if each not in ['*', '-', '+']:
            number += each
        else:
            numbers.append(int(number))
            number = ''
            operations.append(each)
    numbers.append(int(number))
    min_and_max = [len(numbers)*[(None, None)] for i in range(0, len(numbers))]
    for i in range(0, len(numbers)):
        min_and_max[i][i] = (int(numbers[i]), int(numbers[i]))
    for s in range(1, len(numbers)):
        for i in range(0, len(numbers) - s):
            j = i + s
            get_min_and_max(i, j, min_and_max, operations)
    return min_and_max[0][-1][0]


def get_min_and_max(i, j, min_and_max, op):
    for k in range(i, j):
        a = evalt(min_and_max[i][k][0], min_and_max[k+1][j][0], op[k])
        b = evalt(min_and_max[i][k][1], min_and_max[k+1][j][1], op[k])
        c = evalt(min_and_max[i][k][1], min_and_max[k+1][j][0], op[k])
        d = evalt(min_and_max[i][k][0], min_and_max[k+1][j][1], op[k])
        if min_and_max[i][j][0] is None or max(a, b, c, d) > min_and_max[i][j][0]:
            min_and_max[i][j] = (max(a, b, c, d), min_and_max[i][j][1])
        if min_and_max[i][j][1] is None or min(a, b, c, d) < min_and_max[i][j][1]:
            min_and_max[i][j] = (min_and_max[i][j][0], min(a, b, c, d))
    return


if __name__ == "__main__":
    print(get_maximum_value(input()))