'''
Created on 24.10.2014

@author: Maria
'''
from BaseAI import BaseAI
import math
from Heuristic import Heuristic
from AlphaBetaPruning import AlphaBetaPruning


class PlayerAI(BaseAI):
    
        
    def getMove(self, grid):
        result  = self.alphaBetaSearch(grid)
        return result['direction']

    def alphaBetaSearch(self, grid):
        
        abp = AlphaBetaPruning()
        
        alpha = {'score': float("-inf"), 'direction': -1 }
        beta = {'score': float("inf"), 'direction': -1 }
        
        moves = grid.getAvailableMoves()
        result = {'score': float("-inf"), 'direction': -1}
        depth = 3
        
        for m in moves: 
            newGrid = grid.clone()
            newGrid.move(m)
            
            value = abp.minValue(newGrid, depth, alpha, beta, grid, m)
            
            if value['score'] > result['score']:
                result = value
                result['direction'] = m
        return result
        
