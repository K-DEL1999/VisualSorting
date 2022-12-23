import random, pygame
from sorting_algorithms import selection_sort

def run_pygame():
    screen_dimensions = initialize_screen_size()
    screen = initialize_pygame(screen_dimensions)
    clock = initialize_clock()
    
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    screen.fill((0,0,0))

    clock.tick(5)
    pygame.display.flip()

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

run_pygame()
pygame.quit()







