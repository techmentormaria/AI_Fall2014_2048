#!/usr/bin/env python
#coding:utf-8

#!/usr/bin/env python
#coding:utf-8

from random import randint
from BaseAI import BaseAI
from PlayerAI import PlayerAI
from AlphaBetaPruning import AlphaBetaPruning

class ComputerAI(BaseAI):
	def getMove(self, grid):
		result = self.alphaBetaSearch(grid)
		return result

	def alphaBetaSearch(self, grid):
		cells = grid.getAvailableCells()
		
		#IF NOT COMPUTER AI
		#return cells[randint(0, len(cells) - 1)] if cells else None
		
		cell = 0
		abp = AlphaBetaPruning()
		
		alpha = {'score': float("-inf"), 'direction': -1}
		beta = {'score': float("inf"), 'direction': -1} 
		result = {'score': float("inf"), 'direction': -1}
		for c in cells:
			newGrid = grid.clone()
			newGrid.insertTile(c, abp.getNewTileValue())
			value = abp.maxValue(newGrid, 2, alpha, beta, grid, None)
			if value['score'] < result['score']:
				result = value
				cell = c
		return cell
		
