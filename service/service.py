from factory.factory1 import Factory1
from factory.factory2 import Factory2

class Service:
    def __init__(self, max_clients):
        self.max_clients = max_clients
        self.clients = []

    def add_client(self, client):
        if len(self.clients) < self.max_clients:
            self.clients.append(client)
            print(f"Client {client.id} added to Service")
        else:
            print("Client limit reached, unable to add new Client")

    def factories_summary(self):
        # Cuenta el número de clientes asociados a cada fábrica
        factory1_clients = sum(1 for client in self.clients if isinstance(client.factory, Factory1))
        factory2_clients = sum(1 for client in self.clients if isinstance(client.factory, Factory2))
        print("\nFactories Summary:\n")
        print(f"- Clients using Factory 1 = {factory1_clients}")
        print(f"- Clients using Factory 2 = {factory2_clients}\n")
        # Imprime qué fábrica utiliza cada cliente
        for client in self.clients:
            factory_type = '1' if isinstance(client.factory, Factory1) else '2'
            print(f"- Client {client.id} uses Factory {factory_type}")

    def client_most_expensive_food(self):
        # Encuentra el alimento más caro entre todos los clientes
        most_expensive_food = max(self.clients, key=lambda c: c.food.cost)
        return most_expensive_food.id, type(most_expensive_food.food).__name__, most_expensive_food.food.cost
