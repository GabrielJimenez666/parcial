from .factory import Factory
from appliance.microwave import Microwave
from food.spaghetti import Spaghetti

class Factory2(Factory):
    def make_appliance(self, model_number, consumption):
        return Microwave(model_number, consumption)

    def make_food(self, weight, cost):
        return Spaghetti(weight, cost)
