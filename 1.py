import random
import sys
import os
import datetime

now = datetime.datetime.now()


from PIL import Image                                                                                
im = Image.open('1.jpeg')
img=im.resize((512,512))
img.show()

print("\n            -----------------------")
print(now.strftime("             %d-%m-%Y | %H:%M:%S"))
print("            -----------------------")

print("\n 	     SNAKE && LADDER GAME")
print("            ----------------------")
print("        Snakes and ladders is still fun!")
print("		               -INDIA MART\n")

print("IMPORTANT INSTRUCTIONS:")
print("\n***Playing the Snakes and Ladders Board Game***\n")
print("->Understand the object of the game")
print("->Decide who goes first")
print("->Roll the dice and move")
print("->Climb up ladders")
print("->Slide down snakes")
print("->Take an extra turn if you roll a six")
print("->Land exactly on the last square to win") 
print("\nNOTE:-Number of players must be > 1")


sAlPoS={1: 38,4: 14,9:  31,17: 7,21: 42,28: 84,51: 67,54: 34,62: 19,64: 60,72: 91,80: 99,87: 36,93: 73,95: 75,98: 79,}


class Player:
	def __init__(self, inPlayerNum):
		self.playerPos = 0
		self.playerNum = inPlayerNum

	def updatePosition(self, inPos):
		self.playerPos = inPos

	def getPosition(self):
		return self.playerPos

	def getPlayerNum(self):
		return self.playerNum


def gameMaster(inPlayer):
	global winner
	if winner == False:
		print("\n-----------Player %i-----------" % inPlayer.getPlayerNum())
		roll = rollDice()
		print("You rolled: %i" % roll)
		movePlayer(inPlayer, roll)
		checkPosition(inPlayer)
		if roll is 6:
			print("CONGO..ONE MORE CHANCE MATE..!!")
			gameMaster(playerList[i])  


def rollDice():   
    print("click y to roll die || click n to exit game") 
    c=input() 
    if(c=='y' or c=='Y'):
        d=random.randint(1,6)
    elif(c=='n'  or c=='N'):
        sys.exit()
    else:
    	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % ( 1,1000))
    	print("Sorry!  That was no valid option.  Try again...\n")
    	f=rollDice()
    	return f
    return d


count=1
def movePlayer(inPlayer, roll):
	global playerList
	if inPlayer.getPosition() + roll <= 100:
		inPlayer.updatePosition(inPlayer.getPosition() + roll)
		print("You are at spot %i" % inPlayer.getPosition())
		if inPlayer.getPosition() == 100:
			global count
			print("\nCongratulations...Player %i is the Winner-"% inPlayer.getPlayerNum(),end="")
			print(" %i "% count)
			count=count+1
			playerList.remove(inPlayer)
			global looser
			looser=True
			if(len(playerList)==1 or len(playerList)==0):
				global winner
				winner = True
	else:
		print("HardLuck..!!Wait For Next Chance")
		print("You are at spot %i" % inPlayer.getPosition()) 


def checkPosition(inPlayer):
	for pos in sAlPoS:
		if pos == inPlayer.getPosition():
			if pos < sAlPoS[pos]:
				print("Hurray..!!Its a ladder,you Climb up to spot %i" % sAlPoS[pos])
			else:
				print("OOPS..!!Its a snake,you are swallowed!!,Come down to spot %i" % sAlPoS[pos])
			inPlayer.updatePosition(sAlPoS[pos])


if __name__ == '__main__':
	global winner
	global looser
	winner = False		
	looser = False
	while True:
        	try:
        	    numPlayers = int(input('\nEnter number of players: '))
        	    if numPlayers is 1:
        	    	raise ValueError
        	    else:
        	    	break
        	except ValueError:
        	    os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % ( 1,1000))
        	    print("Oops!  That was no valid number.  Try again...")
	num=numPlayers
	print("\nThe Players Are:")
	j=1
	while(num!=0):
		print("player %i" % j )
		j=j+1
		num=num-1
		
	global playerList		
	playerList = []
	
	for j in range(1,numPlayers+1): 
		playerList.append(Player(j))
	
	while winner == False:
		i=0
		while(i<len(playerList)):
			if winner == False:
				gameMaster(playerList[i])
			else:
				break		 				
			if looser == True:
				looser=False
				continue
			i+=1	
			
os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % ( 1,500))
	
def python():				
	print("\nClick 1 to new game || click 0 to quit")
	q=input() 
	if(q=='1'):
		os.system("clear & python3 py.py")
	elif(q=='0'):
		exit()
	else:
		os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % ( 1,1000))
		print("Choose Correct Option")
		python()		

python() 
