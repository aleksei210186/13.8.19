tickets = int(input('Сколько билетов Вы хотите приобрести?'))
price = 0
for i in range(tickets):
    age = int(input('Введите возраст посетителя(целое число):'))
    if age < 18:
        price += 0
    elif 18 <= age < 25:
        price += 990
    else:
        price += 1390
if tickets > 3:
    price -= ((price/100)*10)
print('Итого:', round(price), 'рублей.')
