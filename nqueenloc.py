import random
import sys

n = int(raw_input(">"))
def generateStartState(n):
	board = []
	for i in range(1,n+1):
		board.append((i,random.randrange(1,n+1)))
	return board

def threatens(q1, q2):
	q1x = q1[0]
	q1y = q1[1]
	q2x = q2[0]
	q2y = q2[1]

	if (q1x + q1y == q2x + q2y or q1x - q1y == q2x - q2y or q1y == q2y):
		return True
	else:
		return False

def h(board):
	n = 0
	for i in range(0,len(board)):
		for j in range(i+1,len(board)):
			if threatens(board[i],board[j]):
				n += 1
	return n

def step(board):
	for i in [-1,1]:
		for queen in board:
			q1x = queen[0]
			q1y = queen[1]
			if q1y + i > len(board) or q1y + i < 1:
				continue
			else:
				newBoard = board[:]
				newBoard.remove(queen)
				newBoard.append((q1x, q1y + i))
				if h(newBoard) == 0:
					return newBoard
				elif h(newBoard) < h(board):
					return step(newBoard)
	return step(generateStartState(len(board)))

print step(generateStartState(n))
