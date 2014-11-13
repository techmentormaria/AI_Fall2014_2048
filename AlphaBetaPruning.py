'''
Created on 28.10.2014

@author: Maria
'''
from BaseAI import BaseAI
import math
from Heuristic import Heuristic

from random import randint

directionVectors = (UP_VEC, DOWN_VEC, LEFT_VEC, RIGHT_VEC) = ((-1, 0), (1, 0), (0, -1), (0, 1))
vecIndex = [UP, DOWN, LEFT, RIGHT] = range(4)



class AlphaBetaPruning(BaseAI):
    def minValue(self, grid, depth, alpha, beta, oldGrid, lastMove):
        #TERMINAL TEST
        if depth == 0:
            return {'score': self.heuristic(grid, oldGrid), 'direction': lastMove}
        
        v = {'score': float("inf"), 'direction': -1 }
        
        cells = grid.getAvailableCells()
        
        for c in cells:
            newGrid = grid.clone()
            newGrid.insertTile(c, self.getNewTileValue())
                
            v = min(v, self.maxValue(newGrid, depth - 1, alpha, beta, grid, lastMove), key=lambda a: a['score'])
            
            if v['score'] <= alpha['score']:
                return v
            if beta['score'] > v['score']:
                beta = v
        return v
        
    def maxValue(self, grid, depth, alpha, beta, oldGrid, lastMove):
        #TERMINAL TEST
        if depth == 0:
            return {'score': self.heuristic(grid, oldGrid), 'direction': lastMove}
    
        if not grid.canMove():
                return {'score': 0, 'direction': lastMove}    
            
        
        v = {'score': float("-inf"), 'direction': -1 }
        
        moves = grid.getAvailableMoves()
        
        for m in moves:
                 
            newGrid = grid.clone()
            newGrid.move(m) 
          
            v = max(v, self.minValue(newGrid, depth - 1, alpha, beta, grid, m), key=lambda a: a['score'])
            
            if v['score'] >= beta['score']:
                return v 
            if alpha['score'] < v['score']:
                alpha = v
            
        return v
    
    def heuristic(self, newGrid, oldGrid):
        h = Heuristic()
        return h.getHeuristicScore(newGrid, oldGrid)
    
    def newTileCheck(self, grid, oldGrid):
        return - self.getNearByScore(grid) + self.heuristic(grid, oldGrid)
    
    def getNewTileValue(self):
        possibleNewTileValue = [2, 4]
        defaultPossibility = 0.7
        possibility = defaultPossibility
        
        if randint(0, 99) < 100 * possibility: 
            return possibleNewTileValue[0] 
        else: 
            return possibleNewTileValue[1]


    
