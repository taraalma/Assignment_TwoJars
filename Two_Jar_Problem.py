import time

#Define variables
JarA = 0	#User can input the values
JarB = 0	#User can input the values

#define enumerators
from enum import Enum
class Jars(Enum):
	A = 0
	B = 1

#Define functions
def PrintInstructionsWithTime():
	print ("Welcome to the Two Jar problem, where you get problems, with jars, at no cost.")
	time.sleep(0.7)
	print ("There are two Jars. None of the Jars has marks that show the level in any measurement.")
	time.sleep(0.7)
	print ("The purpose is to reach certain amount of water in a Jar given two Jars of different measures.")
	time.sleep(0.7)
	print ("For example: given a Jar of 3 L and 5 L, get 4 L.")
	time.sleep(0.7)
	print ("You can only fill the Jars with new water until they are full. You cannot partially fill any Jar with an arbitrary amount of new water.")
	time.sleep(0.7)
	print ("You can pass water between Jars. However, you cannot know exactly how many liters have been passed to the other Jar by simply puring small amounts of water.")
	time.sleep(0.7)
	print ("However, you deduce the amount of water that a Jar has if you transfer water between them.")
	time.sleep(0.7)
	print ("Let water transfer begin.")
	time.sleep(0.7)
	print ("You will have to specify both the Jar A and Jar B capacity in liters.")
	time.sleep(0.7)	
	print ("You will also have to specify how many liters the algorithm has to reach")
	time.sleep(0.7)	
	print ("Start!")
	time.sleep(0.7)

def PrintInstructionsNoTime():
	print ("Welcome to the Two Jar problem, where you get problems, with jars, at no cost.")
	print ("There are two Jars. None of the Jars has marks that show the level in any measurement.")
	print ("The purpose is to reach certain amount of water in a Jar given two Jars of different measures.")
	print ("For example: given a Jar of 3 L and 5 L, get 4 L.")
	print ("You can only fill the Jars with new water until they are full. You cannot partially fill any Jar with an arbitrary amount of new water.")
	print ("You can pass water between Jars. However, you cannot know exactly how many liters have been passed to the other Jar by simply puring small amounts of water.")
	print ("However, you deduce the amount of water that a Jar has if you transfer water between them.")
	print ("You will have to specify both the Jar A and Jar B capacity in liters.")
	print ("You will also have to specify how many liters the algorithm has to reach")
	print ("Get wet and let water transfer begin...Start!")
	#print ("Start!")
	
def JarAEmpty():
	print ("Jar A is now empty")

def JarBEmpty():
	print ("Jar B is now empty")

def JarAFull():
	print ("Jar A is full! ")

def JarBFull():
	print ("Jar B is full!")
	
def DisplayA():
	global JarA
	print ("Jar A has:",JarA,"liters")

def DisplayB():
	global JarB
	print ("Jar B has:",JarB,"liters")	

def PrintMaxValues():
	global JarAMaxVolume
	global JarBMaxVolume
	global JarVolume
	print ("Jar A maximum value is:",JarAMaxVolume,"liters")
	print ("Jar B maximum value is:",JarBMaxVolume,"liters")
	print ("liters to find are:",JarVolume,"liters")
	
def PrintCurrentStatus():
	DisplayA()
	DisplayB()
	print("")
	
def PrintFromAtoB( x ):
	print ("You passed",x,"liters of water from Jar A to Jar B ")

def PrintFromBtoA( x ):
	print ("You passed",x,"liters of water from Jar B to Jar A ")	

def FillJar( x ):
	global JarA
	global JarB
	if (x == Jars.A):
		JarA = JarAMaxVolume
	if (x == Jars.B):
		JarB = JarBMaxVolume
		
def PassFromAtoB():
	global JarA
	global JarB
	
	print("Passing water from Jar B to Jar A")
	for x in range(0,JarBMaxVolume):
		if ( JarB == 0 ):
			print("Jar B is empty! Refill Jar B to continue")
			FillJar(Jars.B)
			print("Jar B is full again and Jar A contains",JarA,"liters")
			break
		elif (JarA == JarAMaxVolume):
			print("Jar A is full! Empty the Jar to continue...")
			JarA = 0
			print("Jar A is now empty and Jar B contains",JarB,"liters")
			break
		else:
			JarB = JarB - 1
			JarA = JarA + 1
	print("The status of the Jars for this iteration is the following:")
	PrintCurrentStatus()


def askForInput():
	global JarAMaxVolume
	global JarBMaxVolume
	global JarVolume
	
	print("Please introduce Jar A maximum volume")
	JarAMaxVolume = int(input())
	#JarBMaxVolume = 5
	print("Please introduce Jar B maximum volume")
	JarBMaxVolume = int(input())
	#JarBMaxVolume = 3
	print("Please introduce the liters to find")
	JarVolume = int(input())
	#JarVolume = 2

def runTest():
	for x in range(0,99):
		y = x+1
		print("Now starting iteration",y)
		PassFromAtoB()
		if ( (JarB == JarVolume) or (JarA == JarVolume) ):
			print("During iteration:",y,"we found the specified volume of",JarVolume,"liters")
			break	
		
########################################################################

#main program execution
#PrintInstructionsWithTime()
askForInput()
PrintMaxValues()
PrintCurrentStatus()
print("Filling Jar B to start to find the correct volume...")
FillJar(Jars.B)
runTest()
