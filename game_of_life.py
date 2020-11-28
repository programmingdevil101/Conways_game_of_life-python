from copy import deepcopy
import time
import random
import pygame
pygame.init()


HEIGHT = 400
WIDTH = 400
Black = (0, 0, 0)
White = (255, 255, 255)
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
			
			# FOR LIVE CELL
			if current_state[i][j] == 1:
				if no_of_alive_neighbors not in (2, 3):
					next_state[i][j] = 0

			# FOR DEAD CELL
			if current_state[i][j] == 0:
				if no_of_alive_neighbors == 3:
					next_state[i][j] = 1

	return (next_state)

# ---- TODO: MAKE A NEW RENDER FUNCTION THAT DOESNOT USE TERMINAL
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


def render_with_pygame(state):
	screen = pygame.display.set_mode((HEIGHT, WIDTH))
	pygame.display.set_caption("Conway's game of life")
	screen.fill(White)
	run = True
	new_state = state
	while run:
		drawGrid(new_state, screen)
		new_state = next_state(new_state)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				
		pygame.display.update()



def drawGrid(state, screen):
	no_of_row = len(state)
	no_of_col = len(state[0])
	cell_width = WIDTH//no_of_col
	cell_Height = HEIGHT//no_of_row

	for x in range(no_of_row):
		for y in range(no_of_col):
			rect = pygame.Rect(x*cell_width, y*cell_width, cell_width, cell_Height)
			if state[x][y] == 1:
				#pygame.draw.line(screen, Black, (x, y), (2*x, 2*y))
				#print(rect)
				pygame.draw.rect(screen, Black, rect, 1)
			else:
				pygame.draw.rect(screen, White, rect, 1)



def loop(init_state):
	state = init_state
	while True:
		render(state)
		state = next_state(state)
		time.sleep(0.03)

# keep rows and column atmost 400 as avove that will make cell height and width 0 due to floor division
init_state = random_state(200, 200)
render_with_pygame(init_state)
pygame.quit()
#loop(init_state)
