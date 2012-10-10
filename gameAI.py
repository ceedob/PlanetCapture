class controller(object):
	def tick(player, universe, params={}):
		pass
		
class Player(controller):
	mouseX, mouseY = 0,0
	mouseDown = False
	def updateInput(inputEvent={}):
		try:
			Player.mouseX, Player.mouseY = inputEvent["mousePosition"]
		except IndexError:
			pass
		try:
			Player.mouseDown = inputEvent["mouseButton"]
			
		except IndexError:
			pass
		try:
			pass 
		except IndexError:
			pass	
	def tick(player, universe, params={}):
		pass
	
class Random(controller):
	def tick(player, universe, params={}):
		pass
	
class Target(controller):
	def tick(player, universe, params={}):
		pass
	