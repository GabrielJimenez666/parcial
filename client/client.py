from factory.factory1 import Factory1
from factory.factory2 import Factory2

class Client:
    _id_counter = 1

    def __init__(self, factory_type, model_number, consumption, weight, cost):
        self.id = Client._id_counter
        Client._id_counter += 1
        self.factory = Factory1() if factory_type == 1 else Factory2()
        self.appliance = self.factory.make_appliance(model_number, consumption)
        self.food = self.factory.make_food(weight, cost)

    def __str__(self):
        return f"Client {self.id}: {self.appliance}, {self.food}"
