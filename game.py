#!/usr/bin/python
# 'Game' class polls moves from two agents and applies the moves they return.

from agent import Agent
from cliagent import CLIAgent
from pycolony import pycolony
from colors import bg,bc
import copy,colors

class Game(object):

	# pass two Agents and a pycolony instance
	def __init__(self, ag1, ag2, pc):
		self.ag1 = ag1
		self.ag2 = ag2
		self.pc = pc

		self.turn = self.ag1

	def next_turn(self):

		# print
		print('\n' + self.pc.colors[self.pc.turn]+'Player '+str(self.pc.turn)+'\'s turn'+bg.endc+'\n')
		self.pc.p()

		# prompt
		move = self.ag1.getmove(copy.copy(self.pc))

		# apply
		self.pc.move(move[0],move[1])

		# swap turns
		if self.turn == self.ag1:
			self.turn = self.ag2
		else:
			self.turn = self.ag1

	def loop(self):
		if not isinstance(self.ag1,Agent) or not isinstance(self.ag2,Agent):
			print('Error. Both agents must inherit Agent in the Game class.')
			return False

		try:
			while True:
				self.next_turn()
				if self.pc.isover(): break

		except KeyboardInterrupt,SystemExit:
			print(bc.red + 'Exiting' + bc.endc)

		return True

def main():
	ag1 = CLIAgent()
	ag2 = CLIAgent()

	pc = pycolony()
	pc.num_players = 2
	pc.setcorners()

	g = Game(ag1,ag2,pc)
	g.loop()

if __name__ == '__main__': main()
