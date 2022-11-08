
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


################################## start #######################################
pygame.init()
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y), 0, 32)
background = pygame.image.load(BG_FNAME)
background = background.convert()

mouse_img  = pygame.image.load(MOUSE_FNAME).convert_alpha()
mouse_size_x = mouse_img.get_width()
mouse_size_y = mouse_img.get_height()

ball_img = pygame.image.load(BALL_FNAME).convert_alpha()

### superklasse #### en superklasse er en form som brukes for å implementere subklasser
class MovingObject:
    def __init__(self):###### variabler som definerer egenskapene ####
        self.x = 42
        self.y = 200
        self.speed = [50 + 60 * random.random(),
                      50 + 60 * random.random()]
        self.size = 30
        self.color = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))

    def move(self, time_passed):
        self.x += self.speed[0] * time_passed
        self.y += self.speed[1] * time_passed

        # Hastigheten blir delt på to hver gang den treffer veggen
        if self.x < 0:
            self.speed[0] = abs(self.speed[0]/2)
        if self.y < 0:
            self.speed[1] = abs(self.speed[1]/2)

        if self.x > SCREEN_X - self.size:
            self.speed[0] = -abs(self.speed[0]/2)
            self.color = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
        if self.y > SCREEN_Y - self.size:
            self.speed[1] = -abs(self.speed[1]/2)
            self.color = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))

    def draw(self): #### not in use####
        pass

################################################ SUBKLASSER #############################

### subklasse BigCircle ###################
class BigCircle(MovingObject):
    def __init__(self):
        MovingObject.__init__(self)

    def draw(self):
        pygame.draw.circle(screen, self.color, (round(self.x), round(self.y)), self.size)


## subklasse Circle ########################

class Circle(MovingObject):
    def __init__(self):
        MovingObject.__init__(self)

    def draw(self):
        pygame.draw.circle(screen, self.color, (round(self.x), round(self.y)),
                           round(self.size / 2))

############################ instance ########### 
'''
***
'''

objs = [
    BigCircle(),
    BigCircle(),
    BigCircle(),
    Circle(),
    Circle(),
    Circle(),
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




# Oppgave 3
# Superklasse er en klasse som kan bli brukt i andre subklasser.
# Sub klasser arver egenskaper fra en superklasse.
# Arv er egenskaper en subklasse kan få fra en superklasse.