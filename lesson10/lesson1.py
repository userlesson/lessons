
def get_age(age):
    if 11 <= age % 100 <= 19:
        return "лет"
    elif age % 10 == 1:
        return "год"
    elif 2 <= age % 10 <= 4:
        return "года"
    else:
        return "лет"

pets = {}

name = input("Введите имя питомца: ")
animal_type = input("Введите вид питомца: ")
age = int(input("Введите возраст питомца: "))
owner = input("Введите имя владельца: ")

pets[name] = {
    'Вид питомца': animal_type,
    'Возраст питомца': age,
    'Имя владельца': owner
}

for pet_name, pet_info in pets.items():
    animal_type = pet_info['Вид питомца']
    age = pet_info['Возраст питомца']
    age_wit = f"{age} {get_age(age)}"
    owner = pet_info['Имя владельца']
    
    res = f"Это {animal_type} по кличке \"{pet_name}\". Возраст питомца: {age_wit}. Имя владельца: {owner}"
    print(res)