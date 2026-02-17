print("Введите размер списка")
N = int(input())

arr = list(map(int, input().split()))

if len(arr) > N:
    print("Размер списка превышает указанный")
else:
    res = [arr[-1]] + arr[:-1]
    print(res)