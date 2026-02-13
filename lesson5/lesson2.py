word = input("Введите слово: ").lower()

letters_count = 0
sogl_count = 0

a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0

for char in word:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        letters_count += 1
        if char == 'a':
            a_count += 1
        elif char == 'e':
            e_count += 1
        elif char == 'i':
            i_count += 1
        elif char == 'o':
            o_count += 1
        elif char == 'u':
            u_count += 1
    elif 'a' <= char <= 'z':
        sogl_count += 1

print("Гласных:", letters_count)
print("Согласных:", sogl_count)
print()

print("a:", a_count if a_count > 0 else False)
print("e:", e_count if e_count > 0 else False)
print("i:", i_count if i_count > 0 else False)
print("o:", o_count if o_count > 0 else False)
print("u:", u_count if u_count > 0 else False)