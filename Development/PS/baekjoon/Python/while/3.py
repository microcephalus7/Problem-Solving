# 이 풀이는 n이 10 이하일 경우에도 단순히 1의 자리가 10의 자리로 간다는 걸 생각 못 함. 규칙성 에 더 집중하고 단순화 시키지 못 함.
n = num = int(input())  # 변수 지정
count = 0  # count 설정
while True:
    ten = n // 10  # 연산자
    one = n % 10  # 연산자
    total = ten+one
    count += 1
    n = int(str(one)+str(total % 10))
    if(num == n):
        break  # 나가기 설정
print(count)