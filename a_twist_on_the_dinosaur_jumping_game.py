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

bird = [pygame.image.load(os.path.join("Assets/64x64", "Bird1.png")),
        pygame.image.load(os.path.join("Assets/64x64", "Bird2.png"))]

background = pygame.image.load(os.path.join("Assets/64x64", "Track.png"))

class cat:
    x_position = 80
    y_position = 310


    def __init__(self) :
        self.duck_image = ducking
        self.run_image = running
        self.jump_image = jumping

        self.cat_duck = False
        self.cat_run = True
        self.cat_jump = False

        self.step_index = 0 
        self.image = self.run_image[0]
        self.cat_rectangle = self.image.get_rect()
        self.cat_rectangle.x = self.x_position
        self.cat_rectangle.y = self.y_position

    def update(self, user_input) :
        


def main () : 
    run = True 
    clock = pygame.time.Clock()
    player = cat()


    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        Screen.fill ((255, 255, 255,))
        user_input = pygame.key.get_pressed()

        player.draw(screen)
        player.update(user_input)

        clock.tick(30)
        pygame.display.update()






main()