name = input("Напишіть своє ім'я: ")
Lastname = input("Напиши своє призвище:")
status = input("Хто ви по статусу: ")
age = int(input("Скільки тобі років:"))
if name == "Андрій":
    print(name)
else:
    print("Error")

if Lastname == "Кохан":
    print(Lastname)
else:
    print("Error")

if status == "Інженер":
    print(status)
else:
    print("Error")

if age < 18:
    print("0 rank")
elif age == 18:
    print("1 rank")
elif age > 18:
    print("2 rank")
else:
    print("Error")