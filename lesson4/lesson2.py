number = int(input("Введите число: "))

ten_thousands = number // 10000
thousands = (number // 1000) % 10
hundreds = (number // 100) % 10
tens = (number // 10) % 10
units = number % 10

power_res = tens ** units

multiply_result = power_res * hundreds

difference = ten_thousands - thousands

res = multiply_result / difference

print("Результат: ", res)