from copy import deepcopy 
import sys 
INFINITY = sys.maxsize

initial = [	[1, 2, 3], 
			[5, 6, None], 
			[7, 8, 4]] 

final   = [
			[5, 1, 3], 
			[7, 2, 6], 
			[None, 8, 4]] 

rows 	= len(initial) 
cols 	= len(initial[0])
quit 	= False 

def display(mat): 
	for row in mat: 
		for el in row: 
			print(el, end = '\t') 
		print() 

def h_score(initial, row, col, nrow, ncol):
	temp 	= deepcopy(initial) 
	score   = 0 

	temp[row][col], temp[nrow][ncol] = temp[nrow][ncol], temp[row][col]


	for i in range(len(temp)): 
		for j in range(len(temp[0])): 
			if temp[i][j]: 
				if not final[i][j] or temp[i][j] != final[i][j]: 
					score += 1 

	return score

def eight_puzzle(initial, row, col, g_score): 
	global quit 
	moves = {'D' : INFINITY, 'L' : INFINITY, 'R' : INFINITY, 'U' : INFINITY} 

	if row - 1 > - 1: 
		moves['U'] = g_score + h_score(initial, row, col, row - 1, col)

	if row + 1 < rows: 
		moves['D'] = g_score + h_score(initial, row, col, row + 1, col)

	if col - 1 > - 1: 
		moves['L'] = g_score + h_score(initial, row, col, row, col - 1)

	if col + 1 < cols: 
		moves['R'] = g_score + h_score(initial, row, col, row, col + 1)


	mn =  min(moves.values()) 

	if mn - g_score == 0: 
		quit = True 

	if moves['U'] == mn: 
		return (row - 1, col) 

	if moves['D'] == mn:
		return (row + 1, col) 


	if moves['R'] == mn:
		return (row, col + 1) 

	if moves['L'] == mn:
		return (row, col - 1) 


def main(initial, g_score):
	global quit 
	while not quit: 
		for row in range(len(initial)): 
			for col in range(len(initial[0])): 
				if not initial[row][col]: 
					narray = deepcopy(initial) 
					nrow, ncol = eight_puzzle(initial, row, col, g_score) 
					narray[row][col], narray[nrow][ncol] = narray[nrow][ncol], narray[row][col]
					display(narray)
					print()
					main(narray, g_score + 1)

print('INITIAL\n')
display(initial) 

print('\nFINAL\n')
display(final) 

print('\nSTEPS\n')
main(initial, 0)
