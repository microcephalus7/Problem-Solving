import sys

num = int(sys.stdin.readline())
string = ""
for i in range(1, num + 1):
    for o in range(1):
        string += "*"
    print(string)
