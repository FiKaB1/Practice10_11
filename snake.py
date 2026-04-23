import pygame
import random
time=pygame.time.Clock()
pygame.init()
screen=pygame.display.set_mode((400,400))
pygame.display.set_caption('Snake Game')
icon=pygame.image.load('images\icon_snake.png')
bg=pygame.image.load('images\snake_bg.png')
lose_photo=pygame.image.load('images\snake.png')
pygame.display.set_icon(icon)
running=True
gameplay=True
BLock=20
snake=[[200,200],[180,200],[160,200]]
direction='RIGHT'

soz=pygame.font.Font('fonts\\font.ttf',15)
score=0
def spawn_food():
    while True:
        f=[random.randint(0,19)*BLock,random.randint(0,19)*BLock]
        if f not in snake:
            return f
food=spawn_food()
while running:
    time.tick(10)
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
            head[1]+=BLock
        snake.insert(0,head)
        if head==food:
            food=spawn_food()
            score+=1
        else:
            snake.pop()
        if head[0]<0 or head[0]>=400 or head[1]<0 or head[1]>=400 or head in snake[1:]:
            gameplay=False
        for i,block in enumerate(snake):
            if i==0:
                pygame.draw.rect(screen,(95, 153, 245),(block[0]+1,block[1]+1,BLock-2,BLock-2))
            else:
                pygame.draw.rect(screen,(0, 58, 150),(block[0]+1,block[1]+1,BLock-2,BLock-2))
        pygame.draw.rect(screen,(255,0,0),(food[0],food[1],BLock,BLock))
        score_text=soz.render(f'Score {score}',True,(255,255,255))
        screen.blit(score_text,(5,5))
    else:
        keys=pygame.key.get_pressed()
        screen.blit(bg,(0,0))
        screen.blit(lose_photo,(160,100))
        lose_word=soz.render(f'Score: {score}',True,(255,255,255))
        screen.blit(lose_word,(155,200))
        retry_word=soz.render('R - retry',True,(255,0,0))
        screen.blit(retry_word,(155,220))
        if keys[pygame.K_r] :
            gameplay=True
            score=0
            snake=[[200,200],[180,200],[160,200]]
            direction='RIGHT'
            food=spawn_food()
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
            if event.key==pygame.K_DOWN and direction!='UP':
                direction='DOWN'
            
            


