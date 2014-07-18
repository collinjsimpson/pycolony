#!/usr/bin/python

# collinjsimpson 2014
# pycolony: A Python implementation of the strategy game "Colony" released by Midnight Synergy.

import sys
from colors import bg,bc

class pycolony:
	def __init__(self):
		self.__init__(10,10)
	def __init__(self,rows,cols):
		self.grid = {}
		self.rows = rows
		self.cols = cols
		self.new_tiles = {} # keeps track of the latest map changes

		self.colors = [bg.blue, bg.red, bg.green]
		self.color_blind = False

		self.turn = 0 # whose turn it is
		self.num_players = 2 # number of players
	
	# this mode disables move history (self.new_tiles)
	def set_colorblind(self,color_blind):
		self.color_blind = color_blind

	# attempt to move from cell 'src' to cell 'tar', where src and tar are tuples in form (r,c)
	def move(self,src,tar):
		if src not in self.grid: # check if src tile empty
			sys.stderr.write('Error. No ball at the specified source tile.\n')
			return 1
		elif tar in self.grid: # check if tar tile empty
			sys.stderr.write('Error. A ball exists at the target tile.\n')
			return 2
		elif self.grid[src] != self.turn:
			sys.stderr.write('Error. Players must move pieces they own.\n')
			return 3

		# check distance moved for action
		xdist = abs(src[0]-tar[0])
		ydist = abs(src[1]-tar[1])
		dist = xdist + ydist

		if dist == 0: # no movement
			sys.stderr.write('Error. The source and target tiles are the same.\n')
			return 4
		elif xdist <= 1 and ydist <= 1: # clone
			self.clear_new_tiles()
			self.grid[tar] = self.grid[src]
			self.new_tiles[src] = self.colors[self.turn] + '#' + bg.endc
			self.new_tiles[tar] = self.colors[self.turn] + '+' + bg.endc
		elif xdist <= 2 and ydist <= 2: # jump
			self.clear_new_tiles()
			self.grid[tar] = self.grid[src]
			self.new_tiles[src] = bc.white + '#' + bc.endc
			self.new_tiles[tar] = self.colors[self.turn] + '+' + bg.endc
			del self.grid[src]
		else: # dist > 2; too far
			sys.stderr.write('Error. The target tile is too far away.\n')
			return 5

		# convert all adjacent tiles
		for r in range(-1,2):
			for c in range(-1,2):
				if r == 0 and c == 0: continue
				t = (tar[0]+r,tar[1]+c)
				if t in self.grid and self.grid[t] != self.turn:
					self.grid[t] = self.turn
					self.new_tiles[t] = self.colors[self.turn] + 'o' + bg.endc
		self.next_turn()

	# cycle turns
	def next_turn(self):
		self.turn = (self.turn + 1) % self.num_players

	# print grid
	def p(self):
		for r in range(0,self.rows):
			for c in range(0,self.cols):
				if self.color_blind:
					if (r,c) not in self.grid:
						sys.stdout.write('.')
					else:
						sys.stdout.write(str(self.grid[(r,c)]))

				elif (r,c) in self.new_tiles:
					sys.stdout.write(self.new_tiles[(r,c)])
				elif (r,c) in self.grid:
					sys.stdout.write(self.colors[self.grid[(r,c)]] + '.' + bg.endc)
				else:
					sys.stdout.write('.')
			sys.stdout.write('\n')

	# allows you to erase the latest event history to print a clean board state
	def clear_new_tiles(self):
		self.new_tiles = {}

def main():
	p = pycolony(10,10)
	#p.set_colorblind(True) # use this on windoze

	p.grid[(0,0)] = 0
	p.grid[(9,9)] = 1
	p.grid[(7,7)] = 0
	p.grid[(7,6)] = 0
	p.grid[(8,6)] = 0
	p.grid[(8,9)] = 0
	p.p()

	p.move((0,0),(1,1))
	print('')
	p.p()

	p.move((9,9),(8,7))
	print('')
	p.p()

if __name__ == '__main__': main()
