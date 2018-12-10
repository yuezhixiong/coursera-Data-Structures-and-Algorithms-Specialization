# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def fast(n):
    if (n <= 1):
        return n
    a, b = 0, 1
    for _ in range(n-1):
        c = a + b
        a, b = b, c
    return c

n = int(input())
print(fast(n))
