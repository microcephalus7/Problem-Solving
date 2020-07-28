import sys

input()  # 인풋함수 선언으로 input 기능 활성화
s = list(sum(map(int, n.split()))
         for n in sys.stdin)  # list 컴프리헨션으로 n 변수 활성화 및 합계값 list

for i in range(0, len(s+1)):
    print("Case #%d: %d" % (i+1, s[i]))
