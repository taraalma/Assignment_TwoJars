#TwoJarsProblem
#March 3, 2019
#Luis Rojas
#19550002

#Instructions:
# Run the program. Preferably, in a console!
# follow the instructions printed on the console

import time
import random


#define enumerators
from enum import Enum
class Jars(Enum):
	A = 0
	B = 1

#Start variables initialization
JarA = 0	#User can input the values
JarB = 0	#User can input the values

printRules = 0					# Flag to signal the rules being applied.
debugRules = 0					# Flag to show status to developer.
printStatus = 0					# Flag used to show the status of the jars 
								# at the end of some operations

JarAInitialVolume = 0			# Jar A initial amount of liters
JarBInitialVolume = 0			# Jar B initial amount of liters
JarAMaxVolume = 4				# Maximum liters Jar A can hold
JarBMaxVolume = 3				# Maximum liters Jar B can hold
PassToA = 98					# Magic number to avoid repetition
PassToB = 12					# Magic number to avoid repetition
maximumCyclesToRun = 0			# Number of maximum numbers to run program
ProgramIsFinishedFlag = False	# Flag to signal that the program is complete
#End variables initialization

#Start of function definitions
def debugFunction():
	global printRules
	global debugRules
	global printStatus
	print ("Print Rules? (Y/N)")
	debuginfo = input()
	if ( debuginfo == "N" or debuginfo == "n"):
		printRules = 0
	else:
		printRules = 1
	
	print ("Print debug information? (Y/N)")
	debuginfo = input()
	if ( debuginfo == "N" or debuginfo == "n"):
		debugRules = 0
	else:
		debugRules = 1

	print ("Print Jars status? (Y/N)")
	debuginfo = input()
	if ( debuginfo == "N" or debuginfo == "n"):
		printStatus = 0
	else:
		printStatus = 1	


def releaseInitialFunction():
	global printRules
	global debugRules
	global printStatus
	
	printRules = 1
	debugRules = 0
	printStatus = 1	

		
#Jar X status alerts.
def PrintJarAEmpty():
	print ("Jar A is now empty")

def PrintJarBEmpty():
	print ("Jar B is now empty")

def PrintJarAFull():
	print ("Jar A is full! ")

def PrintJarBFull():
	print ("Jar B is full!")
	
def PrintJarAStatus():
	global JarA
	print ("Jar A has:",JarA,"liters")

def PrintJarBStatus():
	global JarB
	print ("Jar B has:",JarB,"liters")	

#print instructions
def PrintInstructionsWithTime():
	print ("Welcome to the Two Jar problem, where you get problems, with jars, at no cost.")
	time.sleep(3)
	print ("There are two Jars. None of the Jars has marks that show the level in any measurement.")
	time.sleep(3)
	print ("The purpose is to reach certain amount of water in a Jar given two Jars of different measures.")
	time.sleep(3)
	print ("For example: given a Jar of 4 L and another one of 3 L, get 2 L.")
	time.sleep(3)
	print ("You can only fill the Jars with new water until they are full. You cannot partially fill any Jar with an arbitrary amount of new water.")
	time.sleep(3)
	print ("You can pass water between Jars. However, you cannot know exactly how many liters have been passed to the other Jar by simply puring small amounts of water.")
	time.sleep(3)
	print ("However, you deduce the amount of water that a Jar has if you transfer water between them.")
	time.sleep(3)
	print ("Let water transfer begin.")
	time.sleep(3)
	print ("Jar A has a capacity of 4 liters.")
	time.sleep(3)	
	print ("Jar B has a capacity of 3 liters.")
	time.sleep(3)	
	print ("You need to reach exactly 2 liters")
	time.sleep(3)	
	print ("Please insert the initial value of the jars")
	time.sleep(3)

	
# Print starting information
def PrintStartInfo():
	global JarAInitialVolume
	global JarBInitialVolume
	
	print ("Jar A maximum value is: 4 liters")
	print ("Jar A initial value is:", JarAInitialVolume,"liters")
	print ("Jar B maximum value is: 3 liters")
	print ("Jar B initial value is:", JarBInitialVolume,"liters")
	print ("Amount of water to find: 2 liters")

# Function used to print the current water status of both Jars	
def PrintCurrentStatus():
	PrintJarAStatus()
	PrintJarBStatus()
	print ("")

def PrintFromAtoB( x ):
	print ("You passed",x,"liters of water from Jar A to Jar B ")

def PrintFromBtoA( x ):
	print ("You passed",x,"liters of water from Jar B to Jar A ")	

# Function used to fill any of the Jars
def FillJar( x ):
	global JarA
	global JarB
	if (x == Jars.A):
		JarA = JarAMaxVolume
	if (x == Jars.B):
		JarB = JarBMaxVolume

# Function used to pass water between Jars
def PassWaterTo( x ):
	global JarA
	global JarB
	global printRules
	global debugRules
	global printStatus
	
	if ( x == PassToA ):
		if ( debugRules == 1 ):
			print ("Passing water from Jar B to Jar A")
		if ( JarB == 0 ):		# if Jar B is empty
			RuleTwo()			# fill Jar B
			if ( printStatus == 1 ):
				PrintCurrentStatus()
		if (JarA == JarAMaxVolume): 
			RuleFive()
			if ( printStatus == 1 ):
				PrintCurrentStatus()
			JarB = JarB - 1
			JarA = JarA + 1
			if ( printStatus == 1 ):
				PrintCurrentStatus()
		else:
			JarB = JarB - 1
			JarA = JarA + 1
			if ( printStatus == 1 ):
				PrintCurrentStatus()
	elif ( x == PassToB):
		if (debugRules==1):
			print ("Passing water from Jar A to Jar B")
		if ( JarA == 0 ):		# if Jar A is empty
			RuleOne()			# fill Jar B
			if ( printStatus == 1 ):
				PrintCurrentStatus()
		if (JarB == JarBMaxVolume): 
			RuleSix()
			if ( printStatus == 1 ):
				PrintCurrentStatus()
			JarA = JarA - 1
			JarB = JarB + 1
			if ( printStatus == 1 ):
				PrintCurrentStatus()
		else:
			JarA = JarA - 1
			JarB = JarB + 1
			if ( printStatus == 1 ):
				PrintCurrentStatus()

def PassAllWaterTo( x ):
	global JarA
	global JarB
	global printRules
	global debugRules
	global printStatus
	global JarAMaxVolume
	global JarBMaxVolume

	if ( x == PassToA ):
		if (debugRules == 1):
			print ("Passing ALL water from Jar B to Jar A")
		while True:
			if ( JarB == 0 ):
				if ( debugRules == 1):
					PrintJarBEmpty()
					print("The Jar A still has", JarA," Liters")
				break
			elif ( JarA == JarAMaxVolume ):
				if (printRules == 1):	
					print("Rule 5")
					RuleFive()
			else:
				JarB = JarB - 1
				JarA = JarA + 1
			if( printStatus == 1):
				PrintCurrentStatus()	
	elif ( x == PassToB):
		if (debugRules == 1):
			print ("Passing ALL water from Jar A to Jar B")
		while True:
			if ( JarA == 0 ):
				if ( debugRules == 1):
					PrintJarAEmpty()
					print("The Jar B still has", JarB," Liters")
				break
			elif ( JarB == JarBMaxVolume ):
				if (printRules == 1):	
					print("Rule 6")
					RuleSix()
			else:
				JarB = JarB + 1
				JarA = JarA - 1
			if( printStatus == 1):
				PrintCurrentStatus()

# Function used to set the initial values for both Jars
def askForInitialJarsVolume():
	global JarAInitialVolume
	global JarBInitialVolume
	global JarA
	global JarB
	global printRules
	global debugRules
	global printStatus
	
	print ("Please introduce Jar A initial volume")
	JarAInitialVolume = int(input())
	print ("Please introduce Jar B initial volume")
	JarBInitialVolume = int(input())
	print ("Start!")
	print ("")
	print ("")
	
	print ("Jar A starts at", JarAInitialVolume,"and Jar B starts at",JarBInitialVolume)
	JarA = JarAInitialVolume
	JarB = JarBInitialVolume

# This function fills Jar A
def RuleOne():
	global printRules
	global debugRules
	global printStatus
	global JarA
	global JarB
	
	if ( printRules == 1 ):
		print ("Rule 1")
	if ( debugRules == 1 ):
		print ("Now filling Jar A")
	FillJar( Jars.A )
	if (debugRules == 1):
		PrintJarAFull()

# This function fills Jar B
def RuleTwo():
	global printRules
	global debugRules
	global printStatus
	
	if ( printRules == 1 ):
		print ("Rule 2")
	if (debugRules == 1):
		print ("Now filling Jar B")
	
	FillJar( Jars.B )
	if (debugRules == 1):
		PrintJarBFull()

# Empty a little Jar A 
def RuleThree():
	global JarA
	global printRules
	global debugRules
	global printStatus
	
	if ( printRules == 1 ):
		print ("Rule 3")
	if (JarA == 0 ):
		if ( debugRules == 1 ):
			print ("Jar A was already empty :(")
	else:
		JarA = JarA - 1
		if ( debugRules == 1 ):
			print ("Now emptying Jar A a little")

# Empty a little Jar B 
def RuleFour():
	global JarB
	global printRules
	global debugRules
	global printStatus
	
	if ( printRules == 1 ):
		print ("Rule 4")
	if (JarB == 0):
		if ( debugRules == 1 ):
			print ("Jar B was already empty :(")
	else:
		JarB = JarB - 1
		if ( debugRules == 1 ):
			print ("Emptying Jar B a little...")

# This function will empty Jar A
def RuleFive():
	global JarA
	global printRules
	global debugRules
	global printStatus
	
	if ( printRules == 1 ):
		print ("Rule 5")
	if ( debugRules == 1 ):
		print ("Emptying Jar A")
	JarA = 0
	if ( debugRules == 1 ):
		PrintJarAEmpty()

# This function will empty Jar B
def RuleSix():
	global JarB
	global printRules
	global debugRules
	global printStatus
	
	if ( printRules == 1 ):
		print ("Rule 6")
	if ( debugRules == 1):
		print ("Emptying Jar B")
		
	JarB = 0
	if ( debugRules == 1 ):
		PrintJarBEmpty()
#Jar A = 4 liters
#Jar B = 3 liters

# This function will pass water from Jar B to Jar A
def RuleSeven():
	global printRules
	global debugRules
	global printStatus
	
	if ( printRules == 1 ):
		print ("Rule 7")
	if ( debugRules == 1):
		print ("Passing water from Jar B to Jar A")
	PassWaterTo( PassToA )

# This function will pass water from Jar A to Jar B
def RuleEight():
	global printRules
	global debugRules
	global printStatus
	
	if ( printRules == 1 ):
		print ("Rule 8")
	if ( debugRules == 1 ):
		print ("Passing water from Jar A to Jar B")
	PassWaterTo( PassToB )

#This function will pass completely the content of Jar A into Jar B
def RuleNine():
	global printRules
	global debugRules
	global printStatus
	
	if ( printRules == 1 ):
		print ("Rule 9")
	PassAllWaterTo(PassToB)

#This function will pass completely the content of Jar B into Jar A
def RuleTen():
	global printRules
	global debugRules
	global printStatus
	
	if ( printRules == 1 ):
		print ("Rule 10")
	PassAllWaterTo(PassToA)
	
#This function will pass 2 liters of water from Jar B into Jar A
def RuleEleven():
	global printRules
	global debugRules
	global printStatus
	
	if ( printRules == 1 ):
		print ("Rule 11")
	for x in range(1,3):
		PassWaterTo(PassToA)

#This function will completely empty Jar A
def RuleTwelve():
	global JarA
	global printRules
	global debugRules
	global printStatus
	
	if ( printRules == 1 ):
		print ("Rule 12")
	JarA = 0

def CloseInOneMinute ( ):
	time.sleep(10)
	time.sleep(10)
	time.sleep(10)
	time.sleep(10)
	time.sleep(10)
	time.sleep(10)
	
#This function will check when the 2 liters are found
def HaveWeFinished ( ):
	global JarA
	global JarB
	global ProgramIsFinishedFlag
	if (JarA == 2 and JarB == 2 ):
		ProgramIsFinishedFlag = True
		print("FINISHED")
		return(True)
	elif (JarB == 2 and JarA == 4):
		ProgramIsFinishedFlag = True
		#RuleFive()
		print("FINISHED")
		return(True)
	elif (JarA == 2 and JarB == 3):
		ProgramIsFinishedFlag = True
		#RuleSix()
		print("FINISHED")
		return(True)	

#This function will initialize the program
def startProgram():
	global JarA
	global JarB
	global printStatus
	global maximumCyclesToRun
	global printRules
	global debugRules
	global printStatus
	global ProgramIsFinishedFlag

	while ( True ):
	
		if ( JarA > JarB ):						
			# keep passing water until you eventually find the solution
			
			for x in range ( 0, 15):
				RuleSeven()
				if ( HaveWeFinished() ):
					break
			break

		elif ( JarA < JarB ):
			# keep passing water until you eventually find the solution
			for x in range ( 0, 15):
				RuleEight()
				if ( HaveWeFinished() ):
					break
			break
			
		elif ( JarB == JarA ) :
			# if both are equal at start, the program will randomly 
			# decide to fill one and empty the other
			evaluarRandom = random.randint(1,2)		
			if ( evaluarRandom == 1 ):
				RuleOne()
				RuleSix()
			else:
				RuleTwo()
				RuleFive()
		else:
			break

	print (	"The program has actually found the solution!")
	print (	"" )
	print (	"" )
	print (	"" )
	print (	"You can now close this windows.")
	print (	"This window will automatically close in 2 minutes...")
	CloseInOneMinute()
	CloseInOneMinute()
	

#End of function definitions

#Main program
#debugFunction()


PrintInstructionsWithTime()
releaseInitialFunction()
askForInitialJarsVolume()
startProgram()