import pygame, sys, math, random
from pygame.locals import *


####################################
###          SETUP GAME          ###
####################################

pygame.init()
fpsClock = pygame.time.Clock()

from gameItems import *

def sign(n):
	if n < 0:
		return -1
	elif n > 0:
		return 1
	else:
		return 0


windowSurfaceObj = pygame.display.set_mode((0,0))
pygame.display.set_caption("Planet Capture")

mouseX, mouseY = 0, 0

cursorBoxX, cursorBoxY = 0, 0




players = [Player("Chris",(0,0,255)),Player("AI1",(255,0,0)),Player("CPU",(0,255,0))]
			

planets = []
for planet in range(len(players*2)):
	planets.append(Planet(random.randint(100,windowSurfaceObj.get_width()-100),random.randint(100,windowSurfaceObj.get_height()-100)))


#planets = [{"pos":(400,500),"owner":"Computer","color":(200,200,200),"ships":0,"progress":0},{"pos":(700,150),"owner":"Player","color":(0,0,255),"ships":5,"progress":0}]
#players = {"Player":{"color":(0,0,255),"active":(128,128,255), "ships":[{"px":700,"py":200,"vx":-1,"vy":0,"ax":.1,"ay":3,"ang":0}]},"Computer":{"color":(255,0,0),"active":(255,128,128), "ships":[]}}



while True:

####################################
###    POLL AND HANDLE EVENTS    ###
####################################

	for event in pygame.event.get():
		if   event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			pass
		elif event.type == KEYUP:
			players[0].addship(random.randint(50,windowSurfaceObj.get_width()-50),random.randint(50,windowSurfaceObj.get_height()-50))
			players[1].addship(random.randint(50,windowSurfaceObj.get_width()-50),random.randint(50,windowSurfaceObj.get_height()-50))
			players[2].addship(random.randint(50,windowSurfaceObj.get_width()-50),random.randint(50,windowSurfaceObj.get_height()-50))
			pass
		elif event.type == MOUSEMOTION:
			mouse = pygame.mouse.get_pos()
			mouseX = mouse[0]
			mouseY = mouse[1]
			
		elif event.type == MOUSEBUTTONUP:
			pass
			
		elif event.type == MOUSEBUTTONDOWN:
			pass
		elif event.type == JOYAXISMOTION:
			pass
			

####################################
###     UPDATE GAME ELEMENTS     ###
####################################

	for p in planets:
		p.tick()
	for ship in players[0].ships:
		if ship.owner == players[0]:ship._accelerateTo(mouseX, mouseY, 1000)		
	for player in players:
		for s in player.ships:
			for planet in planets:
				s.accelerateTo(planet)
			
			s.tick(planets)
			
			if s.posX > windowSurfaceObj.get_width()  or s.posX < 0: s.veloX = 0
			if s.posY > windowSurfaceObj.get_height() or s.posY < 0: s.veloY = 0
			#s.posY = s.posY % (windowSurfaceObj.get_height())
			
			#s['px'] = (s['px'] + s['vx']) 
			#s['py'] = (s['py'] + s['vy']) % (windowSurfaceObj.get_height())
			#s['vx'] = (s['vx']+s['ax'])*0.99
			#s['vy'] = (s['vy']+s['ay'])*0.99
			##s['ax'] = s['ax']*-sign(s['vx'])
			##s['ay'] = s['ay']*-sign(s['vy'])
			#s['ang'] = math.tan(s['vy']/s['vx'])
			
			
			
####################################
###      DRAW GAME SURFACE       ###
####################################


	windowSurfaceObj.fill((0,0,0))

	for p in players:
		for s in p.ships:
			if s.active: pygame.draw.polygon(windowSurfaceObj,s.owner.color,s.getPoints())
			#pygame.draw.polygon(windowSurfaceObj,players[p]["color"],((s["px"]+5*math.sin(s['ang']),s["py"]+5*math.cos(s['ang'])),(s["px"]+5*math.sin(s['ang']+math.pi/3),s["py"]+5*math.cos(s['ang']+math.pi/3)),(s["px"]+5*math.sin(s['ang']-math.pi/3),s["py"]+5*math.cos(s['ang']-math.pi/3)))) 
		
	for p in planets:
		#draw planets
		p.draw(windowSurfaceObj)
		

	pygame.display.update()
	fpsClock.tick(30)