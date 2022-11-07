class bil:
    def __init__(self,motor,
antall_seter,
farge,
speed,
max_speed,
dimensjon_dekk,
drivstoff,
dimensjon_bil,
konsum,
distance_vision):
        self.motor = motor
        self.antall_seter = antall_seter
        self.farge = farge
        self.speed = speed
        self.max_speed = max_speed
        self.dimensjon_dekk = dimensjon_dekk
        self.drivstoff = drivstoff
        self.dimensjon_bil = dimensjon_bil
        self.konsum = konsum
        self.distance_vision = distance_vision
    def weather_condition(self):
        self.max_speed -= 10
        self.konsum -= 10
        self.distance_vision -= 100
        return self.max_speed, self.konsum, self.distance_vision
    def daylight(self):
        self.max_speed += 10
        self.konsum += 10
        self.distance_vision += 100
        return self.max_speed, self.konsum, self.distance_vision
    def hurry_up(self):
        self.max_speed += 1000
        self.konsum -= 10
        self.distance_vision -= 10
        return self.max_speed, self.konsum, self.distance_vision
# Bilverdi blir til bil klassen
bilVerdi = bil(10, 5, 1, 100, 200, 20, 20, 200, 20, 10)

print(bilVerdi.weather_condition())
print(bilVerdi.daylight())
print(bilVerdi.hurry_up())