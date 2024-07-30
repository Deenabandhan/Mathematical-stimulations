import random

import pygame

pygame.init()

display=pygame.display.set_mode((1500,1500))
pygame.display.set_caption("Galton Board")
clock=pygame.time.Clock()
FPS=150
color = (255, 255

, 255)
c1 = (255, 255, 255)

XL=10
XR=990
wallx1=[]
wallx2=[]
wally1=[100,160,220,280]
wally2=[130,190,250,310]

B_img=pygame.image.load("MathLogo-76476912.png")
B_img=pygame.transform.scale(B_img,(50,50))

cdt=[]
for i in range(-100,11001):
    cdt.append(990)
    
class Button:
	def __init__(self,x,y):
		self.img=B_img
		self.rect=self.img.get_rect()
		self.rect.topleft=(x,y)
		self.clicked=False
	def draw(self):
		display.blit(self.img,(self.rect.x,self.rect.y))
		pos=pygame.mouse.get_pos()
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] and not self.clicked:
				self.clicked=True
				#print("ko")
				return(1)
			if not pygame.mouse.get_pressed()[0]:
				self.clicked=False	
		else:
			return(0)
	
class Ball():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.velocity=10
    def draw(self):
        pygame.draw.circle(display,(29,149,229),(self.x,self.y),6)
    def move(self,cur):
        if(cur==0):
        	return(1)
        self.y+=self.velocity
        if(self.y in wally1):
            if(self.x in wallx1):
                self.x=(int)(self.x/10)
                self.x=(self.x)*10+(random.choice([-1,1]))*25
        if (self.y in wally2):
            if (self.x in wallx2):
                #print("yes")
                self.x = (int)(self.x / 10)
                self.x = (self.x) * 10 + (random.choice([-1,1]))*25
        if(self.y>=cdt[(int)(self.x)]):
            cdt[self.x]=self.y-10
            self.velocity=0
            return(1)
        return(0)
def gen():
    for i in range(1, 148, 4):
        pygame.draw.line(display, color, (i * 10, 100), ((i + 1) * 10, 100), 6)
        wallx1.extend([i for i in range(i*10-20,i*20+11)])
    for i in range(3, 150, 4):
        pygame.draw.line(display, color, (i * 10, 130), ((i + 1) * 10, 130), 6)
        wallx2.extend([i for i in range(i * 10-20, i * 10 + 21)])
    for i in range(1, 148, 4):
        pygame.draw.line(display, color, (i * 10, 160), ((i + 1) * 10, 160), 6)
    for i in range(3, 150, 4):
        pygame.draw.line(display, color, (i * 10, 190), ((i + 1) * 10, 190), 6)
    for i in range(1, 148, 4):
        pygame.draw.line(display, color, (i * 10, 220), ((i + 1) * 10, 220), 6)
    for i in range(3, 150, 4):
        pygame.draw.line(display, color, (i * 10, 250), ((i + 1) * 10, 250), 6)
    for i in range(1, 148, 4):
    	pygame.draw.line(display, color, (i * 10, 280), ((i + 1) * 10, 280), 6)
    for i in range(3, 150, 4):
        pygame.draw.line(display, color, (i * 10, 310), ((i + 1) * 10, 310), 6)
    pygame.draw.line(display,(223,32,92),(910,1000),(920,1000),6)
    pygame.draw.line(display,(111,219,36),(860,1000),(870,1000),6)
    pygame.draw.line(display,(22,75,233),(810,1000),(820,1000),6)
    pygame.draw.line(display,(210,35,220),(760,1000),(770,1000),6)
    pygame.draw.line(display,(152,111,103),(710,1000),(720,1000),6)
    pygame.draw.line(display,(63,170,192),(660,1000),(670,1000),6)
    pygame.draw.line(display,(205,220,35),(610,1000),(620,1000),6)
def game(ball,button):
    ord=0
    cur=1
    while True:
        for event in pygame.event.get():
        	if event.type == pygame.QUIT:
                	return
        display.fill((0,0,0))
        gen()
        for i in range(len(ball)):
        	ball[i].draw()
        if(ord<len(ball) and ball[ord].move(cur)==1 ):
        	if(ord%50==0 and ord<203):
            		cur=button.draw()
        	if(cur!=0):
            		ord+=1
        pygame.display.update()
        clock.tick(FPS)

ball=[]
button=Button(1400,10)
for i in range(100):
    ball.append(Ball(750,0))
game(ball,button)
