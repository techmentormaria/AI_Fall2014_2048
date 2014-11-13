'''
Created on 24.10.2014

@author: Maria
'''
import math

directionVectors = (UP_VEC, DOWN_VEC, LEFT_VEC, RIGHT_VEC) = ((-1, 0), (1, 0), (0, -1), (0, 1))
vecIndex = [UP, DOWN, LEFT, RIGHT] = range(4)

class Heuristic:
    
    def getHeuristicScore(self, newGrid, oldGrid):
        
        score = 0
        
        # (1): actual score
        addScore = newGrid.score
        if addScore > 0:
            addScore = math.log(addScore) / math.log(2)
            
        # (2): empty fields
        # the higher the score, the more important the empty fields
        # highest score * available fields
        empty = 0
        if len(newGrid.getAvailableCells()) > 1:
            empty = math.log(len(newGrid.getAvailableCells())) / math.log(2)
        
        # (3): how close are our numbers?
        close = self.smoothness(newGrid) * math.log(newGrid.getHighestValue()) / math.log(2)
        
        # (4): are we close to a great corner order?
        order = self.getOrderScore(newGrid)
       
        # (5): what is our highest number so far?
        fields = len(newGrid.getAvailableCells())
        emptyFields = 0
        if not fields == 0 and not newGrid.getHighestValue() == 0:
            emptyFields = math.log(newGrid.getHighestValue()) / math.log(2) + newGrid.getHighestValue()
        
        return close * 0.1 + emptyFields * 1 + order * 1.3 + empty * 2.7
        return score
        
            
    
    def getOrderScore(self, grid):

        score = 0
        
        # since there are just 4 rows and 4 columns, I can score it statically
        highestVal = grid.getHighestValue()
        x = 0
        y = 0
        
        # left up corner
        if grid.map[0][0] == highestVal:
            score += highestVal
            x = 0
            y = 0
             
        # left down corner
        if grid.map[3][0] == highestVal:
            score += highestVal
            x = 3
            y = 0
#         
        # right up corner
        if grid.map[0][3] == highestVal:
            score += highestVal
            x = 0
            y = 3
             
        # right down corner
        if grid.map[3][3] == highestVal:
            score += highestVal
            x = 3
            y = 3
            
        return     (math.log(score)) if score > 0 else 0
        
    def smoothness(self, grid):
        smoothness = 0
        freeTiles = 0
        for x in range (0, 4):
            for y in range(0, 4):
                if grid.map[x][y] != 0:
                    #SMOOTHNESS
                    value = math.log(grid.map[x][y]) / math.log(2)
                    
                    vecRange = { 1, 0 , 2, 3 }
      
                    for dir in vecRange:
                        vec = directionVectors[dir]
                        targetCell = grid.findFarthestAway([x, y], vec)
                        targetValue = grid.map[targetCell[0]][targetCell[1]]
                       
                        if targetValue > 0:
                            tValue = math.log(targetValue) / math.log(2)
                            smoothness -= abs(value - tValue)
                    
                        #FREETILE
#                         if grid.map[x][y] == 2:
#                             if not grid.crossBound((x + vec[0], y + vec[1])):
#                                 if grid.map[x + vec[0]][y + vec[1]] == 0:
#                                     freeTiles += 1
        return smoothness + freeTiles           
                        
        
