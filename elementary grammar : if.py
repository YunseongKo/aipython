# # a의 대소관계 비교
# a = input("a의 값을 적어주세요: ")
# if a > 5:
#     print("a는 5보다 큽니다")
#     print("end")
# else:
#     print("a는 5보다 작거나 같다")

# 성별 결정
gender = input("당신의 성별을 기입해주세요: " )
if gender == "Male":
    print("오른쪽으로 입장하세요.")
elif gender == "Female":
    print("왼쪽으로 입장해주세요.")
else:
    print("나가주세요.")

# 만약 같은 세로줄에 if를 여러개 쓰면 위에서 if의 조건을 만족해도 모든 if문을 실행한다 -> 비효율적인 구조
    
# 점수
absent = int(input("결석 횟수를 입력해주세요: "))
score = float(input("성적을 기입해주세요: "))
if absent < 5:
    if score >= 90:
        print("성적 : A")
    elif 90 >= score > 70:
        print("성적 : B")
    elif 70 >= score > 50:
        print("성적 : C")
    else:
        print("성적 : D")
else:
    print("성적 : F")

# 수의 범위
a = int(input("숫자를 적어주세요: "))
b = int(input("숫자를 적어주세요: "))
if a > 3:
    if b < 10:
        print("a는 3보다 크고 b는 10보다 작다")
# and문 활용
a = int(input("숫자를 적어주세요: "))
b = int(input("숫자를 적어주세요: "))
if a > 3 and b < 10:
    print("a는 3보다 크고 b는 10보다 작다")


# 사용자로부터 시험 점수를 입력받습니다.
score = int(input("시험 점수를 입력해주세요: "))

# 점수 범위에 따라 조건을 검사하고 해당하는 학점을 출력합니다.
if 90 <= score <= 100:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 70 <= score < 80:
    print("C")
elif 60 <= score < 70:
    print("D")
else:
    print("F")