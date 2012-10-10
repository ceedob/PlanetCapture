import random
from pygame.locals import *
class controller(object):
	@staticmethod
	def tick(player, universe, params={}):
		pass
		
class Human(controller):
	mouseX, mouseY = 0,0
	mouseDown, unHandledClick = False, False

	@staticmethod	
	def runEvent(event):
		if event.type == KEYDOWN:
			pass
		elif event.type == KEYUP:
			pass
			
		elif event.type == MOUSEMOTION:
			Human.mouseX, Human.mouseY = event.pos
		elif event.type == MOUSEBUTTONUP:
			Human.mouseX, Human.mouseY = event.pos
			if event.button in (1,2,3):
				Human.mouseDown = False					

		elif event.type == MOUSEBUTTONDOWN:
			Human.mouseX, Human.mouseY = event.pos
			if event.button in (1,2,3):
				Human.mouseDown, Human.unHandledClick = True, True
			
	

	
	@staticmethod
	def tick(player, universe, params={}):
		if Human.unHandledClick:
			Human.unHandledClick = False
		for ship in player.ships:
			ship._accelerateTo(Human.mouseX, Human.mouseY, 1000)
			for planet in universe:
				ship.accelerateTo(planet)
			
			ship.tick(universe)

	
class RandomAI(controller):
	@staticmethod
	def tick(player, universe, params={}):
		for ship in player.ships:
			for planet in universe:
				for iterations in range(10):
					ship.accelerateTo(planet)
			
			ship.tick(universe)
			
	
class Target(controller):
	@staticmethod
	def tick(player, universe, params={}):
		pass
	