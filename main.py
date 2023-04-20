tickets = int(input("Введите количество билетов: "))
total = 0

for ticket in range(tickets):
    age = int(input(f"Введите возраст посетителя {ticket+1}-го билета: "))
    if age < 18:
        price = 0
    elif age >= 18 and age <= 25:
        price = 990
    else:
        price = 1390
    total += price

if tickets > 3:
    total *= 0.9

print(f"Общая стоимость билетов: {total} руб.")