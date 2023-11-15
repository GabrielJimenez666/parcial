from food import Food

class Beef(Food):
    def __str__(self):
        return f"Beef(weight={self.weight}, cost={self.cost})"
