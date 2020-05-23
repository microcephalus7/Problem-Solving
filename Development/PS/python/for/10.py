import sys

num = int(sys.stdin.readline())
string = ""

for i in range(1, num + 1):
    for z in range(num + 1 - i, 1):
        string += " "
    for o in range(1):
        string += "*"
    print(string)
