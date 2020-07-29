import sys

a, b = map(int, sys.stdin.readline().split())
score = [x for x in input().split() if int(x) < b]
print(' '.join(score))
