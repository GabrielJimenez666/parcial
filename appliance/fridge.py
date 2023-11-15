from appliance import Appliance

class Fridge(Appliance):
    def __str__(self):
        return f"Fridge(model_number={self.model_number}, consumption='{self.consumption}')"
