# 해설 1 : if문을 활용
A,B,C=map(int,input().split())
if B<A<C and C<A<B:
    print(A)
elif A<B<C and C<B<A:
    print(B)
else:
    print(C)

# 해설 2 : 오름차순
A,B,C=map(int,input().split())
numbers = [A, B, C] # list, 객체라는 개념을 내포하고 있다
numbers.sort()
print(numbers[-2])

# 해설 3 : 내림차순
A,B,C=map(int,input().split())
numbers = [A, B, C] # list, 객체라는 개념을 내포하고 있다
numbers.sort(reverse=True)
print(numbers[1])