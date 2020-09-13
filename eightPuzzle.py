# CSCE 405, Dr. Moore
# Assignment 1, 8 Puzzle Solver
# Andrew Baluyut, Hannah Crayton

from Node import Node
from collections import deque
import sys

# Program function declarations

def evenParity(start_state):
	num_inversions = countInversions(start_state)
	return (num_inversions % 2 == 0)

def countInversions(start_state):
	start_count = 0

	for i in range(8):
	    for j in range(i+1, 9):
		    if start_state[j] and start_state[i] and start_state[i] > start_state[j]:
    			start_count += 1

	return start_count

def printBoard(state):
	print()
	for i in range(0,len(state),3):
		for j in range(3):
			print(state[i+j], end=" ")
		print()
		

def sequence(state):
	if state.parent is None:
		printBoard(state.data)
		return
	sequence(state.parent)
	printBoard(state.data)

#----Breadth-First Search----#

def bfs(state,goal):
	# count = 0 #remove after testing
	fringe = deque()
	fringe.append(state)
	closed = []
	#pseudocode
	while fringe:
		# print(f"loop {count}")
		newState = fringe.popleft() #queue
		closed.append(newState) # add the newstate to explored/ close
		if newState.data == goal:
			# print("fringe:")
			# for i in fringe:
			# 	print(i.data)
			# print("closed:")
			# for i in closed:
			# 	print(i.data)
			# return the path from start to goal
			print("\nThe goal state was found!")
			# while there is a parent print the parent
			sequence(newState)
			print(f"The number of nodes expanded were: {len(closed)}")
			print(f"The total number of nodes in the search space were: {len(fringe) + len(closed)}")
			print('The length of the solution path was: ') #This is also just the number of times the board was printed right?
			return True #True for testing

		for neighbor in newState.checkMoves(): # check every move we can make
			if neighbor not in closed: #if we didn't explore/ close the node
				fringe.append(neighbor) # add the neighbor/ child to fringe
				closed.append(neighbor) # add the current state to closed

#----Greedy Best-First Search using the Misplaced Tiles heuristic----#

def gbfs(state,goal):
	
	#common print sequence
	print("\nThe goal state was found!")
	# while there is a parent print the parent
	sequence(newState)
	print(f"The number of nodes expanded were: {len(closed)}")
	print(f"The total number of nodes in the search space were: {len(fringe) + len(closed)}")
	print('The length of the solution path was: ') #This is also just the number of times the board was printed right?	


#----A* Search using the Misplaced Tiles heuristic----#

def aStarMisplacedTiles(state,goal):
	
	#common print sequence
	print("\nThe goal state was found!")
	# while there is a parent print the parent
	sequence(newState)
	print(f"The number of nodes expanded were: {len(closed)}")
	print(f"The total number of nodes in the search space were: {len(fringe) + len(closed)}")
	print('The length of the solution path was: ') #This is also just the number of times the board was printed right?

#----A* Search using the Manhattan Distance heuristic----#

def aStarManhattanDistance(state,goal):
	
	#common print sequence
	print("\nThe goal state was found!")
	# while there is a parent print the parent
	sequence(newState)
	print(f"The number of nodes expanded were: {len(closed)}")
	print(f"The total number of nodes in the search space were: {len(fringe) + len(closed)}")
	print('The length of the solution path was: ') #This is also just the number of times the board was printed right?	


#MAIN

def main():

	#Board initialization
	print("The 8 puzzle solver recieves an input of integers 0-8, the zero representing the blank space.")
	
	# start_state = input("Please input a start state of the 8 puzzle: ")
	# goal_state = input("Now please enter a goal state for the puzzle: ")

	start_state = [1,2,3,
								 4,5,0,
								 7,8,6]
	goal_state =  [1,2,3,
								 4,5,6,
								 7,8,0]

	# start_state = [2,8,3,
	#  							 1,6,4,
	#  							 7,0,5]
	# goal_state =  [0,1,2,
	# 							 3,4,5,
	# 							 6,7,8]

	current_state = Node(start_state)

	if evenParity(start_state):
		print('Great choice, this puzzle is solvable.')
		print('Our initial state is: ', start_state)
		current_state = Node(start_state)

		#Run each search algorithm to compare. 
		bfs(current_state,goal_state)
		gbfs(current_state,goal_state)
		aStarMisplacedTiles(current_state,goal_state)
		aStarManhattanDistance(current_state,goal_state)

	else: print('I am sorry, but this is not solvable. Please choose a different set.')

		
if __name__ == "__main__":
	main()
