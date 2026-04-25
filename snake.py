import pygame
import random
clock=pygame.time.Clock()
pygame.init()
screen=pygame.display.set_mode((400,400),pygame.NOFRAME)
pygame.display.set_caption('Snake Game')
icon=pygame.image.load('images\icon_snake.png')
bg=pygame.image.load('images\snake_bg.png')
lose_photo=pygame.image.load('images\snake.png')           #loading all photos
pygame.display.set_icon(icon)
running=True
gameplay=True
BLock=20
snake=[[200,200],[180,200],[160,200]]
direction='RIGHT'

soz=pygame.font.Font('fonts\\font.ttf',15)            #basic variables
score=0
level=1

def spawn_food():
    while True:
        food_block=random.choice([10,16,20])
        f=[random.randint(0,19)*BLock,random.randint(0,19)*BLock] #for spawn foods not in snake and different weights
        if f not in snake:
            return f,food_block
food,food_bl=spawn_food()
dt=6
food_spawn_time=pygame.time.get_ticks()
food_limit=5000
while running:
    clock.tick(dt)
    dt=level+5
    if gameplay:
        screen.blit(bg,(0,0))
        head=snake[0].copy()
        

        if direction=='RIGHT' :
            head[0]+=BLock
        if direction=='LEFT':
            head[0]-=BLock
        if direction=='UP' :
            head[1]-=BLock
        if direction=='DOWN':
            head[1]+=BLock            #moveing our snake
        snake.insert(0,head)
        now=pygame.time.get_ticks()
        if now-food_spawn_time>=food_limit:
            food,food_bl=spawn_food()                       #it is for timer
            food_spawn_time=now
            snake.pop()
        elif head==food:
            food,food_bl=spawn_food()
            food_spawn_time = now
            if food_bl==20:
                score+=3
            elif food_bl==16:
                score+=2
            elif food_bl==10:
                score+=1                   #different scores for different weights
        else:
            snake.pop()
        if head[0]<0 or head[0]>=400 or head[1]<0 or head[1]>=400 or head in snake[1:]:
            gameplay=False
        for i,block in enumerate(snake):
            if i==0:
                pygame.draw.rect(screen,(95, 153, 245),(block[0]+1,block[1]+1,BLock-2,BLock-2))
            else:
                pygame.draw.rect(screen,(0, 58, 150),(block[0]+1,block[1]+1,BLock-2,BLock-2))          #Drawing snake
        
        pygame.draw.rect(screen,(255,0,0),(food[0]+(20-food_bl)//2,food[1]+(20-food_bl)//2,food_bl,food_bl))  #drawing foods
        score_text=soz.render(f'Score {score}',True,(255,255,255))
        screen.blit(score_text,(5,5))
        
        level = score // 10 + 1
        level_text=soz.render(f'Level {level}',True,(255,255,255))
        screen.blit(level_text,(250,5))
        timer=soz.render(f'{5-(now-food_spawn_time)//1000}',True,(255,0,0))
        screen.blit(timer,(food[0]+(20-food_bl)//2,food[1]+(20-food_bl)//2-20))     #words in game
    else:
        keys=pygame.key.get_pressed()
        screen.blit(bg,(0,0))
        screen.blit(lose_photo,(160,100))
        lose_word=soz.render(f'Score: {score}',True,(255,255,255))
        screen.blit(lose_word,(155,200))
        retry_word=soz.render('R - retry',True,(255,0,0))
        screen.blit(retry_word,(155,240))
        level_word=soz.render(f'Level: {level}',True,(255,255,255))
        screen.blit(level_word,(155,220))                                  #words in menu
        quit_word=soz.render('Q - quit',True,(255,0,0))
        screen.blit(quit_word,(155,260))
        if keys[pygame.K_r] :
            gameplay=True
            score=0
            level=1
            snake=[[200,200],[180,200],[160,200]]
            direction='RIGHT'
            food,food_bl=spawn_food()
            food_spawn_time=pygame.time.get_ticks()          #restart all variables
        elif keys[pygame.K_q]:
            running=False
            pygame.quit()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
        if event.type==pygame.KEYDOWN and gameplay:
            if event.key==pygame.K_LEFT and direction!='RIGHT':
                direction='LEFT'
            if event.key==pygame.K_UP and direction!='DOWN':
                direction='UP'
            if event.key==pygame.K_RIGHT and direction!='LEFT':
                direction='RIGHT'
            if event.key==pygame.K_DOWN and direction!='UP':                 #changing direction
                direction='DOWN'
            
            


