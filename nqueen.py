import time

n = int(raw_input('>')) 
queens = 0
x = 0 
y = 0
lx = 1 
ly = 0
even = True
e = 0
rx = n-1
ry = n-1

board = [[0 for x in range(n)] for x in range(n)]
evens = []
odds = []
for i in range(0,n):
	if i%2 == 0:
		evens+=[i]
	else:
		odds+=[i]
print (evens, odds)
searching = False
okay = True
nope = False

def search_horizontal(y, board):
	for xx in range(n):
		if board[y][xx] == 5:
			return nope
	return okay
	
def search_vertical(x, board):	
	for yy in range(n):
		if board[yy][x] == 5:
			return nope
	return okay

def search_diagonals(y,x,board,e):
	#print (y,x)
	for i in range(x+1):
		try:
			if board[y+i][x-i] == 5:
				return nope
		except IndexError:
#			print "backward"
#			print (y,x)
#			print (y+i,x-i)
#			continue
			e='oops'
		try:
			if board[y-i][x-i] == 5:
				return nope
		except IndexError:
#			print "backward"
#			print (y,x)
#			print (y-i,x-i)
			e='oops'

	for i in range(n-x):
		try:
			if board[y+i][x+i] == 5:
				return nope
		except IndexError:
#			print "forward"
#			print (y,x)
#			print (y+i,x+i)
#			continue
			e='oops'
		try:
			if board[y-i][x+i] == 5:
				return nope
		except IndexError:
#			print "forward"
#			print (y,x)
#			print (y-i,x+i)
#			continue
			e='oops'
	return okay

def search(y,x,board,e):
	if search_horizontal(y,board) and search_vertical(x,board) and search_diagonals(y,x,board,e):
		return okay
	else:
		return nope
		
while queens < n:

	if queens == 0 and ly < n and lx < n:
		board[ly][lx] = 5
		queens+=1
		if board [0][0] == 0:
			board[ry][rx] = 5
			queens+=1	

	for yy in evens:
		for xx in range(n):
			if search(yy,xx,board,e):
				board[yy][xx] = 5
				queens+=1		
		
	for yy in odds:
		for xx in range(n):
			if board[yy][xx] == 5:
				break
			if search(yy,xx,board,e):
				board[yy][xx] = 5
				queens+=1		
	
	if queens < n:
		if lx < n-1:
			rx-=1
			lx+=1
		else:
			ry-=1
			rx=n-1
			ly+=1
			lx=0
		queens=0
		board = [[0 for x in range(n)] for x in range(n)]
		    
for row in board:
	print row
