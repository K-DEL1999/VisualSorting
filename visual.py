import random, pygame
from sorting_algorithms import selection_sort

class grid:
    def __init__(self,grid,rows,columns):
        self.grid = grid
        self.rows = rows
        self.columns = columns

def run_pygame(grid):
    screen_dimensions = initialize_screen_size()
    screen = initialize_pygame(screen_dimensions)
    clock = initialize_clock()
    
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0,0,0))
      
         
        display_grid(screen,screen_dimensions,grid) 
       
        clock.tick(5)
        pygame.display.flip()

def display_grid(screen,screen_dimensions,grid):
    r = c = x = y = 0
    width = screen_dimensions[0]/grid.columns
    height = screen_dimensions[1]/grid.rows

    for i in range(len(grid.grid)): 
        print(x,y)        
        pygame.draw.rect(screen,(grid.grid[i]),pygame.Rect(x,y,width,height))
        c += 1
        if c == grid.columns:
            x = 0
            c = 0
            r += 1
            y = r*height
        else:
            x = c*width

def initialize_screen_size():
    WIDTH = 1200
    HEIGHT = 1200
    return [WIDTH,HEIGHT]

def initialize_pygame(screen_dimensions):
    pygame.init()
    screen = pygame.display.set_mode([screen_dimensions[0],screen_dimensions[1]])
    return screen

def initialize_clock():
    clock = pygame.time.Clock()
    return clock

rows = int(input("How many rows: "))
columns = int(input("How many columns: "))

grid = grid([],rows,columns)

for i in range(rows*columns):
        rgb = [(random.randint(0,255)),(random.randint(0,255)),(random.randint(0,255))]
        grid.grid.append(rgb)


run_pygame(grid)

pygame.quit()







