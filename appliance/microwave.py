from appliance import Appliance

class Microwave(Appliance):
    def __str__(self):
        return f"Microwave(model_number={self.model_number}, consumption='{self.consumption}')"
