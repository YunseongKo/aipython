# Remark) split과 Join은 서로의 역과정이다

# split : 구분되는 문자를 기준으로 잘라 리스트로 만들어서 반환하는 역할을 수행
data = "John,30,Engineer\nAlice,25,Designer\nBob,22,Artist"
lines = data.split("\n")

for line in lines:
    fields = line.split(",")
    print("Name:", fields[0], "Age:", fields[1], "Occupation:", fields[2])

# join : 리스트로 주어진 문자열을 하나로 결합할 때 사용
words = ['Hello', 'world', 'this', 'is', 'a', 'test']
sentence = ' '.join(words)
print(sentence)

# Quiz 1
# 내 답
str = "Geeks for Geeks"
for line in str:
    fields = str.split(" ")
print(fields)

# gpt
str = "Geeks for Geeks"
fields = str.split(" ")
print(fields)

# Quiz 2
# 내 답
list = ['Geeks', 'for', 'Geeks']
answer = "-".join(list)
print(answer)