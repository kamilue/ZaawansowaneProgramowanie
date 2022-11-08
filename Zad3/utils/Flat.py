from utils.Property import Property


class Flat(Property):
    @property
    def floor(self):
        return self.floor()

    @floor.setter
    def floor(self, value):
        self.floor = value

    def __str__(self):
        return f'Mieszkanie znajduje się na {self.floor} piętrze'
