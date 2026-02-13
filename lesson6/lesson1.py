N = int(input("Введите количество чисел: "))

count_zero = 0

for i in range(N):
    num = int(input())
    if num == 0:
        count_zero += 1

print(count_zero)