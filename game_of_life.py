from copy import deepcopy
import time
import random


DEAD = 0
ALIVE = 1


def dead_state(height, width):
	return [[DEAD for _ in range(width)] for _ in range(height)]


def random_state(height, width):
	state = dead_state(height, width)

	for i in range(height):
		for j in range(width):
			num = random.random()
			alive_to_dead = 0.65
			cell = 0
			if num<=alive_to_dead:
				cell = ALIVE
			else:
				cell = DEAD
			state[i][j] = cell
	return state


def next_state(current_state):
	next_state = deepcopy(current_state)
	leftB = topB = 0
	rightB = len(current_state[0])-1
	bottomB = len(current_state)-1
	
	for i in range(len(current_state)):
		for j in range(len(current_state[0])):
			neighbors = []
			top_i = i-1
			bottom_i = i+1 
			Left_j = j-1
			Right_j = j+1
						
			if top_i>=topB:
				if Left_j>=leftB:
					neighbors.append(current_state[top_i][Left_j])
				if Right_j<=rightB:
					neighbors.append(current_state[top_i][Right_j])
				neighbors.append(current_state[top_i][j])

			if Left_j>=leftB:
				if bottom_i<=bottomB:
					neighbors.append(current_state[bottom_i][Left_j])
				neighbors.append(current_state[i][Left_j])

			if Right_j<=rightB:
				if bottom_i<=bottomB:
					neighbors.append(current_state[bottom_i][Right_j])
				neighbors.append(current_state[i][Right_j])

			if bottom_i<=bottomB:
				neighbors.append(current_state[bottom_i][j])

			no_of_alive_neighbors = neighbors.count(1)
			print(f"{no_of_alive_neighbors} - {neighbors}")

			# FOR LIVE CELL
			if current_state[i][j] == 1:
				if no_of_alive_neighbors not in (2, 3):
					next_state[i][j] = 0

			# FOR DEAD CELL
			if current_state[i][j] == 0:
				if no_of_alive_neighbors == 3:
					next_state[i][j] = 1

	return (next_state)


def render(state):
	display = {
		DEAD: ' ',
		ALIVE: u"\u2588"
	}

	lines = []
	for x in range(len(state)):
		line = ''
		for y in range(len(state[0])):
			line+=display[state[x][y]]*2
		lines.append(line)
	ren = "\n".join(lines)
	print(ren)

def loop(init_state):
	state = init_state
	while True:
		render(state)
		state = next_state(state)
		time.sleep(0.03)

if __name__ == "__main__":
	init_state = random_state(100, 50)
	loop(init_state)
