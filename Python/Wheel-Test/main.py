from .motorcontroller import MotorController
import pygame
pygame.init()


win = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 60
vel = 5

run = True
motor_controller = MotorController()
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x -= vel
        print('left')
        motor_controller.left()
    if keys[pygame.K_RIGHT]:
        x += vel
        print('right')
        motor_controller.right()
    if keys[pygame.K_UP]:
        y -= vel
        print('up')
        motor_controller.up()
    if keys[pygame.K_DOWN]:
        y += vel
        print('down')
        motor_controller.down()
        
    win.fill((0,0,0))  # Fills the screen with black
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))   
    pygame.display.update() 
    
pygame.quit()