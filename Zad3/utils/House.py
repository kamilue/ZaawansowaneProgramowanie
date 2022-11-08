from utils.Property import Property


class House(Property):
    @property
    def plot(self):
        return self.plot()

    @plot.setter
    def plot(self, value: int) -> int:
        self.plot = value

    def __str__(self):
        return f'Dom posiada rozmiar dzialki {self.plot}'
