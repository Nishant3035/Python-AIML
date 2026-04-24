class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}")


class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

    def display(self):
        super().display()
        print(f"Seats: {self.seats}")


# Creating objects
v1 = Vehicle("Audi", "XE")
c1 = Car("BMW", "X5", 5)

# Calling methods
v1.display()
c1.display()