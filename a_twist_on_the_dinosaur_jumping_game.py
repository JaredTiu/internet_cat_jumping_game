import pygame 
import os 

pygame.init()

screen_height = 600
screen_width = 1100
screen = pygame.display.set_mode((screen_width, screen_height))

running = [pygame.image.load(os.path.join("Assets/64x64", "run1better.png")),
        pygame.image.load(os.path.join("Assets/64x64", "run2better.png"))]
jumping = pygame.image.load(os.path.join("Assets/64x64", "jumping.png"))
ducking = [pygame.image.load(os.path.join("Assets/64x64", "duck2.png")),
        pygame.image.load(os.path.join("Assets/64x64", "duck3.png"))]

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
    y_position_duck = 320


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
        if self.cat_duck:
            self.duck()
        if self.cat_run:
            self.run()
        if self.cat_jump:
            self.jump()
        
        if self.step_index >= 10: 
            self.step_index = 0
        
        if user_input[pygame.K_UP] and not self.cat_jump:
            self.cat_duck = False
            self.cat_run = False
            self.cat_jump = True
        elif user_input[pygame.K_DOWN] and not self.cat_jump:
            self.cat_duck = True
            self.cat_run = False
            self.cat_jump = False
        elif not (self.cat_jump or user_input[pygame.K_DOWN]):
            self.cat_duck = False
            self.cat_run = True
            self.cat_jump = False

    def duck(self):
        self.image = self.duck_image[self.step_index // 5]
        self.cat_rectangle = self.image.get_rect()
        self.cat_rectangle.x = self.x_position
        self.cat_rectangle.y = self.y_position_duck
        self.step_index += 1


    def run(self):
        self.image = self.run_image[self.step_index // 5]
        self.cat_rectangle = self.image.get_rect()
        self.cat_rectangle.x = self.x_position
        self.cat_rectangle.y = self.y_position
        self.step_index += 1

    def jump(self):
        pass

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.cat_rectangle.x, self.cat_rectangle.y))



def main () : 
    run = True 
    clock = pygame.time.Clock()
    player = cat()


    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill ((255, 255, 255,))
        user_input = pygame.key.get_pressed()

        player.draw(screen)
        player.update(user_input)

        clock.tick(30)
        pygame.display.update()






main()