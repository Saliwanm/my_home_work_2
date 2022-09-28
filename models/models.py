import json

class Toyota:
    file = 'cars.json'

    def __init__(self, name, engine, color, gear):
        self.name = name
        self.engine = engine
        self.color = color
        self.gear = gear

    def drive(self):
        print(self.name + ' driving ')

    @classmethod
    def get_data(cls):
        file = open('database/' + cls.file, 'r')
        data_in_json = file.read()
        data = json.loads(data_in_json)
        file.close()
        return data

    @classmethod
    def get_all_cars(cls):
        data = cls.get_data()
        for car in data:
            print(str(car['id']) + ") Our " + car['name'] + " has " + car['engine'] + " motor " + car['color'] + " color and has " + car['gear'] + " gears")

    @classmethod
    def get_by_id(cls, id):
        data = cls.get_data()
        count = 0
        for car in data:
            if id == car['id']:
                print("Your car is " + car['name'] + ", she has " + car['engine'] + " motor " + car['color'] + " color and has " + car['gear'] + " gears")
                break
            count += 1
            if count == len(data):
                print('Not found car with this number')

    @classmethod
    def change_color(cls, id):
        data = cls.get_data()
        count = 0
        for car in data:
            if id == car['id']:
                color = input('What color do you want? ')
                print('Okey, just a moment...')
                for change_car in data:
                    temp = change_car.get('id')
                    if temp == id:
                        change_car['color'] = color
                print('Everything allright, we change color in your car')
                file = open('database/' + cls.file, 'w')
                data_in_json = json.dumps(data)
                file.write(data_in_json)
                file.close()
                break
            count += 1
            if count == len(data):
                print('Sorry, but not found car with this number!')
    @classmethod
    def shift_gear(cls, id):
        data = cls.get_data()
        count = 0
        for car in data:
            if id == car['id']:
                gear = 0
                while gear == 0 or gear > int(car['gear']):
                    gear = int(input('Choose gear to drive: '))
                    if gear > int(car['gear']):
                        print('Your car do not has ' + str(gear) + ' gears')
                    elif gear == 0:
                        print('Sorry, but you got nowhere')
                print('Okey, you start drive...')
                while 0 < gear and gear <= int(car['gear']):
                    print('You enter ' + str(gear) + ' gear and go...')
                    gear = int(input('What next gear do you want: '))
                if gear == 0:
                    print('You stopped')
                else:
                    print('Your car is crashed! Sory.')
                break
            count += 1
            if count == len(data):
                print('Sorry, but not found car with this number!')

    def save(self):
        data = self.get_data()
        new_car = {'name': self.name, 'engine': self.engine, 'color': self.color, 'gear': self.gear}
        if len(data) == 0:
            new_car['id'] = 1
        else:
            new_car['id'] = data[-1]['id'] + 1
        data.append(new_car)
        file = open('database/' + self.file, 'w')
        data_in_json = json.dumps(data)
        file.write(data_in_json)
        file.close()
