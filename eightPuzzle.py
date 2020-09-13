from Node import Node
from collections import deque
import sys

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

# state is a Node
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
			print("\ngoal found")
			# while there is a parent print the parent
			sequence(newState)
			print(f"Number of Nodes expanded {len(closed)}")
			print(f"Number of Nodes in the search space {len(fringe) + len(closed)}")
			return True #True for testing

		for neighbor in newState.checkMoves(): # check every move we can make
			if neighbor not in closed: #if we didn't explore/ close the node
				fringe.append(neighbor) # add the neighbor/ child to fringe
				closed.append(neighbor) # add the current state to closed
				

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
		print('Solvable')
		current_state = Node(start_state)
		bfs(current_state,goal_state)
	else: print('Not solvable')

		
if __name__ == "__main__":
	main()
