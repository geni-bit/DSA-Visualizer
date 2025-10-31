import pygame 
import random 

pygame.init()

class DrawInfo:
    # Colors
    WHITE = (255,255,255)
    GREEN = (0, 255, 0)
    RED = (255,0,0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    GREY = (170, 170, 170)
    ORANGE = (255, 165, 0)
    LIGHT_BLUE = (64, 224, 208)
    BACKGROUN_COLOR = WHITE

    SIDE_PAD = 100
    TOP_PAD = 100

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height 

        self.window = pygame.display.set_mode((width,height))
        pygame.display.set_caption("Sorting Algorithm Vizualization")
        self.set_list(lst)

    def set_list(self,lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.pixel_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.block_height = round((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2

def generate_starting_list(n, min_val, max_val):
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst

def main():

    run = True 
    clock = pygame.time.Clock()

    while run: 
        clock.tick(60)

        pygame.display.update()

        for event in pygame.event.get():
            if event == pygame.QUIT:
                run = False 
    
    pygame.quit()


if __name__ == "__main__":
    main()


       



    



