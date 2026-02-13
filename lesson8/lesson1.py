print("Введите размер массива")
N = int(input())

arr = []

for i in range(N):
    print(f"Значение {i}:")
    num = int(input())
    arr.append(num)

arr.reverse()

for num in arr:
    print(num)