class motorsykkel:
    def __init__(self,motorStørrelse,
speed,
max_speed,
konsum):
        self.motor = motorStørrelse
        self.speed = speed
        self.max_speed = max_speed
        self.konsum = konsum
    def asfalt_in_badCondition(self):
        self.max_speed -= 99
        self.konsum -= 10
        self.speed -= 100
        return self.max_speed, self.konsum
    def dancing_in_the_rain(self):
        self.max_speed += 100
        self.konsum -= 10
        return self.max_speed, self.konsum
    def like_A_ferrari(self):
        self.max_speed += 1000
        self.konsum *= 10 * self.max_speed
        return self.max_speed, self.konsum
# Bilverdi blir til bil klassen
motorsykkelVerdi = motorsykkel(10, 80, 150, 50)

print(motorsykkelVerdi.asfalt_in_badCondition())
print(motorsykkelVerdi.dancing_in_the_rain())
print(motorsykkelVerdi.like_A_ferrari())