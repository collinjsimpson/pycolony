#!/usr/bin/python
# This is an agent which reads user input from the keyboard to return game moves

import abc, sys
from agent import Agent

class CLIAgent(Agent):

	def __init__(self):
		pass

	def getmove(self, pc): # pass a copy of the game world to this agent
		# read from keyboard
		print('Input move: [src_r src_c tar_r tar_c]')
		while True:
			sys.stdout.write('> ')
			sys.stdout.flush()
			L = sys.stdin.readline().split()
			if len(L) != 4:
				print('Please specify 4 values')
				continue
			try:
				for i in range(0,len(L)): # convert to ints
					L[i] = int(L[i])
			except:
				print('Each value must be an integer')
				continue # ask for user input again if non-number specified

			src = (L[0],L[1])
			tar = (L[2],L[3])
			if pc.check_move(src,tar):
				#print((src,tar))
				return (src,tar)
			else:
				#print('Illegal move!\n')
				continue

	# not used in CLI Agent
	def reset(self):
		pass

if __name__ == '__main__':
	Agent.register(CLIAgent)
	
	c = CLIAgent()
	print(c)
