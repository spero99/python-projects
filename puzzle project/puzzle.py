#p17095/100*100 puzzle that is gonna get solved  by th use of the pc
import random

letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
print (letters)                                                                                                                 #test line
random.shuffle(letters)
print(letters)                                                                                                                  #test line

for i in range(10):
    for j in range(10):
        print(letters.pop())
