import json

class Toyota:
    file = 'cars.json'

    def __init__(self, name, engine, color):
        self.name = name
        self.engine = engine
        self.color = color

    # def change_color(self, new_color):
    #     self.color = new_color

    def drive(self):
        print(self.name + ' driving ')

    def shift_gear(self):
        print(self.name + ' shift gear ')

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
            print(str(car['id']) + ") Our " + car['name'] + " has " + car['engine'] + " motor and " + car['color'] + " color.")

    @classmethod
    def get_by_id(cls, id):
        data = cls.get_data()
        count = 0
        for car in data:
            if id == car['id']:
                print("Your car is " + car['name'] + ", she has " + car['engine'] + " motor and " + car['color'] + " color")
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

    def save(self):
        data = self.get_data()
        new_car = {'name': self.name, 'engine': self.engine, 'color': self.color}
        if len(data) == 0:
            new_car['id'] = 1
        else:
            new_car['id'] = data[-1]['id'] + 1
        data.append(new_car)
        file = open('database/' + self.file, 'w')
        data_in_json = json.dumps(data)
        file.write(data_in_json)
        file.close()
