#!/usr/bin/python

# collinjsimpson 2014
# pycolony: A Python implementation of the strategy game "Colony" originally released by Midnight Synergy.

import sys
from colors import bg,bc

class pycolony(object):
	def __init__(self,rows=10,cols=10):
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

	# is the game over? (no more open tiles)
	def isover(self):
		return len(self.grid) == self.rows * self.cols

	# calculate the current score of the involved players
	def getscore(self):
		scores = [0] * self.num_players
		for r in range(0,self.rows):
			for c in range(0,self.cols):
				if (r,c) in self.grid:
					scores[self.grid[(r,c)]] += 1
		return scores

	# return the player that's in the lead (may want to instead return sorted list)
	def getwinner(self):
		score = self.getscore()
		if len(score) == 0: return -1
		x = 0
		for i in range(1,len(score)):
			if score[i] > score[x]:
				x = i
		return x

	# check if move is valid; in the form ((src_r,src_c), (tar_r,tar_c))
	def check_move(self,src,tar):
		if len(src) != 2 or len(tar) != 2:
			sys.stderr.write('Error. Source and target must contain 2 values.\n')
			return False

		if src[0] < 0 or src[1] < 0 or tar[0] < 0 or tar[1] < 0 or \
			src[0] >= self.rows or src[1] >= self.cols or \
			tar[0] >= self.rows or tar[1] >= self.cols:
				sys.stderr.write('Error. That tile lies outside map boundaries.\n')
				return False

		if src not in self.grid: # check if src tile empty
			sys.stderr.write('Error. No ball at the specified source tile.\n')
			return False
		elif tar in self.grid: # check if tar tile occupied
			sys.stderr.write('Error. A ball exists at the target tile.\n')
			return False
		elif self.grid[src] != self.turn:
			sys.stderr.write('Error. Players must move pieces they own.\n')
			return False

		if src == tar:
			sys.stderr.write('Error. Source and target tiles are the same.\n')
			return False
		 
		# calculate the total distance the player is attempting to move
		xdist = abs(src[0]-tar[0])
		ydist = abs(src[1]-tar[1])
		dist = xdist + ydist

		if xdist > 2 or ydist > 2:
			sys.stderr.write('Error. The target tile is too far away.\n')
			return False
		return True
		
	# attempt to move from cell 'src' to cell 'tar', where src and tar are tuples in form (r,c)
	def move(self,src,tar):

		if self.check_move(src,tar) != True: return False

		# calculate the total distance the player is attempting to move
		xdist = abs(src[0]-tar[0])
		ydist = abs(src[1]-tar[1])
		dist = xdist + ydist

		if xdist <= 1 and ydist <= 1: # clone condition
			self.clear_new_tiles()
			self.grid[tar] = self.grid[src]
			self.new_tiles[src] = self.colors[self.turn] + 's' + bg.endc
			self.new_tiles[tar] = self.colors[self.turn] + 't' + bg.endc
		elif xdist <= 2 and ydist <= 2: # jump condition
			self.clear_new_tiles()
			self.grid[tar] = self.grid[src]
			del self.grid[src]
			self.new_tiles[src] = bc.white + 's' + bc.endc
			self.new_tiles[tar] = self.colors[self.turn] + 't' + bg.endc
		else:
			sys.stderr.write('ERROR! Shouldn\'t have reached this line!')

		# convert all adjacent tiles to the current player's color
		for r in range(-1,2):
			for c in range(-1,2):
				if r == 0 and c == 0: continue
				t = (tar[0]+r,tar[1]+c)
				if t in self.grid and self.grid[t] != self.turn:
					self.grid[t] = self.turn
					self.new_tiles[t] = self.colors[self.turn] + 'o' + bg.endc
		self.next_turn()
		return True

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

	# give one corner to each available player (max 4)
	def setcorners(self):
		cs = [(0,0),(self.rows-1,self.cols-1),(self.rows-1,0),(0,self.cols-1)]
		for i in range(0,min(self.num_players,4)):
			self.grid[cs[i]] = i

def main():
	p = pycolony(10,10)
	#p.set_colorblind(True) # use this on windoze or if colorblind

	p.grid[(0,0)] = 0
	p.grid[(9,9)] = 1
	p.grid[(7,7)] = 0
	p.grid[(7,6)] = 0
	p.grid[(8,6)] = 0
	p.grid[(8,9)] = 0
	p.p()
	print(p.getscore())

	p.move((0,0),(1,1))
	print('')
	p.p()
	print(p.getscore())

	p.move((9,9),(8,7))
	print('')
	p.p()
	print(p.getscore())

if __name__ == '__main__': main()
