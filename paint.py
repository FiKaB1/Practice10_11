import pygame
import math
pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((1500,800))
pygame.display.set_caption('Paint')
icon=pygame.image.load('images\icon_paint.png')
eraser=pygame.image.load('images\eraser.png')
clean=pygame.image.load('images\clean.png')
pencil=pygame.image.load('images\pencil.png')
soz=pygame.font.Font('fonts\\font.ttf',30)
rect=pygame.image.load('images\\rectangle.png')
circle=pygame.image.load('images\circle.png')
square=pygame.image.load('images\square.png')
etriangle=pygame.image.load('images\etriangle.png')
rtriangle=pygame.image.load('images\\rtriangle.png')
rhombus=pygame.image.load('images\\rhombus.png')

eraser_rect=eraser.get_rect(topleft=(100,5))
clean_rect=clean.get_rect(topleft=(100,50))
pencil_rect=pencil.get_rect(topleft=(250,10))

plus_rect=pygame.Rect(350,10,30,30)
minus_rect=pygame.Rect(350,50,30,30)
pygame.display.set_icon(icon)
running=True
red_rect=pygame.Rect(500,10,20,20)
green_rect=pygame.Rect(530,40,20,20)
blue_rect=pygame.Rect(560,70,20,20)
yellow_rect=pygame.Rect(530,10,20,20)
ligblue_rect=pygame.Rect(560,10,20,20)
pink_rect=pygame.Rect(500,40,20,20)
black_rect=pygame.Rect(560,40,20,20)
purple_rect=pygame.Rect(500,70,20,20)
orange_rect=pygame.Rect(530,70,20,20)

canvas=pygame.Surface((1500,800))
canvas.fill((255,255,255))
color=(0,0,0)
size=3
last_pos=None

mode='Pencil'
start_pos=None
rect_rect=pygame.Rect(750,10,80,80)
circle_rect=pygame.Rect(860,10,80,80)
square_rect=pygame.Rect(970,10,80,80)
rtriangle_rect=pygame.Rect(1080,10,80,80)
etriangle_rect=pygame.Rect(1190,10,80,80)
rhomub_rect=pygame.Rect(1300,10,80,80)

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
        
        if event.type==pygame.MOUSEBUTTONDOWN:
            if plus_rect.collidepoint(event.pos):
                size=min(30,size+1)
            elif minus_rect.collidepoint(event.pos):
                size=max(1,size-1)
            elif event.button==1:
                if rect_rect.collidepoint(event.pos):
                    mode='Rect'
                
                elif circle_rect.collidepoint(event.pos):
                    mode='Circle'
               
                elif square_rect.collidepoint(event.pos):
                    mode='Square'
                
                elif rtriangle_rect.collidepoint(event.pos):
                    mode='Rtriangle' 
                
                elif etriangle_rect.collidepoint(event.pos):
                    mode='Etriangle'

                elif rhomub_rect.collidepoint(event.pos):
                    mode='Rhomub'
                
                elif mode in ['Rect','Circle','Square','Rtriangle','Etriangle','Rhomub'] and event.pos[1]>100:
                    start_pos=event.pos
        if event.type==pygame.MOUSEBUTTONUP:
            if event.button==1:
                if start_pos and event.pos[1]>100:
                    if mode=='Rect':
                        x=min(event.pos[0],start_pos[0])
                        y=min(event.pos[1],start_pos[1])
                        h=abs(event.pos[1]-start_pos[1])
                        w=abs(event.pos[0]-start_pos[0])
                        pygame.draw.rect(canvas,color,(x,y,w,h))
                        start_pos=None
                    elif mode=='Circle':
                        cx=(start_pos[0]+event.pos[0])//2
                        cy=(start_pos[1]+event.pos[1])//2
                        r=min(abs(event.pos[0]-cx),abs(event.pos[1]-cy))
                        pygame.draw.circle(canvas,color,(cx,cy),r)
                        start_pos=None
                    elif mode=='Square':
                        x=min(event.pos[0],start_pos[0])
                        y=min(event.pos[1],start_pos[1])
                        a=min(abs(event.pos[0]-start_pos[0]),abs(event.pos[1]-start_pos[1]))
                        pygame.draw.rect(canvas,color,(x,y,a,a))
                        start_pos=None
                    elif mode=='Rtriangle':
                        a=(start_pos[0],start_pos[1])
                        b=(start_pos[0],event.pos[1])
                        c=(event.pos[0],event.pos[1])
                        pygame.draw.polygon(canvas,color,[a,b,c])
                        start_pos=None
                    elif mode=='Etriangle':
                        a=abs(event.pos[0]-start_pos[0])
                        h=int(a*math.sqrt(3)/2)
                        a1=abs((event.pos[0]+start_pos[0]))//2,abs(event.pos[1]-h)
                        a2=(start_pos[0], event.pos[1])
                        a3=(event.pos[0], event.pos[1])
                        pygame.draw.polygon(canvas,color,[a1,a2,a3])
                        start_pos=None
                    elif mode=='Rhomub':
                        a=((start_pos[0]+event.pos[0])//2,start_pos[1])
                        b=(start_pos[0],(start_pos[1]+event.pos[1])//2)
                        c=((start_pos[0]+event.pos[0])//2,event.pos[1])
                        d=(event.pos[0],(start_pos[1]+event.pos[1])//2)
                        pygame.draw.polygon(canvas,color,[a,b,c,d])
                        start_pos=None

    screen.blit(canvas,(0,0))
    
    pygame.draw.line(screen,(192, 192, 192),(0,50),(1500,50),101)
    pygame.draw.rect(screen,(255,0,0),(500,10,20,20))
    pygame.draw.rect(screen,(0,255,0),(530,40,20,20))
    pygame.draw.rect(screen,(0,0,255),(560,70,20,20))
    pygame.draw.rect(screen,(255,255,0),(530,10,20,20))
    pygame.draw.rect(screen,(0,255,255),(560,10,20,20))
    pygame.draw.rect(screen,(255,0,255),(500,40,20,20))
    pygame.draw.rect(screen,(0,0,0),(560,40,20,20))
    pygame.draw.rect(screen,(128, 15, 209),(500,70,20,20))
    pygame.draw.rect(screen,(255,128,0),(530,70,20,20))
    pygame.draw.rect(screen,color,(590,10,80,80))
    screen.blit(eraser,(100,5))
    screen.blit(clean,(100,50))
    screen.blit(pencil,(250,10))
    pygame.draw.rect(screen,(105, 105, 105),(350,10,30,30))
    pygame.draw.rect(screen,(105, 105, 105),(350,50,30,30))
    plus=soz.render('+',True,(217,217,217))
    screen.blit(plus,(355,7))
    minus=soz.render('-',True,(217,217,217))
    screen.blit(minus,(360,43))
    size_soz=soz.render(f'{size}',True,(105, 105, 105))
    screen.blit(size_soz,(410,30))


    
    pygame.draw.rect(screen,(168, 168, 168),(750,10,80,80))
    pygame.draw.rect(screen,(168, 168, 168),(860,10,80,80))
    pygame.draw.rect(screen,(168, 168, 168),(970,10,80,80))
    pygame.draw.rect(screen,(168, 168, 168),(1080,10,80,80))
    pygame.draw.rect(screen,(168, 168, 168),(1190,10,80,80))
    pygame.draw.rect(screen,(168, 168, 168),(1300,10,80,80))
    screen.blit(rect,(758,18))
    screen.blit(circle,(868,18))
    screen.blit(square,(978,18))
    screen.blit(rtriangle,(1088,18))
    screen.blit(etriangle,(1198,18))
    screen.blit(rhombus,(1308,18))



    mouse=pygame.mouse.get_pos()
    if start_pos:

        if mode=='Rect':
            x=min(mouse[0],start_pos[0])
            y=min(mouse[1],start_pos[1])
            w=abs(mouse[0]-start_pos[0])
            h=abs(mouse[1]-start_pos[1])
            pygame.draw.rect(screen,color,(x,y,w,h))
        elif mode=='Circle':
            cx=(mouse[0]+start_pos[0])//2
            cy=(mouse[1]+start_pos[1])//2
            r=min(abs(mouse[0]-start_pos[0]),abs(mouse[1]-start_pos[1]))//2
            pygame.draw.circle(screen,color,(cx,cy),r)
        elif mode=='Square':
            x=min(mouse[0],start_pos[0])
            y=min(mouse[1],start_pos[1])
            a=min(abs(mouse[0]-start_pos[0]),abs(mouse[1]-start_pos[1]))
            pygame.draw.rect(screen,color,(x,y,a,a))
        elif mode=='Rtriangle':
            a=[start_pos[0],start_pos[1]]
            b=[start_pos[0],mouse[1]]
            c=[mouse[0],mouse[1]]
            pygame.draw.polygon(screen,color,[a,b,c])
        elif mode=='Etriangle':
            a=abs(mouse[0]-start_pos[0])
            h=int(a*math.sqrt(3)/2)
            a1=abs((mouse[0]+start_pos[0]))//2,abs(mouse[1]-h)
            a2=(start_pos[0], mouse[1])
            a3=(mouse[0], mouse[1])
            pygame.draw.polygon(screen,color,[a1,a2,a3])
        elif mode=='Rhomub':
            a=((start_pos[0]+mouse[0])//2,start_pos[1])
            b=(start_pos[0],(start_pos[1]+mouse[1])//2)
            c=((start_pos[0]+mouse[0])//2,mouse[1])
            d=(mouse[0],(start_pos[1]+mouse[1])//2)
            pygame.draw.polygon(screen,color,[a,b,c,d])
    if pygame.mouse.get_pressed()[0]:
        if red_rect.collidepoint(mouse):
            color=(255,0,0)
        elif green_rect.collidepoint(mouse):
            color=(0,255,0)
        elif blue_rect.collidepoint(mouse):
            color=(0,0,255)
        elif yellow_rect.collidepoint(mouse) :
            color=(255,255,0)
        elif ligblue_rect.collidepoint(mouse) :
            color=(0,255,255)
        elif pink_rect.collidepoint(mouse):
            color=(255,0,255)
        elif black_rect.collidepoint(mouse) :
            color=(0,0,0)
        elif purple_rect.collidepoint(mouse):
            color=(128, 15, 209)
        elif orange_rect.collidepoint(mouse):
            color=(255,128,0)
        elif eraser_rect.collidepoint(mouse):
            color=(255,255,255)
        elif clean_rect.collidepoint(mouse):
            canvas.fill((255,255,255))
        elif pencil_rect.collidepoint(mouse):
            color=(0,0,0)
            mode='Pencil'
        elif mouse[1]>100 and mode=='Pencil':
            if last_pos == None:
                last_pos = mouse
            pygame.draw.line(canvas,color,last_pos,mouse,size)
            
            
            last_pos = mouse
    else:
        last_pos=None
        
    pygame.display.update()

    
