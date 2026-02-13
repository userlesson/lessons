X = int(input())

count = 0

i = 1
while i * i <= X:
    if X % i == 0:
        count += 2 
    i += 1

i -= 1
if i * i == X:
    count -= 1

print(count)