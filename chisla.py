user_input = input("Введите число: ")
# Проверяем, является ли введенное значение числом
if user_input.lstrip('-').isdigit():
    number = int(user_input)
    if number > 0:
        if number % 2 == 0:
            print(f"Число {number} является четным")
        else:
            print(f"Число {number} не является четным")
    else:
        print("Ошибка: введено не положительное число")
else:
    print("Ошибка: введено не число")