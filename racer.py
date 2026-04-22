import pygame
import random
clock=pygame.time.Clock()
pygame.init()

screen=pygame.display.set_mode((341,640),flags=pygame.NOFRAME)
icon=pygame.image.load('images\icon_car.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Racer Game')

bg=pygame.image.load('images\\bg_forrace.png')
car=pygame.image.load('images\\car.png')
soz=pygame.font.Font('fonts\\font.ttf',25)
running=True
lose_soz=soz.render('Sen Utyldyn',True,(186, 2, 45))
replay_soz=soz.render('Qaita Oinau',True,(207, 186, 2))  #they are for lose label
replay_soz_rect=replay_soz.get_rect(topleft=(70,285))
exit_soz=soz.render('Shygu',True,(207, 186, 2))
exit_soz_rect=exit_soz.get_rect(topleft=(126,330))

cars=[
    pygame.image.load('images\car1.png'),
    pygame.image.load('images\car2.png'),
    pygame.image.load('images\car3.png'),
    pygame.image.load('images\car4.png')
]
ncars=[
    pygame.image.load('images\\ncar1.png'),
    pygame.image.load('images\\ncar2.png'),
    pygame.image.load('images\\ncar3.png'),
    pygame.image.load('images\\ncar4.png')          #cars are directly with my car,ncars are opposite with my car
]
acc=pygame.image.load('images\\accident.jpg')
bg_y=0
car_x=170
zhaular=[]
nzhaular=[]
#timer for spawn cars
spawn_time=0
spawn_time1=0
spawn_speed1=2000
spawn_speed2=4000
spawn_delay1=random.randint(spawn_speed1,spawn_speed2)
spawn_delay=random.randint(spawn_speed1,spawn_speed2)
gameplay=True


bg_sound=pygame.mixer.Sound('sounds\\car.mp3')
acc_sound=pygame.mixer.Sound('sounds\\accident.mp3')
coin_sound=pygame.mixer.Sound('sounds\coin.mp3')
def sound():
    bg_sound.play(-1)
def acc_so():
    acc_sound.play()
first=True


coin=pygame.image.load('images\coin.png')
coin_list=[
    coin,
    pygame.image.load('images\coin1.png')
]
move_coin=[]
coins=0
spawn_coin=0
spawn_delay2=random.randint(3000,4000)


speed=1
bool_speed1=True
bool_speed2=True
bool_speed3=True

while running:
    dt=clock.tick(60)
    keys=pygame.key.get_pressed()
    if first:
        sound()
        first=False
    
    screen.blit(bg,(0,bg_y))
    screen.blit(bg,(0,bg_y-640))
    if gameplay:
        
        car_rect=car.get_rect(topleft=(car_x,500))
        screen.blit(car,(car_x,500))
        
        bg_y+=speed+6
        if bg_y>=640:               #it is for moving background
            bg_y=0
        
        if keys[pygame.K_LEFT] and car_x>38:
            car_x-=4
        if keys[pygame.K_RIGHT]and car_x<270:
            car_x+=4
        
        
        spawn_time+=dt
        
        spawn_time1+=dt
        coins_to_remove=[]
        for monets in move_coin:
            monets[2]+=3
            screen.blit(monets[0],(monets[1],monets[2]))
            coin_rect=monets[0].get_rect(topleft=(monets[1],monets[2]))
            if car_rect.colliderect(coin_rect):
                if monets[0]==coin_list[0]:
                    coins+=2
                elif monets[0]==coin_list[1]:            #if coin is big +2 if small +1              
                    coins+=1
                coins_to_remove.append(monets)
                coin_sound.play()
        move_coin=[monets for monets in move_coin if monets not in coins_to_remove and monets[2]<700]
        for zhaus in zhaular:
            zhaus[2]+=speed+2
            screen.blit(zhaus[0],(zhaus[1],zhaus[2]))
            zhau_rect=zhaus[0].get_rect(topleft=(zhaus[1],zhaus[2]))
            if zhau_rect.colliderect(car_rect):
                gameplay=False
                acc_so()
                
        zhaular = [zhaus for zhaus in zhaular if zhaus[2] < 700]
        for nzhaus in nzhaular:
            nzhaus[2]+=speed+6
            screen.blit(nzhaus[0],(nzhaus[1],nzhaus[2]))
            nzhau_rect=nzhaus[0].get_rect(topleft=(nzhaus[1],nzhaus[2]))
            if nzhau_rect.colliderect(car_rect):
                gameplay=False
                acc_so()                                  #if my car and enemy cars will do accident gameplay will False
        
        nzhaular=[nzhaus for nzhaus in nzhaular if nzhaus[2]<700]
        if spawn_time>spawn_delay:
            car_zhau=random.choice(cars)
            x=random.choice([185,258])
            zhaular.append([car_zhau,x,-100])
            spawn_time=0
            spawn_delay=random.randint(spawn_speed1,spawn_speed2)            #they help us choice randomly one road and random kind of car
        if spawn_time1>spawn_delay1:
            ncar_zhau=random.choice(ncars)
   
            x1=random.choice([45,115])
            nzhaular.append([ncar_zhau,x1,-100])
            spawn_time1=0
            spawn_delay1=random.randint(spawn_speed1,spawn_speed2)           #they spawn cars in random time and create new random time
        pygame.draw.line(screen,(117, 117, 117),(250,620),(341,620),40)
        screen.blit(coin,(245,600))
        coin_game=soz.render(f'{coins}',True,'Yellow')
        screen.blit(coin_game,(295,606))
        spawn_coin+=dt
        
        if spawn_coin>spawn_delay2:
            coin_road=random.choice([45,115,185,255])
            monet=random.choice(coin_list)
            move_coin.append([monet,coin_road,-100])
            spawn_coin=0
            spawn_delay2=random.randint(3000,4000)

            
        if coins>=10 and coins<20 and bool_speed1:
            speed+=2
            spawn_speed1=1750
            spawn_speed2=2500
            bool_speed1=False
        if coins >=20 and coins<30 and bool_speed2:
            speed+=2
            spawn_speed1=1250
            spawn_speed2=1750
            bool_speed2=False
        if coins >=30  and bool_speed3:
            speed+=3
            spawn_speed1=500
            spawn_speed2=1000
            bool_speed3=False
            

        

    else:
        bg_sound.stop()
        
        screen.blit(acc,(40,70))
        pygame.draw.line(screen,(79, 74, 128),(50,255),(310,255),30)
        screen.blit(lose_soz,(60,240))
        pygame.draw.line(screen,(24, 24, 196),(70,300),(295,300),30)
        screen.blit(replay_soz,replay_soz_rect)
        pygame.draw.line(screen,(24, 24, 196),(126,345),(238,345),30)
        screen.blit(exit_soz,(126,330))
        mouse=pygame.mouse.get_pos()
        if replay_soz_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            zhaular.clear()
            nzhaular.clear()
            move_coin.clear()
            spawn_time=0
            spawn_time1=0
            spawn_coin=0
            spawn_delay1=random.randint(800,2000)
            spawn_delay=random.randint(800,2000) 
            spawn_delay2=random.randint(3000,4000)
            coins=0
            speed=1
            spawn_speed2=4000
            spawn_speed1=2000
            gameplay=True
            first=True
            bool_speed1=True
            bool_speed2=True
            bool_speed3=True
            car_x = 170                                                             #restart all variables
        if exit_soz_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            running=False
            pygame.quit()
        
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
        
            