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
	for i in range(0,len(state),3):
		for j in range(3):
			print(state[i+j], end=" ")
		print()
		

def sequence(state,count,count_list):
	count += 1
	count_list.append(count)
	if state.parent is None:
		print('\nThe initial state is: \n')
		printBoard(state.data)
		return
	sequence(state.parent,count, count_list)
	print("\nNext move:\n")
	printBoard(state.data)
	return count_list

def misplacedTiles(state, goal):
	tiles = 0
	for i in range(len(state)):
		if state[i] == 0:
			continue

		
		elif state[i] != goal[i]:
			tiles += 1
	return tiles

def bubbleSort(list):
	length = len(list)

	for i in range(length - 1):
		for j in range(0, length - i - 1):
			if list[j].weight > list[j+1].weight:
				list[j], list[j+1] = list[j+1], list[j]

def manhattan(state, goal):
	total = 0
	for i in range(9):
		if state[i] != 0:total += abs((i % 3) - (findIndex(state[i],goal) % 3)) + abs((i // 3) - (findIndex(state[i],goal) // 3))
	return total
	 
def findIndex(target, goal):
	for i in range(9):
		if target == goal[i]:
			return i
			

#----Breadth-First Search----#

def bfs(state,goal):
	# count = 0 #remove after testing
	fringe = deque()
	fringe.append(state)
	closed = []
	while fringe:
		# print(f"loop {count}")
		newState = fringe.popleft() #queue
		closed.append(newState.data) # add the newstate to explored/ close
		if newState.data == goal:
			# return the path from start to goal
			# while there is a parent print the parent
			count_list = []
			sequence(newState,0,count_list)
			print("\nThe goal state was found!\n")
			print(f"The number of nodes expanded were: {len(closed)}")
			print(f"The total number of nodes in the search space were: {len(fringe) + len(closed)}")
			print(f"The length of the solution path was: {len(count_list)-1}\n") #This is also just the number of times the board was printed right?
			print("-----------------------------------------------------------")
			return True #True for testing

		for neighbor in newState.checkMoves(): # check every move we can make
			if neighbor.data not in closed: #if we didn't explore/ close the node
				fringe.append(neighbor) # add the neighbor/ child to fringe
				closed.append(neighbor.data) # add the current state to closed

#----Greedy Best-First Search using the Misplaced Tiles heuristic----#

def gbfs(state,goal):
	fringe = deque()
	fringe.append(state)
	closed = []
	while fringe:
		newState = fringe.popleft() #queue
		closed.append(newState.data) # add the newstate to explored/ close

		if newState.data == goal:
			# return the path from start to goal
			# while there is a parent print the parent
			count_list = []
			sequence(newState,0,count_list)
			print("\nThe goal state was found!")
			print(f"The number of nodes expanded were: {len(closed)}")
			print(f"The total number of nodes in the search space were: {len(fringe) + len(closed)}")
			print(f'The length of the solution path was: {len(count_list)-1}') #This is also just the number of times the board was printed right?
			print("-----------------------------------------------------------")
			return True #True for testing

		for neighbor in newState.checkMoves(): # check every move we can make
			if neighbor.data not in closed: #if we didn't explore/ close the node
				neighbor.weight = misplacedTiles(neighbor.data, goal)
				fringe.append(neighbor) # add the neighbor/ child to fringe
				closed.append(neighbor.data) # add the current state to closed
		bubbleSort(fringe)

# #----A* Search using the Misplaced Tiles heuristic----#

def aStarMisplacedTiles(state,goal):
	
	fringe = deque()
	fringe.append(state)
	closed = []
	while fringe:
		newState = fringe.popleft() #queue
		closed.append(newState.data) # add the newstate to explored/ close
		if newState.data == goal:
			# return the path from start to goal
			# while there is a parent print the parent
			count_list = []
			sequence(newState,0,count_list)
			print("\nThe goal state was found!")
			print(f"The number of nodes expanded were: {len(closed)}")
			print(f"The total number of nodes in the search space were: {len(fringe) + len(closed)}")
			print(f'The length of the solution path was: {len(count_list)-1}') #This is also just the number of times the board was printed right?
			print("-----------------------------------------------------------")
			return True #True for testing

		for neighbor in newState.checkMoves(): # check every move we can make
			if neighbor.data not in closed: #if we didn't explore/ close the node
				neighbor.weight = misplacedTiles(neighbor.data, goal) + newState.weight # cost of misplaced tiles and current state
				fringe.append(neighbor) # add the neighbor/ child to fringe
				closed.append(neighbor.data) # add the current state to closed
		bubbleSort(fringe)

#----A* Search using the Manhattan Distance heuristic----#

def aStarManhattanDistance(state,goal):
	fringe = deque()
	fringe.append(state)
	closed = []
	while fringe:
		newState = fringe.popleft() #queue
		closed.append(newState.data) # add the newstate to explored/ close
		if newState.data == goal:
			# return the path from start to goal
			# while there is a parent print the parent
			count_list = []
			sequence(newState,0,count_list)
			print("\nThe goal state was found!")
			print(f"The number of nodes expanded were: {len(closed)}")
			print(f"The total number of nodes in the search space were: {len(fringe) + len(closed)}")
			print(f'The length of the solution path was: {len(count_list)-1}') #This is also just the number of times the board was printed right?
			print("-----------------------------------------------------------")
			return True #True for testing

		for neighbor in newState.checkMoves(): # check every move we can make
			if neighbor.data not in closed: #if we didn't explore/ close the node
				neighbor.weight = manhattan(neighbor.data, goal) + newState.weight # cost of misplaced tiles and current state
				fringe.append(neighbor) # add the neighbor/ child to fringe
				closed.append(neighbor.data) # add the current state to closed
		bubbleSort(fringe)

#MAIN

def main():

	#Board initialization
	print("The 8 puzzle solver recieves an input of integers 0-8, the zero representing the blank space.")
	
	# start_state = input("Please input a start state of the 8 puzzle: ")
	# goal_state = input("Now please enter a goal state for the puzzle: ")

	start_state = [1,4,2,
				   3,0,5,
				   6,7,8]
	goal_state =  [0,1,2,
				   3,4,5,
				   6,7,8]

	# start_state = [2,8,3,
	# 			     1,6,4,
	# 			     7,0,5]

	# goal_state =  [0,1,2,
	# 							 3,4,5,
	# 							 6,7,8]

	current_state = Node(start_state)

	if evenParity(start_state):
		print('Great choice, this puzzle is solvable.\n')
		current_state = Node(start_state)

		#Run each search algorithm to compare.
		print("Running Breadth First Search:\n")
		bfs(current_state,goal_state)
		print("\nRunning Greedy Best First Search:\n")
		gbfs(current_state,goal_state)
		print("\nRunning A* with Misplaced Tiles Heuristic:\n")
		aStarMisplacedTiles(current_state,goal_state)
		print("\nRunning A* with Manhattan Distance Heuristic:\n")
		aStarManhattanDistance(current_state,goal_state)

	else: print('I am sorry, but this is not solvable. Please choose a different set.')

		
if __name__ == "__main__":
	main()
