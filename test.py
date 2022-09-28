
my_list = [{"name": "Mazda", "engine": "2.8", "color": "Red", "id": 1}, {"name": "BMW", "engine": "1.3", "color": "Yellow", "id": 2}, {"name": "Lada", "engine": "1.6", "color": "pink", "id": 3}]

print(my_list)

for car in my_list:
    temp = car.get('id')
    if temp == 2:
        car['color'] = 'red'

print(my_list)