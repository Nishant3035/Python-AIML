class Product:
    count = 0
    def __init__(self,name,price):
        self.name = name
        self.price = price
        Product.count+=1

    def get_info(self):
        print(f"Your product name is {self.name} and price is {self.price}")

    @classmethod
    def get_count(cls):
        print(f"Total count is {cls.count}")    

    @staticmethod
    def cal_discount(price,discount):
        print(f"Final price = {price - (price*discount/100)}")



p1 = Product("Laptop",45000)
p2 = Product("Mobile",20000)
p3 = Product("camera",1000)

p1.get_info()

Product.get_count()
p1.cal_discount(p3.price,12)