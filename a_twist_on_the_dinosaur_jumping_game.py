import pygame 
import os 
import random

pygame.init()

screen_height = 600
screen_width = 1100
screen = pygame.display.set_mode((screen_width, screen_height))

running = [pygame.image.load(os.path.join("Assets/64x64", "run1better.png")),
        pygame.image.load(os.path.join("Assets/64x64", "run2better.png"))]
jumping = pygame.image.load(os.path.join("Assets/64x64", "jumping.png"))
ducking = [pygame.image.load(os.path.join("Assets/64x64", "duck2.png")),
        pygame.image.load(os.path.join("Assets/64x64", "duck3.png"))]

small_dog = [pygame.image.load(os.path.join("Assets/Bubbas", "spr_BubbaE_0.png")),
             pygame.image.load(os.path.join("Assets/64x64", "spr_BubbaE_1.png")), 
             pygame.image.load(os.path.join("Assets/64x64", "spr_BubbaE_1.png")),]

big_dog =  [pygame.image.load(os.path.join("Assets/64x64", "spr_BubbaE2_0.png")),
            pygame.image.load(os.path.join("Assets/64x64", "spr_BubbaE2_1.png")), 
            pygame.image.load(os.path.join("Assets/64x64", "spr_BubbaE2_2.png")),]

bird = [pygame.image.load(os.path.join("Assets/64x64", "Bird1.png")),
        pygame.image.load(os.path.join("Assets/64x64", "Bird2.png"))]

cloud_image = pygame.image.load(os.path.join("Assets/64x64", "Cloud.png"))

background_image = pygame.image.load(os.path.join("Assets/64x64", "Track.png"))

class cat:
    x_position = 80
    y_position = 310
    y_position_duck = 320
    jump_velocity = 8.5


    def __init__(self) :
        self.duck_image = ducking
        self.run_image = running
        self.jump_image = jumping

        self.cat_duck = False
        self.cat_run = True
        self.cat_jump = False

        self.step_index = 0 
        self.jumping = self.jump_velocity
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
        self.image = self.jump_image
        if self.cat_jump:
            self.cat_rectangle.y -= self.jumping * 4
            self.jumping -= 0.8
        if self.jumping < - self.jump_velocity: 
            self.cat_jump = False
            self.jumping = self.jump_velocity

    def draw(self, screen):
        screen.blit(self.image, (self.cat_rectangle.x, self.cat_rectangle.y))

class Cloud:
    def __init__(self):
        self.x = screen_width + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = cloud_image
        self.width = self.image.get_width()

    def update(self):
        self.x -=game_speed
        if self.x < -self.width:
            self.x = screen_width + random.randint(2500, 3000)
            self.y = random.randint (50, 100)
    
    def draw (self, screen):
        screen.blit(self.image, (self.x, self.y))

class obstacle:
    def __init__(self, image, type): 
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = screen_width

    def update(self): 
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width: 
            obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)

class small_dog_(obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 290

class big_dog_(obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 270

class bird_(obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, screen):
        if self.index >= 9:
            self.index = 0
            screen.blit(self.image[self.index//5], self.rect)
            self.index += 1



def main () : 
    global game_speed, x_position_background, y_position_background, points, obstacles
    run = True 
    clock = pygame.time.Clock()
    player = cat()
    cloud_image = Cloud()
    game_speed = 10
    x_position_background = 0
    y_position_background = 360
    points = 0 
    font = pygame.font.Font("freesansbold.ttf", 20)
    obstacles = []

    def score(): 
        global points, game_speed
        points += 1
        if points % 100 == 0: 
            game_speed += 1

        point_counter = font.render("score: " + str(points), True, (0, 0, 0))
        point_counter_rect = point_counter.get_rect()
        point_counter_rect.center = (1000, 40)
        screen.blit(point_counter, point_counter_rect) 

    def background(): 
        global x_position_background, y_position_background
        image_width = background_image.get_width()
        screen.blit(background_image, (x_position_background, y_position_background))
        screen.blit(background_image, (image_width + x_position_background, y_position_background))
        if x_position_background <= -image_width:
            screen.blit(background_image, (image_width + x_position_background, y_position_background))
            x_position_background = 0
        x_position_background -= game_speed


    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill ((255, 255, 255,))
        user_input = pygame.key.get_pressed()

        player.draw(screen)
        player.update(user_input)

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(small_dog_(small_dog))
            elif random.randint(0, 2) == 1:
                obstacles.append(big_dog_(big_dog))
            elif random.randint(0, 2) == 2:
                obstacles.append(bird_(bird))
        
        for obstacle in obstacles:
            obstacle.draw(screen)
            obstacle.update()
            if player.cat_rectangle.colliderect(obstacle.rect):
                pygame.draw.rect(screen, (255, 0, 0), player.cat_rectangle, 2)

        background()

        cloud_image.draw(screen)
        cloud_image.update()

        score()

        clock.tick(30)
        pygame.display.update()






main()