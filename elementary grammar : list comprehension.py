# squares = [x**2 for x in range(5)]
# print(squares)

# new_list = [expression for item in iterable if condition]

# if squares % 2 == :
#     print(squares)
# else:


# Quiz 1
squares = [x**2 for x in range(1,6)]
print (squares)


# Quiz 2
countries = ["Seoul", "New York", "London", "Shanghai", "Paris", "Tokyo"]
# 철자에 S를 포함하는 도시를 추출

# 답 1
countries = ["Seoul", "New York", "London", "Shanghai", "Paris", "Tokyo"]
cities_with_S = [city for city in countries if 'S' in city]
print(cities_with_S)

# 답 2
countries = ["Seoul", "New York", "London", "Shanghai", "Paris", "Tokyo"]
countries_with_S = []
for city in countries:
    if  'S' in city:
        countries_with_S.append(city)
print(countries_with_S)