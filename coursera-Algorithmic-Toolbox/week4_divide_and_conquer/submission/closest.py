# Uses python3
import sys
import math


def naive(x, y):
    dist = 1e15
    for k in range(len(x)):
        for l in range(k+1, len(x)):
            dx = x[k]-x[l]
            dy = y[k]-y[l]
            d = dx*dx + dy*dy
            if d < dist:
                dist = d
    return math.sqrt(dist)


def distFunc(p1, p2):
    dx, dy = p1[0]-p2[0], p1[1]-p2[1]
    return math.sqrt(dx*dx+dy*dy)


def crossDist(points, mdist, left, mid, right):
    l = mid
    while((l >= left) and ((points[mid][0]-points[l][0]) < mdist)):
        r = mid+1
        while((r <= right) and ((points[r][0]-points[mid][0]) < mdist)):
            #d = distFunc(points[l],points[r])
            dx, dy = points[l][0]-points[r][0], points[l][1]-points[r][1]
            d = math.sqrt(dx*dx+dy*dy)
            if d < mdist:
                mdist = d
            r += 1
        l -= 1
    return mdist


def minDist(points, left, right):
    if left+1 == right:  # 2 points
        return distFunc(points[left], points[right])
    mid = left+int((right-left)/2)
    ld = minDist(points, left, mid)
    rd = minDist(points, mid+1, right)

    return crossDist(points, min(ld, rd), left, mid, right)


def calcVar(arr):
    mean = sum(arr)/len(arr)
    return sum([(x-mean)**2 for x in arr])


def minimum_distance(x, y):
    if len(x) == 1:
        return 0
    #points = sorted([t for t in zip(x,y)])
    if calcVar(x) > calcVar(y):
        points = sorted([t for t in zip(x, y)])
    else:
        points = sorted([t for t in zip(y, x)])
    return minDist(points, 0, len(points)-1)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
