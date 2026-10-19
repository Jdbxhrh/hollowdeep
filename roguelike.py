import pygame 

pygame.init() 

WIDTH=800 
HEIGHT=600 
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hollowdeep") 
clock=pygame.time.CLock()  

SIZE=32 
SPEED=4 
player_x=400 
player_y=300

running=True 
while running: 
    for event in pygame.event.get(): 
        if event.type==pygame.QUIT 
        running=False 

keys=pygame.key.get_pressed() 
if keys[pygame.K_LEFT] or keys[pygame.K_a] 
    player_x-=SPEED 
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]: 
        player_x+=SPEED  
    if keys[pygame.K_UP] or keys[pygame.K_w]: 
        player_y-=SPEED 
    if keys[pygame.K_DOWN] or keys[pygame.K_s]: 
        player_y+=SPEED


    screen.full((20,20,30)) 
    pygame.display.flip() 
    clock.tick(60) 

pygame.quit()