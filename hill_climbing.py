from random import randint
from copy import deepcopy

class NQueen:

	def __init__(self, row, col):

		self.row = row
		self.col = col

	def conflict(self, other):

		return (self.row == other.row or
		 		self.col == other.col or
		 		(abs(self.row - other.row) == abs(self.col - other.col)))

class HillClimbing:

	random_restarts = 0
	steps_after_last_restart = 0
	heuristic = 0
	steps_climbed = 0

	def generate_board(self):

		self.board = [] 
		for i in range(self.N):
			self.board.append(NQueen(randint(0, self.N - 1), i))
 
		return self.board 

	def find_heuristic(self, board):

		heuristic = 0
		for i in range(self.N):
			for j in range(i + 1, self.N):
				if board[i].conflict(board[j]):
					heuristic += 1

		return heuristic

	def next_board(self): 
		next_board = deepcopy(self.board) 
		temp_board = deepcopy(self.board) 
		t_heuristic = 0 
		best_heuristic = self.heuristic 


		for i in range(self.N): 
			temp_board[i] = NQueen(0, i) 

			if i > 0: 
				temp_board[i - 1] = NQueen(self.board[i - 1].row, self.board[i - 1].col) 

			for j in range(self.N + 1): 	
				t_heuristic = self.find_heuristic(temp_board)


				if t_heuristic < best_heuristic: 
					best_heuristic = t_heuristic
					next_board = deepcopy(temp_board) 

				if j <= self.N: 
					temp_board[i] = NQueen(j, i) 


		if best_heuristic == self.heuristic: 
			self.random_restarts += 1
			next_board = self.generate_board() 
			self.steps_after_last_restart = 0 

		else: 
			self.heuristic = best_heuristic 

		self.steps_climbed += 1 
		self.steps_after_last_restart += 1 

		print('Next board : ') 
		self.display(next_board)
		print('heuristic : ', self.find_heuristic(next_board), '\n')
		return next_board 

	def display(self, board):
		mat = [['_'] * self.N for i in range(self.N)]

		for queen in board: 
			mat[queen.row][queen.col] = 'Q'

		for row in mat:
			for el in row: 
				print(el, end = '\t')
			print() 

		print()

	def main(self): 

		self.N = int(input('enter number of queens : '))

		while self.N in range(1, 4): 
			print('No possible solution for %d queens, please enter another number'%(self.N))
			self.N = int(input('enter number of queens : '))

		self.generate_board()
	
		self.display(self.board) 

		print('initial heuristic : ', self.find_heuristic(self.board)) 
		i = 0 

		self.heuristic = self.find_heuristic(self.board) 
		while(self.heuristic != 0):
			self.board = self.next_board() 
			self.heuristic = self.find_heuristic(self.board) 		
		
		print('Total number of steps climbed : %d' % (self.steps_climbed)) 
		print('Number of random restarts : %d' % (self.random_restarts))	
		print('Steps climbed after last restart : %d' % (self.steps_after_last_restart))

hill_climbing = HillClimbing() 
hill_climbing.main()


