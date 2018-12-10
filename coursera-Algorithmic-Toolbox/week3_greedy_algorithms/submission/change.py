# Uses python3
import sys

def get_change(value):
    #write your code here
    p, n, d = 1, 5, 10
    count = 0
    while value > 0:
        if value >= d:
            count += value // d
            value %= d
        elif value >= n:
            count += value // n
            value %= n
        else:
            count += value // p
            break
    return count

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
