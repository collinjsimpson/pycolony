#!/usr/bin/python

import abc
from abc import abstractmethod

# the 'Agent' class returns game moves given a board state.
# Agent's can create their own internal cache throughout a game.
class Agent(object):
	__metaclass__ = abc.ABCMeta

	@abstractmethod
	def getmove(self, colony):
		# this function returns a game action given a current board state
		return

	@abstractmethod
	def reset(self):
		# this function clears any agent cache that may have been previously created
		return
