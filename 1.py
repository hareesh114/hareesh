import random
import sys 

#pip install pillow

from PIL import Image                                                                                
im = Image.open('1.jpeg')
img=im.resize((256,512))
img.show() 

#printing 100 numbers

b=list(range(11,21))[::-1]
c=list(range(21,31))
d=list(range(31,41))[::-1]
e=list(range(41,51))
f=list(range(51,61))[::-1]
g=list(range(61,71))
h=list(range(71,81))[::-1]
i=list(range(81,91))
j=list(range(91,101))[::-1]

print("\n 	     SNAKE && LADDER GAME")
print("            ----------------------")
print("        Snakes and ladders is still fun!")
print("		               -INDIA MART\n")
print("\n* * * * * * * * * * * * * * * * * * * * * * *")
print('*',j,'*','\n','*',i,'*','\n','*',h,'*','\n','*',g,'*','\n','*',f,'*','\n','*',e,'*','\n','*',d,'*','\n','*',c,'*','\n','*',b,'*')

print(' ',end="")
print('*',end="")
print(' ',end="")
print("[",end="")
for i in range(1,10):
	print('0',end="")
	print(i,end="")
	print(',',end="")
	print(' ',end="") 
print("10",end="")
print("]",end="")
print(' ',end="")
print('*')
print("* * * * * * * * * * * * * * * * * * * * * * *")


def play():
	player1=0
	player2=0

	#positions of snackes and ladders
	def check_for_snakes_and_ladders(n):

		"""This method checks for the presence of snakes or ladders in the board"""
	
		ladders={1:38,4:14,9:31,21:42,28:84,36:44,51:67,71:91,80:97}
		snakes={98:78,95:75,93:73,87:24,64:60,62:19,56:53,49:11,48:26,16:6}
		if(n in ladders):
			print("\n-----------Hurray..!!Its a ladder,Climb up-----------")
			n=ladders[n]
		elif(n in snakes):
			print("\n-----------OOPS..!!Its a snake,you are swallowed!!,Come down-----------")
			n=snakes[n]
		return n


	#rolling dice
		"""This method takes input from each of the players, prints the current position of the players and checks for the
		winner of the game"""


	def roll_dice(r):	
		print("click y to roll die // click n to exit game")
		c=input() 
		d=random.randint(1,6)
		if(c=="y" or c=="Y"):
			k=d
			d=int(d)+int(r) 
			print("number on die is :",end="")
			print(k)
		elif(c=="n"  or c=="N"):
			sys.exit()
		return d


	while(player1 < 100 or player2 < 100):
		print("\n	Its turn of player1\n")
		prev1=player1
		player1=roll_dice(player1)
		player1=check_for_snakes_and_ladders(player1)
		print("\n************************************************")
		k1=player1 
		if(k1<=100):
			print("Current status of Player1:",player1,"and Player2:",player2)
		
			print("\n************************************************")
			if(k1 is 100):
				print("\n************************************************")
				print(" 	Congrats player1, you are the Winner of the game")
				break
		elif(k1>100):
			player1=prev1
			print(" 	HardLuck..!!Wait For Next Chance") 
			print("Current status of Player1:",player1,"and Player2:",player2)
			print("************************************************\n")
	
		print("\n	Its turn of player2\n")
		prev2=player2
		player2=roll_dice(player2)
		player2=check_for_snakes_and_ladders(player2)
		print("\n************************************************")	
		k2=player2
		if(k2<=100):	
			print("Current status of Player1:",player1," and Player2:",player2)
		
			print("\n************************************************")
			if(k2 is 100):
				print("\n************************************************")
				print(" 	Congrats player2, you are the Winner of the game")
				break
		elif(k2>100):
			player2=prev2
			print(" 	HardLuck..!!Wait For Next Chance")
			print("Current status of Player1:",player1,"and Player2:",player2)				
			print("************************************************\n") 

play()


f=0
while(f is 0):
	print("Click x to new game || click z to quit")
	i=input()
	if(i=="x" or i=="X"):
		play()
	elif(i=="Z" or i=="z"):
		sys.exit() 

