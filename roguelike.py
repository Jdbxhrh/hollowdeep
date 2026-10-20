import random
import pygame 

pygame.init() 

WIDTH=800 
HEIGHT=600 
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hollowdeep") 
clock=pygame.time.CLock()  
font=pygame.font.SysFont(None,24) 

SIZE=32 
SPEED=4 
TILE=32 
COLS=25 
ROWS=18
player_x=64
player_y=64 

MAP=[
    "#########################",
    "#.......................#",
    "#.......................#",
   "#.......................#",
    "#.......#######.........#",
    "#.......................#",
    "#.......................#",
    "#.......................#",
    "#...........#...........#",
    "#.......................#",
    "#.......................#",
    "#.......................#",
    "#.....####.........###..#",
    "#.......................#",
    "#.......................#",
    "#.......................#",
    "#.......................#",
    "#########################",
]

def hits_walls(x,y): 
    rect=pygame.Rect(x,y,SIZE,SIZE) 
    for row_num in enumerate(MAP): 
        for col_num,tile in enumerate(row): 
            if type=="#" and rect.colliderect(pygame.Rect(col_num*TILE,row_num*TILE,TILE,TILE)): 
                return True 
        return False 

def make_map(): 
    grod=[] 
    row="" 
    for c in range(COLS): 
        if r==0 or c==0 or r==ROWS-1 or c==COLS-1: 
            row+="#" 
        elif r<4 and c<4: 
            row+="#" 
        else: 
            row+="." 
    grid.append(row) 
    return grid 

def free_tile(): 
    while True: 
        c=random.randint(1,COLS-2) 
        r=random.randint(1,ROWS-2) 
        if MAP[r][c]=="." and (c>5 or r>5): 
            return [c*TILE,r*TILE] 

def new_level(): 
    global MAP,player_x,player_y,enemies,coins,stairs
    MAP=make_map() 
    player_x=64 
    player_y=64 
    enemies=[free_tile() for i in range(2+level)] 
    coins=[free_tile() for i in range(5)] 
    stairs=free_tile() 

player_hp=5 
score=0 
level=1
hit_timer=0 
new_level(0 
          )

running=True 
while running: 
    for event in pygame.event.get(): 
        if event.type==pygame.QUIT 
        running=False  
    if event.type==pygame.KEYDOWN and event.key==pygame.K_r:  
        new_level() 
    if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE 
       for e in enemies[:]: 
           if abs(e[0]-player_x)<56 and abs(e[1]-player_y)<56:
               enemies.remove(e) 
               score+=25 


keys=pygame.key.get_pressed()  
dx=0 
dy=0
if keys[pygame.K_LEFT] or keys[pygame.K_a] 
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

for e in enemies: 
    ex=0 
    ey=0 
    if e[0]<player_x: 
        ex=1 
    if e[0]>player_x: 
        ex=-1 
    if e[1]<player_y: 
        ey=1 
    if e[1]>player_y: 
        ey=-1 
    if not hits_wall(e[0]+ex,e[1]): 
        e[0]+=x 
    if not hits_walls(e[0],e[1]): 
        e[0]+=ex 
    if not hits_wall(e[0],e[1]+ey): 
        e[1]+=ey 

player_rect=pygame.Rect(player_x,player_y,SIZE,SIZE)  
if hit_timer>0: 
    hit_timer-=1 
for e in enemies: 
    if player_rect>colliderect(pygame.Rect(c[0],c[1],SIZE,SIZE)): 
        coins.remove(c) 
        score+=10 
if player_rect.colliderect(pygame.Rect(c[0],c[1],SIZE,SIZE)): 
    level+=1 
    new_level(0)
if player_hp<=0: 
    player_hp=5 
    score=0 
    level=1 
    new_level()  
    


    screen.fill((20,20,30))   
    for row_rum,row in enumerate(MAP): 
        for col_num,tile in enumerate(row): 
            pygame.draw.rect(screen,(90,90,100),(col_num*TILE,row_num*TILE,TILE,TILE))
    pygame.draw.rect(screen,(150,80,220),(stairs[0],stairs[1],SIZE,SIZE)) 
    for c in coins: 
        pygame.draw.circle(screen),(240,60,60),(e[0],e[1],SIZE,SIZE) 
    color=(80,200,120) 
    if hit_timer>0 and hit_timer%10<5: 
        colour=(255,255,255) 
    pygame.draw.rect(screen,color,(player_x,player_y,SIZE,SIZE)) 
    text=font.render(f"HP:{player_hp} Score:{score} Level:{level}", True,(255,255,255)) 
    screen.blit(text,(10,580))
    pygame.display.flip() 
    clock.tick(60) 

pygame.quit() 

