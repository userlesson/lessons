arr = {}

for num in range(10, -6, -1):
    arr[num] = num ** num

for key, value in arr.items():
    print(f"{key}: {value}")