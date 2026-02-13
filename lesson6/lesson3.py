A = int(input())
B = int(input())

if A % 2 != 0:
    A += 1

for i in range(A, B + 1, 2):
    print(i, end=" ")