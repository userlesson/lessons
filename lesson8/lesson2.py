N = int(input())

arr = list(map(int, input().split()))

res = [arr[-1]] + arr[:-1]

print(res)