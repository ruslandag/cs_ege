class Phone:
    def __init__(self,brand,version, capacity, price):
        self._brand = brand
        self._version = version
        self._capacity = capacity
        self._price = price

    def __str__(self):
        return f'Brand: {self._brand}\nModel: {self._version}\n' + \
            f'Memory Capacity: {self._capacity}\nPrice: {self._price} рублей'