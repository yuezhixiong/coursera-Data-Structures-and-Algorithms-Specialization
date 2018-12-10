#Uses python3

import sys

def get_max_number(arr_a):
    max_number = arr_a[0]
    for x in arr_a:
        if(int(str(x) + str(max_number)) > int(str(max_number) + str(x))):
            max_number = x
    return max_number

def largest_number(a):
    res = ""
    while len(a) > 0:
        largest_number = get_max_number(a)
        res += str(largest_number)
        a.remove(largest_number)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
