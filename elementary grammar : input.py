# # 변수 선언 및 초기화
# number = 10

# # 변수 값 변경
# number = 20

# # 변수를 사용한 계산
# result = number * 2

# # 변수 값 출력
# print(result)

# a='3'
# b=int(a)
# print(type(a), a)


# # Quiz
# a=input("당신의 나이는?")
# print(a, "살이군요")
# print("내년엔" + "a+1" + "살이 되네요")
# print(type(a))

# Solution 1
a=input("당신의 나이는?")
b=int(a)
print(a, "살 이군요.")
print("내년엔", b+1, "살이 되네요")
print(type(b))

# Solution 2
a=input("당신의 나이는?")
print(a, "살 이군요.")
print("내년엔", int(a)+1, "살이 되네요")
print(type(b))

# Solution 3
a=int(input("당신의 나이는?"))
print(a, "살 이군요.")
print("내년엔", a+1, "살이 되네요")
print(type(b))


# Quiz 2
a=int(input("당신의 나이는?"))
msg=a+"살 이군요"
print(msg)
print("내년엔",a+1,"살이 되네요")
print(type(a))

# Soultion 1
a=int(input("당신의 나이는?"))
msg="a"+"살 이군요"
print(msg)
print("내년엔",a+1,"살이 되네요")
print(type(a))

# Soultion 2
a=input("당신의 나이는?")
msg=a+"살 이군요"
print(msg)
print("내년엔",int(a)+1,"살이 되네요")
print(type(a))