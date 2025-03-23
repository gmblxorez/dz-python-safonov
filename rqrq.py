while True:
    user_input = input("Введите число: ")
    if user_input.lower() == 'exit':
        print("Программа завершена.")
        break
    if user_input.lstrip('-').isdigit():
        num_length = len(user_input.lstrip('-'))
        print(f"В этом числе {num_length} цифры.")
    else:
        print("Ошибка: данные не являются числом.")