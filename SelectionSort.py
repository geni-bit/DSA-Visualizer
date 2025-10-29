import pygame
import random

pygame.init()

WindowSize = 600
Window = pygame.display.set_mode((WindowSize, WindowSize))
pygame.display.set_caption('Selection Sort Visualization')

rectangleWidth = 20

# Colors
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREY = (170, 170, 170)
ORANGE = (255, 165, 0)
LIGHT_BLUE = (64, 224, 208)

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
        self.color = GREEN

def createRectangles():
    num_rectangles = WindowSize // rectangleWidth - 5
    rectangles = []
    heights = []

    for i in range(5, num_rectangles):
        height = random.randint(20, 500)
        while height in heights:
            height = random.randint(20, 500)

        heights.append(height)
        rect = Rectangle(ORANGE, i * rectangleWidth, height)
        rectangles.append(rect)

    return rectangles

def draw_rect(rectangles):
    Window.fill(GREY)
    for rect in rectangles:
        pygame.draw.rect(Window, rect.color, (rect.x, WindowSize-rect.height, rect.width, rect.height)) 
        pygame.draw.line(Window, BLACK, (rect.x, WindowSize), (rect.x, WindowSize-rect.height)) 
        pygame.draw.line(Window, BLACK, (rect.x + rect.width, WindowSize), (rect.x + rect.width, WindowSize-rect.height)) 
        pygame.draw.line(Window, BLACK, (rect.x, WindowSize - rect.height), (rect.x + rect.width, WindowSize-rect.height))

def selection_sort(rectangles):
    numRectangles = len(rectangles)

    for i in range(numRectangles):
        min_index = i
        rectangles[i].set_smallest()
        draw_rect(rectangles)
        pygame.time.delay(50)

        for j in range(i + 1, numRectangles):
            rectangles[j].select()
            draw_rect(rectangles)
            pygame.time.delay(10)

            if rectangles[j].height < rectangles[min_index].height:
                rectangles[min_index].unselect()
                min_index = j
                rectangles[j].set_smallest()

            rectangles[j].unselect()
            draw_rect(rectangles)
            pygame.time.delay(10)
            yield  # allow frame-by-frame updates

        # Swap the rectangles visually and logically
        rectangles[i].x, rectangles[min_index].x = rectangles[min_index].x, rectangles[i].x
        rectangles[i], rectangles[min_index] = rectangles[min_index], rectangles[i]

        rectangles[i].set_sorted()
        draw_rect(rectangles)
        pygame.time.delay(50)
        yield


def display_text(txt, y, size):
    FONT = pygame.font.SysFont('Verdana', size)

    text = FONT.render(txt, True, BLACK)
    text_rect = text.get_rect(center = (WindowSize/2, y))
    Window.blit(text, text_rect)

def main():
    rectangles = createRectangles()
    draw_rect(rectangles)
    sorting_generator = selection_sort(rectangles)

    run = True
    sorting = False

    while run:
        if sorting:
            try:
                next(sorting_generator)
            except StopIteration:
                sorting = False
        else:
            draw_rect(rectangles)

        display_text('Selection Sorting Algorithm Visualization: ', 30, 20)
        display_text('Press SPACE to start sorting or q to quit', 70, 20)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    sorting = not sorting
                if event.key == pygame.K_q:
                    run = False

        pygame.display.update()

    pygame.quit()

main()
