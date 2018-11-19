import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Demo Game")

#set up sprites and other variables

paddle_rect = [300,500,50,20]
paddle_color = (250,0,0)

ball_rect = [150,150,20,20]
ball_color = (250,250,0)

gameover = False
clock = pygame.time.Clock()

#game loop starts here
while not gameover:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                gameover = True
            #other key events here that happen ONCE when you press


                
    #keys that you can hold down:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_m]:
        paddle_rect[0] += 5
            
    #actions that happen automatically.               
    #move stuff
    ball_rect[0] += 10
    ball_rect[1] += 10


                
    #handle collisions

    #clear the screen
    screen.fill((0,0,0))
    
    #draw stuff
    pygame.draw.ellipse(screen, ball_color, ball_rect)
    pygame.draw.rect(screen, paddle_color, paddle_rect)

    #show the new screen (60x per second).
    pygame.display.flip()

pygame.quit()
    

