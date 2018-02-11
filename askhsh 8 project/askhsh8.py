#p17095/from 30 random naumbers betwwen -30,30 find all the groups of three with sum of 0
import random
import itertools

my_randoms=[]

for i in range (30):
    my_randoms.append(random.randrange(-30,30,1))
print (my_randoms)
my_trios= list(itertools.combinations(my_randoms ,3))
#print("oi triades einai:"my_trios)#test line ,be careful if you change range
print("to plhthos tvn triadvn einai:")
print(len(my_trios))#test line
trios_zero=[]
for i in range(len(my_trios)):
    sum=0
    for j in range(3):
        sum += my_trios[i][j]
    #print(sum)
    if sum==0:
        trios_zero.append(my_trios[i])
if trios_zero==[]:
    print("none of the possible triplets equals to zero")
else:
    print(trios_zero)
    print ("oi triades poy xoyn athroisma mhden einai :" )
    print(len(trios_zero))
