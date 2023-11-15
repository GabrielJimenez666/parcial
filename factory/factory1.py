from factory.factory import Factory
from appliance.fridge import Fridge
from food.beef import Beef

class Factory1(Factory):
    def make_appliance(self, model_number, consumption):
        return Fridge(model_number, consumption)

    def make_food(self, weight, cost):
        return Beef(weight, cost)
