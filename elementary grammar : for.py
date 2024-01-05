# 세로로 리스트 내 변수를 나열
a = [1, 2, 3, 4, 5]
for i in a:
    print(i)

# end를 응용한 가로로 적기
a = [1, 2, 3, 4, 5]
for i in a:
    print(i,end="")

# range 이용 (start, stop, step) : 5회 반복
for i in range(1, 10, 2):
    print(i)

# range 안에 숫자 하나만 적으면 0에서 시작하고 간격은 1로 고정되며 (적은 숫자 -1)에서 끝남
for n in range(10):
    print(n)

# 문자열의 반복
for x in '월화수':
    print(x)