import pygame, sys, math, random
from pygame.locals import *


####################################
###          SETUP GAME          ###
####################################

pygame.init()
fpsClock = pygame.time.Clock()

scoreFont = pygame.font.SysFont('Sans',17)

from gameItems 	import *
from gameAI		import *

def sign(n):
	if n < 0:
		return -1
	elif n > 0:
		return 1
	else:
		return 0


windowSurfaceObj = pygame.display.set_mode((0,0))
pygame.display.set_caption("Planet Capture")


cursorBoxX, cursorBoxY = 0, 0




players = [Player("Chris",(32,32,200),controller=gameAI.Human),Player("CPU1",(200,32,32)),Player("CPU2",(32,200,32)),Player("CPU3",(32,180,180))]
			

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
			
		else:
			Human.runEvent(event)
			if event.type == MOUSEBUTTONUP:
				for i in range(random.randint(1,len(players))):players[0].addship(random.randint(Human.mouseX-50,Human.mouseX+50),random.randint(Human.mouseY-50,Human.mouseY+50)) 			
				for p in players[1:]:
 					for i in range(random.randint(1,len(players)*2)):p.addship(random.randint(50,windowSurfaceObj.get_width()-50),random.randint(50,windowSurfaceObj.get_height()-50))
# 		elif event.type == KEYDOWN:
# 			pass
# 		elif event.type == KEYUP:
# 			pass
# 		elif event.type == MOUSEMOTION:
# 			inputEvent = {}
# 			inputEvent["mousePosition"] = event.pos
# 
# 			Human.updateInput(inputEvent)
# 			
# 		elif event.type == MOUSEBUTTONUP:
# 			eventdata = {}
# 			eventdata["mousePosition"] = pygame.mouse.get_pos()
# 			if event.button in (1,2,3):
# 				eventdata["mouseButton"] = True					
# 				
# 			Human.updateInput(eventdata)
# 			
# 		elif event.type == MOUSEBUTTONDOWN:
# 			eventdata = {}
# 			eventdata["mousePosition"] = pygame.mouse.get_pos()
# 			if event.button in (1,2,3):
# 				eventdata["mouseButton"] = True					
# 				
# 			Human.updateInput(eventdata)
# 			
# 			for i in range(random.randint(0,len(players))):players[0].addship(random.randint(mouseX-50,mouseX+50),random.randint(mouseY-50,mouseY+50))
# 			for p in players[1:]:
# 				for i in range(random.randint(0,len(players)*2)):p.addship(random.randint(50,windowSurfaceObj.get_width()-50),random.randint(50,windowSurfaceObj.get_height()-50))
# 			
# 		elif event.type == JOYAXISMOTION:
# 			pass
			

####################################
###     UPDATE GAME ELEMENTS     ###
####################################

	for p in planets:
		p.tick()
	
	#for ship in players[0].ships:
		#if ship.owner == players[0]:ship._accelerateTo(Human.mouseX, Human.mouseY, 1000)		
	
	for player in players:
		#for s in player.ships:
		#	for planet in planets:
		#		s.accelerateTo(planet)
		#	
		#	s.tick(planets)
		#	
		#	#Edge action is to stop going off the screen and allow the planets to re-attract ships
		#	
		#	if s.posX > windowSurfaceObj.get_width()  or s.posX < 0: s.veloX = 0 
		#	if s.posY > windowSurfaceObj.get_height() or s.posY < 0: s.veloY = 0
		player.tick(planets, params={"width":windowSurfaceObj.get_width(),"height":windowSurfaceObj.get_height()})

			
			
			
####################################
###      DRAW GAME SURFACE       ###
####################################

	#clear the screen with black
	windowSurfaceObj.fill((0,0,0))
	
	#draw the ships
	for player in players:
		for ship in player.ships:
			if ship.active: pygame.draw.polygon(windowSurfaceObj,ship.owner.color,ship.getPoints())
	#draw the planets		
	for planet in planets:
		planet.draw(windowSurfaceObj)
		
	#draw the scores
	index = 0
	for player in players:
		name  = player.name
		score = player.score
		playerScoreObj = scoreFont.render("%s:%i" % (name,score),False,player.activecolor)
		playerScoreRect = playerScoreObj.get_rect()
		playerScoreRect.topleft = (10,10+30*index)
		windowSurfaceObj.blit(playerScoreObj,playerScoreRect)
		index += 1
		

	pygame.display.update()
	fpsClock.tick(30)