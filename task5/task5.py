class Temperature:

    def __init__(self, temp: float, type: str):
        self.temp = temp
        self.type = type

    def celsius(self):
        if self.type == 'K':
            self.temp = self.temp - 273.15
            self.type = 'C'
        elif self.type == 'F':
            self.temp = (self.temp - 32) * 5 / 9
            self.type = 'C'

    def fahrenheit(self):
        if self.type == 'K':
            self.temp = (self.temp - 273.15) * 9 / 5 + 32
            self.type = 'F'
        elif self.type == 'C':
            self.temp = (self.temp * 9 / 5) + 32
            self.type = 'F'

    def kelvin(self):
        if self.type == 'C':
            self.temp = self.temp + 273.15
            self.type = 'K'
        elif self.type == 'F':
            self.temp = (self.temp - 32) * 5 / 9 + 273.15
            self.type = 'K'

    def __str__(self):
        return f"{self.temp}, {self.type}"


temp = Temperature(0, 'C')

temp.kelvin()
print(temp)