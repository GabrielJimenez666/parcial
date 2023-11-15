class Food:
    def __init__(self, weight, cost):
        self.weight = weight
        self.cost = cost

    def __str__(self):
        return f"{self.__class__.__name__}(weight={self.weight}, cost={self.cost})"
