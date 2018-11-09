from entity import Entity
import libtcodpy as libtcod
from itertools import chain
from copy import deepcopy
from random import randint

## PURPOSE: Handles game logic and updates map entities ##

class GameMap:
	
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.entities = self.initialise_tiles()
	
	## INITIALISES TILES AND RANDOMLY ASSIGNS ALIVE TILES 50/50 ##
	def initialise_tiles(self):
		default = [[Entity(x, y, ' ', libtcod.white) for y in range(self.height)] for x in range(self.width)]
		for y in range(self.height):
			for x in range(self.width):
				flip = randint(0, 1)
				if(flip == 1):
					r = randint(50, 205)
					g = randint(50, 205)
					b = randint(50, 205)
					default[x][y] = Entity(x, y, '#', libtcod.Color(r, g, b))
		return default
	
	## CHECKS FOR CHANGES IN DEAD/ALIVE TILES AND UPDATES ENTITIES ##
	def update_tiles(self):
		newents = deepcopy(self.entities)
		for y in range(self.height):
			for x in range(self.width):
				if(self.is_alive(self.entities[x][y]) and not(self.count_neighbours(x, y) == 2 or self.count_neighbours(x, y) == 3)):
					newents[x][y] = Entity(x, y, ' ', libtcod.white)
				elif((not self.is_alive(self.entities[x][y])) and self.count_neighbours(x, y) == 3):
					r = randint(50, 205)
					g = randint(50, 205)
					b = randint(50, 205)
					newents[x][y] = Entity(x, y, '#', libtcod.Color(r, g, b))
					
		self.entities = newents
		
	def count_neighbours(self, x, y):
		count = 0
		for a in range(x-1, x+2):
			for b in range(y-1, y+2):
				if((not(a == x and b == y)) and (a >= 0 and b >= 0) and (a < self.width and b < self.height) and self.is_alive(self.entities[a][b])):
					count += 1
		return count
		
	def is_alive(self, entity):
		return entity.char == '#'
	
	def get_entities(self):
		return list(chain.from_iterable(self.entities))