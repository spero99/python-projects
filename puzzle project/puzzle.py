#p17095/100*100 puzzle that is gonna get solved  by th use of the pc
import random

letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

seq=[]
puzzle_row=[]
puzzle_col=[]
def sequence():
    for i in range(100):
    return seq
def makepuzzle():
    letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    letters=letters*50
    random.shuffle(letters)

    for i in range(100):
        puzzle_row.append(letters.pop())
    puzzle_row.append('\n')
    return puzzle_row

for i in range(100):
    makepuzzle()

print(" ".join(puzzle_row))


#print (" ".join(puzzle_col))
