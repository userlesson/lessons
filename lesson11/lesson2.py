import collections

# БД
pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        }
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        }
    }
}

def get_age(age):
    if 11 <= age % 100 <= 19:
        return "лет"
    elif age % 10 == 1:
        return "год"
    elif 2 <= age % 10 <= 4:
        return "года"
    else:
        return "лет"

def get_pet(ID):
    return pets[ID] if ID in pets else False

# Добавляем питомца
def create():
    last = collections.deque(pets, maxlen=1)[0] if pets else 0
    new_id = last + 1
    
    print("Добавление питомца")
    name = input("Имя: ")
    species = input("Вид: ")
    age = int(input("Возраст: "))
    owner = input("Владелец: ")
    
    pets[new_id] = {name: {
        "Вид питомца": species,
        "Возраст питомца": age,
        "Имя владельца": owner
    }}
    print(f"Питомец добавлен с ID: {new_id}")

# Показать данные
def read():
    ID = int(input("Введите ID питомца: "))
    pet = get_pet(ID)
    
    if pet:
        for name, data in pet.items():
            suffix = get_age(data["Возраст питомца"])
            print(f'Это {data["Вид питомца"]} по кличке "{name}". '
                  f'Возраст питомца: {data["Возраст питомца"]} {suffix}. '
                  f'Имя владельца: {data["Имя владельца"]}')
    else:
        print(f"Питомец с ID {ID} не найден")

# Обновление данных о питомце
def update():
    ID = int(input("Введите ID питомца для обновления: "))
    pet = get_pet(ID)
    
    if pet:
        for name, data in pet.items():
            print("Оставьте поле пустым, если не хотите менять")
            new_name = input(f"Имя ({name}): ") or name
            new_species = input(f"Вид ({data['Вид питомца']}): ") or data['Вид питомца']
            
            age_input = input(f"Возраст ({data['Возраст питомца']}): ")
            new_age = int(age_input) if age_input else data['Возраст питомца']
            
            new_owner = input(f"Владелец ({data['Имя владельца']}): ") or data['Имя владельца']
            
            del pets[ID]
            pets[ID] = {new_name: {
                "Вид питомца": new_species,
                "Возраст питомца": new_age,
                "Имя владельца": new_owner
            }}
            print("Информация обновлена")
    else:
        print(f"Питомец с ID {ID} не найден")

# Удаление питомца
def delete():
    ID = int(input("Введите ID питомца для удаления: "))
    if ID in pets:
        del pets[ID]
        print("Питомец удален")
    else:
        print(f"Питомец с ID {ID} не найден")

# Показать список питомнец
def show_all():
    if not pets:
        print("Список пуст")
        return
    
    for ID, pet in pets.items():
        for name, data in pet.items():
            suffix = get_age(data["Возраст питомца"])
            print(f"ID: {ID}")
            print(f'Это {data["Вид питомца"]} по кличке "{name}". '
                  f'Возраст: {data["Возраст питомца"]} {suffix}. '
                  f'Владелец: {data["Имя владельца"]}')

def main():
    commands = {
        "create": create,
        "read": read,
        "update": update,
        "delete": delete,
        "list": show_all,
        "stop": None
    }
    
    print("Команды: create, read, update, delete, list, stop")
    
    while True:
        cmd = input("\nВведите команду: ").lower().strip()
        
        if cmd == "stop":
            break
        elif cmd in commands:
            commands[cmd]()
        else:
            print("Неизвестная команда")

if __name__ == "__main__":
    main()