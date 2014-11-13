AI_Fall2014-2048
================

mh3478 - Maria Hollweck - Artificial Intelligence - HW2



(1) Alpha Beta - Pruning for the Player - Random Inserts for the Computer
I was interested in finding out how far I can come with a depth = 0 and also with the depth > 0. Here my results.

(a) high depth
I used to test with depth 3, that means I will go one step forward. Most time, my AI is reaching > 1024, sometimes 2048.

My Heuristics contains the following methods:
- how close are our numbers? weighted with 0.1
- how many empty fields do I have in the grid? weighted with 2.7
- what is the highest value in the grid? weighted with 1
- do we have a good order? weighted with 1

(b) depth = 0
I used to test this with depth 1, that means I will just calulate the next step from the CURRENT grid (without any smart steps forward). 
I usually reach 1024 and sometimes 2048. The big benefit of this Algorithm: it's very very fast. 

My Heuristics for this contained the following methods:
- how close are our numbers? weighted with 0.8 
- how many empty fields do I have in the grid? weighted with 0.3
- what is the highest score that the grid can achieve? weighted 1
- is the highest tile in a corner? weighted 1
- do we have a good order? weighted with 1


(2) Random Inserts for Player - Alpha Beta Implementation for the Computer
I used my alpha-beta-pruning algorithm and started with the cells (min) instead of with the tiles (max). My depth is 2.
I just tested my ComputerAI in combination with my best PlayerAI and got to 256 and 128.

(3) My customized files are:
	- Grid.py: I customized the Grid.py and added extra methods (marked with "MH3478 EDIT" and "MH3478 END")
	- Heuristic.py 
	- AlphaBetaPruning.py
	- PlayerAI.py
	- ComputerAI.py
