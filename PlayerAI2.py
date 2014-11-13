#!/usr/bin/env python
# coding:utf-8

from random import randint
from BaseAI import BaseAI
import math
from Grid import directionVectors
import sys
from Displayer import Displayer

# direction vectors
directionVectors = (UP_VEC, DOWN_VEC, LEFT_VEC, RIGHT_VEC) = ((-1, 0), (1, 0), (0, -1), (0, 1))
vecIndex = [UP, DOWN, LEFT, RIGHT] = range(4)


class PlayerAI(BaseAI):
	
	def getMove(self, grid):
		moves = grid.getAvailableCells()
		
		alpha = {'score': float("-inf"), 'direction': None}
		beta = {'score': float("inf"), 'direction': None}
		
		newGrid = grid.clone()
		
		result = self.alphaBeta(newGrid, 5, alpha, beta, True, None, grid, True)
		#print "RESULT " + str(result)
		return result['direction']
		
		
	
# 	def getMove(self, grid):
# 		# I'm too naive, please change me!
# 		moves = grid.getAvailableMoves()
# 		
# 		#
# 		bestScore = 0
# 		bestMove = 0
# 		isMove = False
# 		i = 0
# 		for m in moves:
# 			print "MOVE"
# 			print m
# 			
# 			newGrid = grid.clone()
# 			newGrid.move(m)
# 			currentScore = self.getHeuristicScore(newGrid, grid.score)
# 			
# 			if currentScore > bestScore or bestScore == 0:
# 				bestScore = currentScore
# 				bestMove = m
# 				isMove = True
# 				i += 1
# 			print "\n"
# 		return  bestMove
		# return moves[randint(0, len(moves) - 1)] if moves else None

	def getNewTileValue(self):
		possibleNewTileValue = [2, 4]
		defaultPossibility = 0.7
		possibility = defaultPossibility
		
		if randint(0, 99) < 100 * possibility: 
			return possibleNewTileValue[0] 
		else: 
			return possibleNewTileValue[1]


	def alphaBeta2(self, grid, depth, a, b, maximizingPlayer, lastMove, oldGrid):
		if depth == 0:
			test = { 'score': self.getHeuristicScore(grid, oldGrid.score), 'direction': lastMove}
			return test
		
		if not grid.canMove():
			return {'score': 0, 'direction': lastMove}
		
		isFirstDepth = False
		if lastMove == None:
			isFirstDepth = True
		
		if maximizingPlayer == True:
			moves = grid.getAvailableMoves()
			for m in moves:
				
				newGrid = grid.clone()
				newGrid.move(m)
				
				if isFirstDepth:
					lastMove = m
				
				ab = (self.alphaBeta(newGrid, depth - 1, a, b, False, lastMove, grid))
				
				if a['score'] < ab['score']:
					a = ab
					print "SCORE " + str(a)
					print lastMove
					print m
					if isFirstDepth:
						lastMove = m
					#lastMove = m
				#if b <= a:
				#	break
				
			return { 'score': a['score'], 'direction': lastMove}
		else:
			try:
				moves = grid.getAvailableCells()
				for c in moves:
					newGrid = grid.clone()
					newGrid.insertTile(c, self.getNewTileValue())
					ab = self.alphaBeta(newGrid, depth - 1, a, b, True, lastMove, grid)
					if b['score'] > ab['score']:
						b = ab
					#if b <= a:
					#	break
				
				return { 'score': b['score'], 'direction': lastMove}
			except: 
				print "Unexpected error:", sys.exc_info()[0]	
	
	
	def alphaBeta(self, grid, depth, a, b, maximizingPlayer, lastMove, oldGrid, first):
		# print "\n\nnew AB!"
		
		if depth == 0:
			test = { 'score': self.getHeuristicScore(grid, oldGrid.score), 'direction': lastMove}
			#print "here is heuristic " + str(test)
			return test
		
		if not grid.canMove():
			return {'score': 0, 'direction': lastMove}
		# if grid.canMove == false -> return 0
		moves = grid.getAvailableMoves()
		# print "depth " + str(depth)
		if maximizingPlayer == True:
			# print moves
			for m in moves:
				#if first:
					#print "\n\nMOVE " + str(m) + "______________________________________________________"
				newGrid = grid.clone()
				newGrid.move(m)
				#print "true moved " + str(m) + " depth " + str(depth)
			
				#displayer = Displayer()
				#displayer.display(newGrid)
				#print "A SCORE " + str(a)	
				ab = (self.alphaBeta(newGrid, depth - 1, a, b, False, m, grid, False))
				
				#print "ab is " + str(ab) + " and depth " + str(depth) 
				#print "a score " + str(a['score'])
				#print "ab score " + str(ab['score'])
					
				
				if a['score'] < ab['score']:
					#print "~~~DEPTH~~~" + str(depth)
					#print "A SCORE " + str(a)
					#print "\nab should be " + str(ab['score'])
					#print "true moved " + str(m) + " depth " + str(depth)
					# print a
					a = ab
					lastMove = m
					
					#if first:
						#print "SCORE " + str(a)
					#print lastMove
						#print m
					#	lastMove = m
						
				#print "BETA " + str(b)	
				if not b['score'] is float("inf"):
					if b['score'] <= a['score']:
						#print "BETA BREAK " + str(b) + " alpha " + str(a)
						break
				# 	print "I'm breaking a " + str(a) + "\n b " + str(b)
				# 	break 
			#print "----a under score " + str(a)
			return { 'score': a['score'], 'direction': lastMove}
		else:
			# print "false"
			moves = grid.getAvailableCells()
			# moves = self.getNewTileValue()
			
			for c in moves:
				newGrid = grid.clone()
				newGrid.insertTile(c, self.getNewTileValue())
				#print "--------------------insert TILE "
				#displayer = Displayer()
				#displayer.display(newGrid)
				ab = self.alphaBeta(newGrid, depth - 1, a, b, True, lastMove, grid, False)
				#ab['score'] += b['score']
				if b['score'] > ab['score']:
					#print "\nfalse ab should be " + str(ab['score'])
					# print "false moved depth " + str(depth)
					# print ab
					b = ab
					# lastMove = m
				# b = min(b, self.alphaBeta(newGrid, depth - 1, a, b, True, m, None), key=lambda p: p[0])
				if b['score'] <= a['score']:
					break
			# print str({ 'score': b, 'direction': lastMove})
			return { 'score': b['score'], 'direction': lastMove}	
	 

    
	def getHeuristicScore(self, newGrid, oldScore):
		score = 0
		
		emptyWeight = 1
		closeWeight = 0
		orderWeight = 1
		scoreWeight = 1
		nearWeight = 0.6
		cornerWeight = 2
		
		debug = False
		# (1): actual score
		addScore = newGrid.score - oldScore
		# print "scc " + str(addScore)
		if addScore > 0:
			addScore = math.log(addScore) / math.log(2)
			
		
		# (2): empty fields
		# the higher the score, the more important the empty fields
		# highest score * available fields
		fields = len(newGrid.getAvailableCells())
		
		emptyFields = math.log(fields * newGrid.getHighestValue()) / math.log(2)
		# (3): how close are our numbers?
		# closescore = self.getCloseNumberScore(newGrid) 
		# score += closescore * 0.5
		# close = self.smoothness(newGrid) * math.log(newGrid.getHighestValue()) / math.log(2)
		# closescore = close
		
		# (4): are we close to a great corner order?
		# order = self.getOrderScore(newGrid)
		order = self.getOrder(newGrid)
		corner = self.getOrderScore(newGrid)
			
		near = self.getNearByScore(newGrid)
		if near == 0:
			near = addScore
		
		
# 		if corner == 0:
# 			nearWeight *= 2
# 			scoreWeight *= 2
# # 		
		
			
		score = corner * cornerWeight + near * nearWeight + scoreWeight * addScore + emptyFields * emptyWeight + order * orderWeight
		# print directionVectors
		
		if debug:
			print "SCORE " + str(scoreWeight * addScore)
			print "EMPTY " + str(emptyFields * emptyWeight)
			# print emptyFields * emptyWeight
			# score += emptyfields
			#print "CLOSE " + str(closescore * closeWeight)
			
			print "ORDER " + str(order * orderWeight)
			print "NEAR " + str(near * nearWeight)
			print "CORNER " + str(corner)
			print "last score " + str(score)
		
		#
  		return score
	
	
	
	def getCloseNumberScore(self, grid):
		score = 0
		i = 0
		for x in grid.map:
			j = 0
			
			for y in x:
				# up
				if i > 0:
					if grid.map[i - 1][j] == y:
						score += y
					# if grid.map[i-1][j] == y/2 or grid.map[i-1][j] == y*2:
					# 	score += 0.05 * y
				
					
				# down
				if i < (len(grid.map) - 1):
					if grid.map[i + 1][j] == y:
						score += y
					# if grid.map[i+1][j] == y/2 or grid.map[i+1][j] == y*2:
					# 	score += 0.05 * y
				
									
				# left
				if j > 0:
					if grid.map[i][j - 1] == y:
						score += y
					# if grid.map[i][j-1] == y/2 or grid.map[i][j-1] == y*2:
					# 	score += 0.05 * y
					
					
				# right
				if j < (len(x) - 1):
					if grid.map[i][j + 1] == y:
						score += y
					# if grid.map[i][j+1] == y/2 or grid.map[i][j+1] == y*2:
					# 	score += 0.05 * y
					
					
				j += 1
				
			i += 1
		return score
	
	def getNearByScore(self, grid):
		score = 0
		for x in range (0, 4):
			for y in range (0, 4):
				if grid.map[x][y] != 0:
					for v in directionVectors:
						a = v[0]
						b = v[1]
						
						cX = x
						cY = y
						while grid.gridInsertOk((cX + a, cY + b)):
							
							if grid.map[cX][cY] == grid.map[cX + a][cY + b] and grid.map[cX][cY] != 0:
								score += math.log(grid.map[cX][cY]) / math.log(2)	
							elif  grid.map[cX][cY] > 0 and grid.map[cX + a][cY + b] > 0  and (grid.map[cX][cY] == grid.map[cX + a][cY + b] / 2 or grid.map[cX][cY] / 2 == grid.map[cX + a][cY + b]):
								if grid.map[cX][cY] > grid.map[cX + a][cY + b]:
									score += math.log(grid.map[cX + a][cY + b] / 2) / math.log(2) / 2
								else:
									score += math.log(grid.map[cX][cY] / 2) / math.log(2) / 2
									
								
# 							elif grid.map[cX][cY] != 0 and grid.map[cX + a][cY + b] != 0:
# 								score -= math.log(grid.map[cX][cY])/ math.log(2) - math.log(grid.map[cX + a][cY + b]) / math.log(2)
							cX = cX + a
							cY = cY + b	
		return score
				
				
				
		
				
	def getOrder(self, grid):
		scores = [0, 0, 0, 0]
		
		# right/left
		for x in range(0, 4):
			current = 0
			next = current + 1
			
			# find the next value 
			while next < 4 and grid.map[x][next] == 0:
				next += 1
			
			while next < 4:
				# get the current and the next value
				# if next >= 4:
				# 	next -= 1
				currentVal = math.log(grid.map[x][current]) / math.log(2) if grid.map[x][current] > 0 else 0
				nextVal = math.log(grid.map[x][next]) / math.log(2) if grid.map[x][next] > 0 else 0
				
				
				if currentVal >= nextVal:
					scores[0] += (nextVal - currentVal)
				elif nextVal > currentVal:
					scores[1] += (currentVal - nextVal)
					
					
				current = next
				next += 1
			
		# up/down
		for y in range(0, 4):
			current = 0
			next = current + 1
			
			# find the next value 
			while next < 4 and grid.map[next][y] == 0:
				next += 1
			
			while next < 4:
				# get the current and the next value
				# if next >= 4:
				# 	next -= 1
					
				currentVal = math.log(grid.map[current][y]) / math.log(2) if grid.map[current][y] > 0 else 0
				nextVal = math.log(grid.map[next][y]) / math.log(2) if grid.map[next][y] > 0 else 0
				
				
			#
				if currentVal >= nextVal:
					scores[2] += (nextVal - currentVal)
					
				elif nextVal > currentVal:
					scores[3] += (currentVal - nextVal)
					
				current = next
				next += 1
			
		# print scores
		
		lr = 0
		if scores[0] == 0:
			lr = scores[1]
		elif scores[1] == 0:
			lr = scores[0]
		elif scores[0] >= scores[1]:
			lr = scores[0]
		elif scores[1] > scores[0]:
			lr = scores[1]
			
		ud = 0
		if scores[2] == 0:
			ud = scores[3]
		elif scores[3] == 0:
			ud = scores[2]
		elif scores[2] >= scores[3]:
			ud = scores[2]
		elif scores[3] > scores[2]:
			ud = scores[3]
		
		
		return lr + ud
					
				
		
		
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
	
		return 	(math.log(score)) if score > 0 else 0

		
		
	
