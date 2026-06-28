class Product:
    count = 0
    def __init__(self,name,price):
        self.name = name
        self.price = price
        Product.count+=1
    def get_info(self):
        print(f"Price of {self.name} is {self.price}")

    @classmethod
    def get_count(cls):
        print(f"Total Object created is {cls.count}")
    @staticmethod
    def discount(price,discount_percent):
        print(f"Total price after discount is {price -(price*discount_percent/100)}")

p1 = Product("laptop",50000)
p2 = Product("Mobile",10000)
p3 = Product("Pen",100)

p3.get_info()

Product.get_count()

p1.discount(50000,30)
