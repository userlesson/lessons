def factorial(n):
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

num = int(input("Введите натуральное число: "))

fctr_num = factorial(num)
print(f"Факториал числа {num} = {fctr_num}")

fctr_list = []
for i in range(fctr_num, 0, -1):
    fctr_list.append(factorial(i))

print(f"Список факториалов: {fctr_list}")