import pygame 
import random

pygame.init()

WindowSize = 600
Window = pygame.display.set_mode((WindowSize,WindowSize))
pygame.display.set_caption('Selection Sort Visualization')

# Variables
rectangleWidth = 20

# Colors 
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
GREY = (170,170,170)
ORANGE = (255,165,0)
LIGHT_BLUE = (64,224,208)

class Rectangle:
    def __init__(self, color, x, height) -> None:
        self.color = color
        self.x = x
        self.width = rectangleWidth
        self.height = height

    def select(self):
        self.color = BLUE

    def unselect(self):
        self.color = ORANGE

    def set_smallest(self):
        self.color = LIGHT_BLUE

    def set_sorted(self): 
        set.color = GREEN

def createRectangles():
    num_rectangles = WindowSize // rectangleWidth - 5
    rectangles = []
    heights = []

    for i in range(5, num_rectangles):
        height = random.randint(20,500)
        while height in heights:
            height = random.randint(20,500) 

        heights.append(height)
        rect = Rectangle(ORANGE, i * rectangleWidth, height)
        rectangles.append(rect)

    return rectangles 

def draw_rect(rectangles):
    Window.fill(GREY)

    for rect in rectangles:
        pygame.draw.rect(Window, rect.color, (rect.x, 200, rect.width,rect.height))




rectangles = createRectangles()

run = True

while run: 
    draw_rect(rectangles)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()

