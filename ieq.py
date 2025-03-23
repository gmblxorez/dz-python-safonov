name = input("Ваше имя: ")
surname = input("Фамилия: ")
age = input("Возраст: ")
# Реализация через метод format()
output_format = "Ваше имя: {}, Фамилия: {}, Возраст: {} лет".format(name, surname, age)
print(output_format)
# Реализация через f-string
output_fstring = f"Ваше имя: {name}, Фамилия: {surname}, Возраст: {age} лет"
print(output_fstring)