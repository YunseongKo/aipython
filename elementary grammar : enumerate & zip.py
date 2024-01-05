# enumerate는 리스트를, zip은 튜플을 반환한다
# enumerate
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)

# 2-1 답안
str = ['a','b','c']
for index, alphabet in enumerate(str):
    print(index, alphabet)

# 2-2 답안 : range 활용
Input = ['a', 'b', 'c']
for i in range(len(Input)):
    print("fruit{} name is {}".format(i, Input[i]))
# 01) Input = ['a', 'b', 'c']:
#     Input이라는 이름의 변수에 리스트 ['a', 'b', 'c']를 할당합니다. 이 리스트에는 세 개의 문자열 요소 'a', 'b', 'c'가 순서대로 들어 있습니다.
#     for i in range(len(Input))::
#     for는 반복문을 시작하는 키워드입니다.
#     i는 반복문에서 사용되는 인덱스 변수로, 각 반복(iteration)마다 다른 값을 가집니다.
#     range() 함수는 연속된 숫자를 생성하는데 사용됩니다. 여기서 len(Input)은 Input 리스트의 길이를 반환하므로, range(len(Input))는 0부터 len(Input) - 1까지의 연속된 숫자를 생성합니다. Input 리스트의 길이가 3이므로, range(3)은 0, 1, 2라는 세 개의 숫자를 생성합니다.
#     결론적으로, 이 라인은 i가 0에서 시작하여 Input 리스트의 길이보다 하나 작은 값까지 (len(Input) - 1, 여기서는 2) 증가하면서 루프를 실행합니다. 각 반복에서 i는 0, 1, 2의 값을 갖게 됩니다.
# 02) print("fruit{} name is {}".format(i, Input[i])):
#     print() 함수는 괄호 안의 내용을 출력합니다.
#     "fruit{} name is {}"는 출력할 문자열의 형식을 지정합니다. 여기서 {}는 format 메서드에 의해 대체될 부분을 나타냅니다.
#     .format(i, Input[i])는 문자열 내의 {}를 format 함수에 전달된 인자들로 대체합니다. 첫 번째 {}는 인덱스 i의 값으로, 두 번째 {}는 Input 리스트의 i번째 요소로 대체됩니다.
#     각 반복에서, 이 라인은 "fruit0 name is a", "fruit1 name is b", "fruit2 name is c"와 같이 인덱스와 해당 인덱스에 위치한 Input 리스트의 요소를 포함한 문자열을 출력합니다.
# 이 코드는 리스트 Input의 각 요소에 대해 "fruit인덱스 name is 요소값" 형식의 문자열을 출력합니다.



# zip : 3개 이상도 묶을 수 있다
names = ['John', 'Jane', 'Doe']
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")
# zip(names, ages)는 names의 첫 번째 요소와 ages의 첫 번째 요소를 튜플로 묶어 반환합니다. 즉, 첫 번째 반복에서는 ('John', 25)를 반환합니다.
# for 루프는 이 튜플을 받아서 name에는 'John'을, age에는 25를 할당합니다.
# print(f"{name} is {age} years old.")는 이 값을 사용하여 문자열을 형식화하고 출력합니다. 결과는 "John is 25 years old."입니다.
# 루프는 다음 튜플로 이동합니다. zip 함수는 names의 두 번째 요소와 ages의 두 번째 요소를 튜플로 묶어 반환합니다. 즉, 두 번째 반복에서는 ('Jane', 30)를 반환합니다.
# 이 과정은 names와 ages 리스트에 있는 모든 요소가 순차적으로 짝지어질 때까지 계속됩니다.
# 코드 실행이 완료되면, names와 ages 리스트에 있는 모든 이름과 나이가 다음과 같이 출력됩니다:
    
# Quiz
name = [ "M","N","S","A" ]
roll_no = [4,1,3,2]
pairs = set()
for nam, roll in zip(name, roll_no):
    pairs.append(zip)
print(f"'{nam}', {roll}")