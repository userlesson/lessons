print("Максимальная грузоподъемность лодки:")
m = int(input())

print("Количество рыбаков")
n = int(input())


print("Вес каждого рыбака")

weight = [int(input()) for _ in range(n)]

weight.sort()

boat = 0
i = 0
j = n - 1

while i <= j:
    if i == j:
        boat += 1
        break
    elif weight[i] + weight[j] <= m:
        i += 1
        j -= 1
    else:
        j -= 1
    boat += 1

print(f"Необходимо лодок: {boat}")