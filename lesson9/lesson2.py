num1 = input().split()
num2 = input().split()

set1 = set(map(int, num2))
set2 = set(map(int, num2))

res = set1.intersection(set2)

print(len(res))