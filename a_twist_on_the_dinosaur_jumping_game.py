import pygame 
import os 

pygame.init()

screen_height = 600
screen_width = 1100
screen = pygame.display.set_mode((screen_width, screen_height))

running = [pygame.image.load(os.path.join("Assets/64x64", "run1.png")),
        pygame.image.load(os.path.join("Assets/64x64", "run2.png"))]
Jumping = pygame.image.load(os.path.join("Assets/64x64", "jump1.png"))


def main () : 
    run = True 

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False