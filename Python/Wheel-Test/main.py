from motorcontroller import *
import pygame
pygame.init()


win = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 60
vel = 5*2

drive_time = 0.2
drive_speed = 'LOW'

run = True
motor_controller = MotorController()
while run:
    pygame.time.delay(25)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP or event.key == ord('w'):
            print('up')
            y -= vel
            motor_controller.forward(drivetime = drive_time, inputspeed = drive_speed)
        elif event.key == pygame.K_DOWN or event.key == ord('s'):
            print('down')
            y += vel
            motor_controller.backward(drivetime = drive_time, inputspeed = drive_speed)
        elif event.key == pygame.K_LEFT or event.key == ord('a'):
            print('left')
            x -= vel
            motor_controller.left(drivetime = drive_time, inputspeed = drive_speed)
        elif event.key == pygame.K_RIGHT or event.key == ord('d'):
            print('right')
            x += vel
            motor_controller.right(drivetime = drive_time, inputspeed = drive_speed)
        elif event.key == ord('q'):
            print('counterclockwise')
            motor_controller.rotate(direction = 'COUNTER_CLOCKWISE',drivetime = drive_time, inputspeed = drive_speed)
        elif event.key == ord('e'):
            print('clockwise')
            motor_controller.rotate(direction = 'CLOCKWISE',drivetime = drive_time, inputspeed = drive_speed)
    else:
        motor_controller.stop()
        
    win.fill((0,0,0))  # Fills the screen with black
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))   
    pygame.display.update() 
    
pygame.quit()