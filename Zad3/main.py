class Property:
    @property
    def area(self):
        return self.area()

    def rooms(self) -> int:
        return self.rooms()

    def price(self):
        return self.price()

    def address(self):
        return self.address()

    @area.setter
    def area(self, value: str):
        self.area = value

    @rooms.setter
    def rooms(self, value: int) -> int:
        self.rooms = value

    @price.setter
    def price(self, value: str):
        self.price = value

    @address.setter
    def address(self, value: str):
        self.address = value


class House(Property):
    @property
    def plot(self):
        return self.plot()

    @plot.setter
    def plot(self, value: int) -> int:
        self.plot = value


class Flat(Property):
    @property
    def floor(self):
        return self.floor()

    @floor.setter
    def floor(self, value):
        self.floor = value
