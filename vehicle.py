class Vehicle:
    def __init__(self, engine_number, chassis_number, regn_no):
        self.engine_number = engine_number
        self.chassis_number = chassis_number
        self.regn_no = regn_no

    def display(self):
        print("display; Vehicle")


class Truck(Vehicle):
    def __init__(self, engine_number):
        self.engine_number = engine_number
        self.chassis_number = chassis_number
        self.regn_no = regn_no
        self.num_wheels = num_wheels


    def display(self):
        super(Truck, self).display()
        print("display: Truck")


engine_number = '1az'
chassis_number = '123'
regn_no = 'ka-04-ma-1111'
num_wheels = 4
truck = Truck(engine_number)
truck.display()
print(truck.engine_number,truck.chassis_number,truck.regn_no)