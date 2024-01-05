# +와 ,
a="파이썬"
print(a, "아 반가워")
print("a"+"아 반가워")
msg=a+"아 반가워"
print(msg)

# 
a="파이썬"
print("%s아 반가워"%a)
print(a, "아 반가워")
msg=a+"아 반가워"
print(msg)

# 소수점 자릿수 맞추기 : f
a=24; b=21; c=(a+b)/2
print(c)
print("%d"%c)
print("%4d"%c) # 4자리 정수, 채워지지 않을 시에 맨 앞 공백으로 들여쓰기를 통해 자릿수를 채움
print("%f"%c)
print("%3.1f"%c) # 3자리(. 포함), 소수점 1자리;
print("%6.2f"%c) # 6자리(. 포함), 소수점 2자리, 공백은 맨 앞에 들여쓰기

# 출력서식 format
name = "홍길동"
age = 20.5
# 출력문 : 이름은 홍길동이고 나이는 20.50 살이다
print("이름은 {}이고 나이는 {}입니다".format(name,age))
print("이름은 {:10s}이고 나이는 {:.2f}입니다".format(name,age))