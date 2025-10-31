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
    BACKGROUND_COLOR = WHITE

    GRADIENTS = [(230, 230, 250), (127,127,213), (0,0,139)]


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

        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.block_height = round((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2

def draw(draw_info):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)
    draw_list(draw_info)
    pygame.display.update()

def draw_list(draw_info):
    lst = draw_info.lst

    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        height = (val - draw_info.min_val) * draw_info.block_height
        y = draw_info.height - height
        
        color = draw_info.GRADIENTS[i % 3]
        
        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, height))
        
        color = draw_info.GRADIENTS[i % 3] 
        
        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, height))


def generate_starting_list(n, min_val, max_val):
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst

def main():

    run = True 
    clock = pygame.time.Clock()

    n = 50 
    min_val = 0
    max_val = 100

    lst = generate_starting_list(n,min_val, max_val)

    draw_information = DrawInfo(800,600, lst)
    while run: 
        clock.tick(60)

        draw(draw_information)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
    
    pygame.quit()


if __name__ == "__main__":
    main()


       



    



