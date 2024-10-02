import pygame 
import os 

pygame.init()

screen_height = 600
screen_width = 1100
screen = pygame.display.set_mode((screen_width, screen_height))

running = [pygame.image.load(os.path.join("Assets/64x64", "run1.png")),
        pygame.image.load(os.path.join("Assets/64x64", "run2.png"))]
jumping = pygame.image.load(os.path.join("Assets/64x64", "jumping.png"))
ducking = [pygame.image.load(os.path.join("Assets/64x64", "duck1.png")),
        pygame.image.load(os.path.join("Assets/64x64", "duck2.png"))]

small_box = [pygame.image.load(os.path.join("Assets/64x64", "Boxsmall1.png")),
             pygame.image.load(os.path.join("Assets/64x64", "Boxsmall2.png")), 
             pygame.image.load(os.path.join("Assets/64x64", "Boxsmall3.png")),]

big_box =  [pygame.image.load(os.path.join("Assets/64x64", "Box.png")),
            pygame.image.load(os.path.join("Assets/64x64", "Boxbig2.png")), 
            pygame.image.load(os.path.join("Assets/64x64", "Boxbig3.png")),]


def main () : 
    run = True 

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False