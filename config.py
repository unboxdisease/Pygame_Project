import pygame
from pygame import mixer
pygame.font.init()
# variables
WIDTH = 700
HEIGHT = 840
i = 0

# locations and velocities of obstacles
v = [3, 2.4, 4, 2, 1.4]
loc = [10 + 70, 180 + 70, 350 + 70, 520 + 70, 680 + 70]
loc2 = [180, 350, 520, 680]

h = []
a = []
b = []

level_1 = 0
level_2 = 0

vel = 2.5

x = 350
y = 800

X = 350
Y = 0
score = 0
score2 = 0
id = 1


# fonts and images

clock = pygame.time.Clock()
back = pygame.image.load('back.png')
black = pygame.image.load('blackboard.png')
bug = pygame.image.load('bug.png')
boat = pygame.image.load('boat.png')
win = pygame.display.set_mode((700, 840))
pygame.display.set_caption("First Game")
myfont = pygame.font.Font("freesansbold.ttf", 16)
largeText = pygame.font.Font('freesansbold.ttf', 30)
smallText = pygame.font.Font('freesansbold.ttf', 20)
vsmallText = pygame.font.Font('freesansbold.ttf', 16)
