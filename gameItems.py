import math, pygame, gameAI

gravity = 100
planetFont = pygame.font.SysFont('Sans',27)

class Player(object):
	color, activecolor = (32,32,32),(128,128,128)
	ships = []
	score = 0
	controller = gameAI.controller()
	name = "Player"
	
	def __init__(self,name = "Player", color = (32,32,32), controller = gameAI.Random()):
		self.name = name
		self.color = color
		self.activecolor = (color[0]/2+128,color[1]/2+128,color[2]/2+128)
		self.score = 0
		self.controller = controller
		
	def addship(self, x, y):
		self.ships.append(Ship(self,x,y))
		
	def tick(self, universe, params = {}):
		for s in self.ships:
			for planet in universe:
				s.accelerateTo(planet)
			
			s.tick(universe)
			
			#Edge action is to stop going off the screen and allow the planets to re-attract ships
			
			if s.posX > params["width"]  or s.posX < 0: s.veloX = 0 
			if s.posY > params["height"] or s.posY < 0: s.veloY = 0

	
	
		shipIndex = 0
		while shipIndex <= len(self.ships)-1:
			if self.ships[shipIndex].active == False:
				del(self.ships[shipIndex])
				shipIndex = 0
			else:
				shipIndex += 1
		
		self.score = len(self.ships)
		for planet in universe: 
			if planet.owner.name == self.name:
				self.score += planet.ships
	

class Planet(object):
	owner = Player()
	pos = (0,0)
	mass = 100
	ships = 0
	progress = 0
	def __init__(self, x,y):
		self.pos = (x,y)
	
	def tick(self):

		if self.progress % (int(self.ships**2*1.5)+30) == 0:
			self.progress = 1	
			self.ships+=1
		else:
			self.progress += 1
	
	def draw(self,windowSurfaceObj):
		pygame.draw.circle(windowSurfaceObj,self.owner.color,self.pos,20,0)
		planetNumObj = planetFont.render(str(self.ships),False,self.owner.activecolor)
		numRectObj = planetNumObj.get_rect()
		numRectObj.topleft = (self.pos[0]-15,self.pos[1]-15)
		numRectObj.bottomright = (self.pos[0]+15,self.pos[1]+15)
		windowSurfaceObj.blit(planetNumObj,numRectObj)

	
class Ship(object):
	
	owner = None
	posX, posY = 0,0
	active = True
	_lastAngle, accelX, accelY, veloX, veloY = 0,0,0,0,0
	
	def __init__(self,owner,x,y):
		self.owner = owner
		self.posX = x
		self.posY = y
	
	def angle(self):
		if veloX == 0 and veloY == 0:
			return self._lastAngle
		else:

			self._lastAngle = math.tan(veloY/veloX)
			return self._lastAngle
			
	def getPoints(self):
		#TODO: have the ships rotate based on their direction
		return ((self.posX,self.posY-5),(self.posX-5,self.posY+5),(self.posX,self.posY+2),(self.posX+5,self.posY+5))
		
	def tick(self, universe):
	 if self.active:
		for p in universe:
			distance = math.sqrt((self.posX - p.pos[0]) ** 2+(self.posY - p.pos[1]) ** 2)
			if distance < 20:
				if p.owner == self.owner:
					p.ships += 1
				else:
					p.ships -= 1
				if p.ships < 0:
					p.owner = self.owner
					p.ships = 0
					p.progress = 0
				self.active = False
		def sign(n):
			if n < 0:
				return -1
			elif n > 0:
				return 1
			else:
				return 0

		self.veloX += self.accelX
		self.veloY += self.accelY
		self.posX += math.pow(abs(self.veloX),1.0/3)*sign(self.veloX)
		self.posY += math.pow(abs(self.veloY),1.0/3)*sign(self.veloY)
		self.accelX = 0
		self.accelY = 0

	def accelerateTo(self,planet):
		return self._accelerateTo(planet.pos[0],planet.pos[1],planet.mass)	
		
	def _accelerateTo(self,x,y,mass):
		
		distance = (self.posX - x) ** 2+(self.posY - y) ** 2
		if distance > 500:
			force = gravity * (mass / distance)

		
			if self.posY - y > 0:
				angle = math.atan((x - self.posX)/(y - self.posY))+math.pi
			elif self.posY - y < 0:
				angle = math.atan((x - self.posX)/(y - self.posY))
			elif self.posX - x > 0:
				angle = 0
			else:
				angle = math.pi
			

		
			self.accelX += force * math.sin(angle)
			self.accelY += force * math.cos(angle)
	