# Uses python3
import sys


# denominations 1, 3, 4

def DpChange(money, coins):
    MinNumCoins = [0]   # Money 0: 0
    for m in range(money):  # m: 0~money - 1
        MinNumCoins.append(1000000)
        for i in range(len(coins)):
            if (m + 1) >= coins[i]:
                NumCoins = MinNumCoins[m + 1 - coins[i]] + 1
                if NumCoins < MinNumCoins[m + 1]:
                    MinNumCoins[m + 1] = NumCoins
    return MinNumCoins[money]


if __name__ == '__main__':
    # read money
    money = [int(x) for x in input().split()][0]
    print(DpChange(money, [1, 3, 4]))