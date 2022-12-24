import random, pygame
from sorting_algorithms import selection_sort

class rectangles:
    def __init__ (self,rectangle_heights,num_of_rec,rectangle_width):
        self.rectangle_heights = rectangle_heights
        self.num_of_rec = num_of_rec
        self.rectangle_width = rectangle_width

def run_pygame(num_of_rec):
    screen_dimensions = initialize_screen_size()
    screen = initialize_pygame(screen_dimensions)
    clock = initialize_clock()
    
    rectangle_heights = initialize_rectangle_heights(num_of_rec,screen_dimensions[1])
    rectangle_width = initialize_rectangle_width(num_of_rec,screen_dimensions[0])
    rects = rectangles(rectangle_heights,num_of_rec,rectangle_width)
        
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0,0,0))
         
        display_rectangles(screen,rects,screen_dimensions) 
       
        clock.tick(5)
        pygame.display.flip()
    
    pygame.quit()

def display_rectangles(screen,rects,screen_dimensions):
    screen_height = screen_dimensions[1]
    
    num_of_rec = rects.num_of_rec
    rect_heights = rects.rectangle_heights
    rect_width = rects.rectangle_width
    
    rect_x = rect_width/8
    adjusted_width = rect_width*(3/4)

    for i in range(num_of_rec):
        rect_y = screen_height - rect_heights[i]
        pygame.draw.rect(screen,(160,160,160),pygame.Rect(rect_x,rect_y,adjusted_width,rect_heights[i]))
        rect_x += rect_width

def initialize_screen_size():
    WIDTH = 1500
    HEIGHT = 1000
    return [WIDTH,HEIGHT]

def initialize_pygame(screen_dimensions):
    pygame.init()
    screen = pygame.display.set_mode([screen_dimensions[0],screen_dimensions[1]])
    return screen

def initialize_clock():
    clock = pygame.time.Clock()
    return clock

def initialize_rectangle_heights(num_of_rec,screen_height):
    rectangles = []

    for i in range(num_of_rec):
        rectangles.append((random.randint(0,101)/100) * screen_height)
    return rectangles

def initialize_rectangle_width(num_of_rec,screen_width):
    rectangle_width = screen_width / num_of_rec
    return rectangle_width
    
num_of_rec = int(input("Input number of rectangles: "))
run_pygame(num_of_rec)







