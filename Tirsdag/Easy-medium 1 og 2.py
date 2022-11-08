
import pygame
import random

################################# settings################################################
'''
her finner du vindustørrelse og elementer(figurer) som brukes i programmet
'''

SCREEN_X = 640
SCREEN_Y = 480
BG_FNAME = "img/sushiplate.jpg" ### figurer for å lage fylle objekter
MOUSE_FNAME = "img/fugu.png"     
BALL_FNAME = "img/ball.png"
SONIC = "img/sonic.jpg"
TURTLE_NAME = "img/turtle.jpg"


################################## start #######################################
pygame.init()
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y), 0, 32)
background = pygame.image.load(BG_FNAME)
background = background.convert()

mouse_img  = pygame.image.load(MOUSE_FNAME).convert_alpha()
mouse_size_x = mouse_img.get_width()
mouse_size_y = mouse_img.get_height()

ball_img = pygame.image.load(BALL_FNAME).convert_alpha()

sonicImg = pygame.image.load(SONIC).convert_alpha()

turtleImg = pygame.image.load(TURTLE_NAME).convert_alpha()

### superklasse #### en superklasse er en form som brukes for å implementere subklasser
class MovingObject:
    def __init__(self):###### variabler som definerer egenskapene ####
        self.x = 42
        self.y = 200
        self.speed = [50 + 60 * random.random(),
                      50 + 60 * random.random()]
        self.size = 30

    def move(self, time_passed):    ######## funksjon move skal bruke variablene ovenfor for å 
        self.x += self.speed[0] * time_passed
        self.y += self.speed[1] * time_passed

        if self.x < 0:
            self.speed[0] = abs(self.speed[0])
        if self.y < 0:
            self.speed[1] = abs(self.speed[1])

        if self.x > SCREEN_X - self.size:
            self.speed[0] = -abs(self.speed[0])
        if self.y > SCREEN_Y - self.size:
            self.speed[1] = -abs(self.speed[1])

    def draw(self): #### not in use####
        pass

################################################ SUBKLASSER #############################


# Easy-medium oppgave 1
# Lager subklassen Sonicc
class Sonicc(MovingObject):
    def __init__(self):
        # Refererer til superklassen MovingObject
        MovingObject.__init__(self)
        # Setter bildet til objektet til sonicImg
        self.img = sonicImg
        # Setter størrelsen til objektet til størrelsen på bildet sonicImg
        self.size = self.img.get_height()
        # Gjør at sonic er 5x raskere enn et vanlig objekt
        self.speed = [self.speed[0] * 5, self.speed[1] * 5]

    def draw(self):
        # Plasserer objektet på skjermen
        screen.blit(self.img, (self.x, self.y))

# lager subklassen turtle
class Turtle(MovingObject):
    def __init__(self):
        # Refererer til superklassen MovingObject
        MovingObject.__init__(self)
        # Setter bildet til objektet til turtleImg
        self.img = turtleImg
        # Setter størrelsen til objektet til størrelsen på bildet turtleImg
        self.size = self.img.get_height()
        # Gjør at turtle er 5x tregere enn et vanlig objekt
        self.speed = [self.speed[0] / 5, self.speed[1] / 5]

    def draw(self):
        # Plasserer objektet på skjermen
        screen.blit(self.img, (self.x, self.y))

# Oppgave 2

# Arv er egenskaper en subklasse kan få fra en superklasse.






##########################################################################



### subklasse Ball ###################
class Ball(MovingObject):
    def __init__(self):
        MovingObject.__init__(self) #### en subklasse må deklarere superklasse
        self.img = ball_img
        self.size = self.img.get_height()

    def draw(self):
        screen.blit(self.img, (self.x, self.y))


## subklasse Circle ########################

class Circle(MovingObject):
    def __init__(self):
        MovingObject.__init__(self)
        self.col = (255, 255, 0)

    def draw(self):
        pygame.draw.circle(screen, self.col, (round(self.x), round(self.y)),
                           round(self.size / 2))

############################ instance ########### 
'''
***
'''

objs = [
    Ball(),
    Ball(),
    Circle(),
    Circle(),
    Sonicc(),
    Sonicc(),
    Turtle(),
    Turtle()
]

######################### main loop ####################################
clock = pygame.time.Clock()
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    time_passed = clock.tick(30) / 1000.0

    # t = pygame.mouse.get_pos()
    # x = t[0]
    # y = t[1]
    x, y = pygame.mouse.get_pos()

    mx = x - mouse_size_x / 2
    my = y - mouse_size_y / 2

    screen.blit(background, (0, 0))
    screen.blit(mouse_img, (mx, my))

    for obj in objs:
        obj.move(time_passed)

    for obj in objs:
        obj.draw()

    pygame.display.update()