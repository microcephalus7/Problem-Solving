import sys

num = int(sys.stdin.readline())

for i in range(num):
    a, b = list(map(int, sys.stdin.readline().split()))

    print(a+b)
