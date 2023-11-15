from food import Food

class Spaghetti(Food):
    def __str__(self):
        return f"Spaghetti(weight={self.weight}, cost={self.cost})"
