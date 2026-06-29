import pygame
import time
import random
pygame.init()

#set up screen size + icon
screen = pygame.display.set_mode((1000,800), pygame.RESIZABLE)
game_icon = pygame.image.load('game_icon.png')
pygame.display.set_icon(game_icon)

#load images from file to use later
my_car = pygame.display.set_caption("Car racing game")
car1 = pygame.image.load('car_1.png')
car2 = pygame.image.load('car_2.png')
car3 = pygame.image.load('car_5.png')
car4 = pygame.image.load('car_6.png')
car = pygame.image.load('car_3.png')
car = pygame.transform.scale(car, (80, 150))


clock = pygame.time.Clock()

#colours, based off r,g,b to be used 
green = (120, 180, 80)
grey = (128,128,128)
black = (0,0,0)
white = (255,255,255)

quit_game = False
game_over = False
game_loop = True

#set initial values for variables / constants
car_x = 385
car_y = 580

car_x_change = 0
car_y_change = 6


#creates a class of objects called cars
class Car:

#these are the things that are specific to each car rather than the group
    def __init__(self, car_x, car_y, image):
        self.car_x = car_x
        self.car_y = car_y
        self.image = pygame.transform.scale(image, (80, 150))
        self.rect = self.image.get_rect(topleft=(self.car_x, self.car_y))

#each car object will run this function when called creates a rectagle, then
#image, based of the individuals x,y values.
    def make_car(self):
        screen.blit(self.image, (self.car_x, self.car_y))
        self.rect.topleft = (self.car_x, self.car_y)

#changes each car x by an amount
    def move_car(self):
        self.car_y += car_y_change
        if self.car_y > 800:
            self.car_y = random.randint(-300, -100)
            self.car_x = random.choice([250, 350, 450, 550, 650])
    
#for each obstcles object, it checks if it overlaps with the car 
    def collisions_car(self, player_rect):
        global game_over                    # CHANGED: Added global so it can modify game_over
        if self.rect.colliderect(player_rect):
            game_over = True



#this makes 4 cars using the car class and sets the x,y values for 
# each to use in the class code 
car_1 = Car(300, -200, car1)
car_2 = Car(550, -500, car2)
car_3 = Car(550, -800, car3)
car_4 = Car(650, -1100, car4)


font = pygame.font.Font("freesansbold.ttf", 50)


#score and high score
def load_high_score():
    try:
        hi_score_file = open("HI_score.txt", 'r')
    except:
        hi_score_file = open("HI_score.txt", 'w')
        hi_score_file.write("0")
        hi_score_file.close()
        hi_score_file = open("HI_score.txt", 'r')
    
    value = hi_score_file.read()
    hi_score_file.close()
    return value

#font
score_font = pygame.font.SysFont("freesansbold", 50)

def display_score(current, high):
    score_txt = score_font.render("Score: " + str(current), True, black)
    high_txt = score_font.render("High Score: " + str(high), True, black)
    screen.blit(score_txt, (20,20))
    screen.blit(high_txt, (20,80))


#showing messages such as score, you died etc
def message(msg, txt_colour):
    txt = font.render(msg, True, txt_colour)
    text_box = txt.get_rect(center=(500, 360))
    screen.blit(txt, text_box)
    pygame.display.update()
    time.sleep(2)


#score variables
current_score = 0
high_score = int(load_high_score())

start_time = time.time()

#game loop 
while not quit_game:

    while game_over:
            msg = ("You crashed! Press A to play again or Q to quit")
            txt = font.render(msg, True, white)
            screen.blit(txt, (120, 350))
            pygame.display.update() 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        quit_game = True
                        game_over = False
                    if event.key == pygame.K_a:
                        game_over = False
                        car_x = 385
                        start_time = time.time()
                        car_1.car_y, car_2.car_y, car_3.car_y, car_4.car_y = \
                              -200, -500, -800, -1100

 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                    car_x_change = 9
            if event.key == pygame.K_LEFT:
                car_x_change = -12
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                car_x_change = 0
            if event.key == pygame.K_LEFT:
                car_x_change = 0

    car_x += car_x_change
        
    if car_x >= 685:
            car_x = 685
            car_x_change = 0
            
    if car_x <= 235:
            car_x = 235
            car_x_change = 0


    screen.fill(green)

    pygame.draw.rect(screen, (60, 60, 60), [200, 0, 600, 800])
    pygame.draw.rect(screen, white, [200, 0, 10, 800])
    pygame.draw.rect(screen, white, [800, 0, 10, 800])

    divider_x_positions = [350, 500, 650]
    for x in divider_x_positions:
            for y in range(0, 800, 60):
                pygame.draw.rect(screen, white, [x, y, 5, 40])

    screen.blit(car, (car_x, car_y))


    current_time = time.time()
    current_score = int(current_time - start_time)
    
    if current_score > high_score:
            high_score = current_score
        

    #each game loop, these lines will run the functions in the cactus class 
    #and it runs as each of those objects (so when cacti_2.collisions () runs,
    #it specifically) checks if cacti_2 collides with the llama)
    player_rect = pygame.Rect(car_x, car_y, 80, 150)
    car_1.make_car()
    car_2.make_car()
    car_3.make_car()
    car_4.make_car()

    car_1.move_car()
    car_2.move_car()
    car_3.move_car()
    car_4.move_car()

    car_1.collisions_car(player_rect)
    car_2.collisions_car(player_rect)
    car_3.collisions_car(player_rect)
    car_4.collisions_car(player_rect)


    hi_score_file = open("HI_score.txt", 'w')
    hi_score_file.write(str(high_score))
    hi_score_file.close()

    display_score(current_score, high_score)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()