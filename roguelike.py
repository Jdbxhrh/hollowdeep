import random
import pygame

pygame.init()

WIDTH=800
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hollowdeep")
clock=pygame.time.Clock()

SIZE=32
SPEED=4
TILE=32
COLS=25
ROWS=18
player_x=64
player_y=64

def hits_wall(x,y):
    rect=pygame.Rect(x,y,SIZE,SIZE)
    for row_num,row in enumerate(MAP):
        for col_num,tile in enumerate(row):
            if tile=="#" and rect.colliderect(pygame.Rect(col_num*TILE,row_num*TILE,TILE,TILE)):
                return True
    return False

def make_map():
    grid=[]
    for r in range(ROWS):
        row=""
        for c in range(COLS):
            if r==0 or c==0 or r==ROWS-1 or c==COLS-1:
                row+="#"
            elif r<4 and c<4:
                row+="."
            elif random.random()<0.12:
                row+="#"
            else:
                row+="."
        grid.append(row)
    return grid

MAP=make_map()

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN and event.key==pygame.K_r:
            MAP=make_map()
            player_x=64
            player_y=64

    keys=pygame.key.get_pressed()
    dx=0
    dy=0
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        dx=-SPEED
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        dx=SPEED
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        dy=-SPEED
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        dy=SPEED

    if not hits_wall(player_x+dx,player_y):
        player_x+=dx
    if not hits_wall(player_x,player_y+dy):
        player_y+=dy

    screen.fill((20,20,30))
    for row_num,row in enumerate(MAP):
        for col_num,tile in enumerate(row):
            if tile=="#":
                pygame.draw.rect(screen,(90,90,110),(col_num*TILE,row_num*TILE,TILE,TILE))
    pygame.draw.rect(screen,(80,200,120),(player_x,player_y,SIZE,SIZE))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()