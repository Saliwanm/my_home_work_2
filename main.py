from models.models import Toyota

while True:
    print("Hello, we have a car's plane. Do you want to create a new car?\n" +
          '1. Add new car\n' +
          '2. Get all cars\n' +
          '3. Get car from Id\n' +
          '4. Change color'
          )

    flag = int(input('Choose menu item: '))

    if flag == 1:
        name = input("Cars name: ")
        engine = input("Car's engin: ")
        color = input("Car's color: ")
        car = Toyota(name, engine, color)
        car.save()
    elif flag == 2:
        Toyota.get_all_cars()
    elif flag == 3:
        id = int(input('Type id: '))
        Toyota.get_by_id(id)
    elif flag == 4:
        print('Which one do you want to repaint?')
        Toyota.get_all_cars()
        id = int(input('Choose number of car: '))
        Toyota.change_color(id)