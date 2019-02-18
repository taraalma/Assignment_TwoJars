import time

#Define variables
JarA = 0	#Max = 5 L
JarB = 0	#Max = 3 L


#define enumerators
from enum import Enum
class Jars(Enum):
	A = 0
	B = 1

#Define functions
def PrintInstructionsWithTime():
	print ("Welcome to the Two Jar problem, where you get problems, with jars, at no cost.")
	time.sleep(0.5)
	print ("There are two Jars. None of the Jars has marks that show the level in any measurement.")
	time.sleep(0.5)
	print ("The purpose is to reach certain amount of water in a Jar given two Jars of different measures.")
	time.sleep(0.5)
	print ("For example: given a Jar of 3 L and 5 L, get 4 L.")
	time.sleep(0.5)
	print ("You can only fill the Jars with new water until they are full. You cannot partially fill any Jar with an arbitrary amount of new water.")
	time.sleep(0.5)
	print ("You can pass water between Jars. However, you cannot know exactly how many liters have been passed to the other Jar by simply puring small amounts of water.")
	time.sleep(0.5)
	print ("However, you deduce the amount of water that a Jar has if you transfer water between them.")
	time.sleep(0.5)
	print ("Let water transfer begin.")
	time.sleep(0.5)
	print ("Jar A has a capacity of 5 liters.")
	time.sleep(0.5)	
	print ("Jar B has a capacity of 3 liters.")
	time.sleep(0.5)	
	print ("You need to reach exactly 4 liters")
	time.sleep(0.5)	
	print ("Start!")
	time.sleep(0.5)

def PrintInstructionsNoTime():
	print ("Welcome to the Two Jar problem, where you get problems, with jars, at no cost.")
	print ("There are two Jars. None of the Jars has marks that show the level in any measurement.")
	print ("The purpose is to reach certain amount of water in a Jar given two Jars of different measures.")
	print ("For example: given a Jar of 3 L and 5 L, get 4 L.")
	print ("You can only fill the Jars with new water until they are full. You cannot partially fill any Jar with an arbitrary amount of new water.")
	print ("You can pass water between Jars. However, you cannot know exactly how many liters have been passed to the other Jar by simply puring small amounts of water.")
	print ("However, you deduce the amount of water that a Jar has if you transfer water between them.")
	print ("Let water transfer begin.")
	print ("Jar A has a capacity of 5 liters.")
	print ("Jar B has a capacity of 3 liters.")
	print ("You need to reach exactly 4 liters")
	print ("Start!")
	
def JarAEmpty():
	print ("Jar A is now empty")

def JarBEmpty():
	print ("Jar B is now empty")
	
def DisplayA():
	global JarA
	print ("Jar A has:",JarA,"liters")

def DisplayB():
	global JarB
	print ("Jar B has:",JarB,"liters")	

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
		JarA = 5
	if (x == Jars.B):
		JarB = 3
		
def PassFromAtoB():
	global JarA
	global JarB
	for x in range(0,JarB):
		if ( JarB == 0 ):
			JarBEmpty()
			break
		elif (JarA == JarAMaxVolume):
			JarAEmpty()
			break
		else:
			JarB = JarB - 1
			JarA = JarA + 1
			PrintCurrentStatus()
	
########################################################################

JarAMaxVolume = 5
JarBMaxVolume = 3

JarA = 4
FillJar(Jars.B)
PassFromAtoB()
