#Problema: "Se tienes dos jarras, una de cuatro litros de capacidad y otra de tres. 
#Ninguna de ellas tiene marcas de medición. Se tiene una llave que permite llenar las jarras de agua. 
#¿Cómo se puede lograr tener exactamente dos litros de agua en la jarra de cuatro litros de capacidad?."

#Desarrollar un programa que, dado el estado inicial de las dos jarras por parte del usuario,
#y encuentre la solución aplicando las reglas de producción siguientes:

#El programa debe desplegar (en lista) el nodo (estado de las jarras) y la regla aplicada.

#El programa debe estar documentado (comentarios dentro del código que informe el desarrollador,
#fecha, título del programa y un breve resumen del objetivo del programa e instrucciones de funcionamiento.

#Elementos extras a considerar: Despliegue grafico de la información. 
#Graficación del arbol de búsquedas, traslado en el árbol.

#Selección del lenguaje a utilizar: Python . Archivos a entregar: Código fuente.

#TwoJarsProblem
#March 3, 2019
#Luis Rojas
#19550002


import time

#Define variables
JarA = 0	#User can input the values
JarB = 0	#User can input the values

#define enumerators
from enum import Enum
class Jars(Enum):
	A = 0
	B = 1

debugRules = 0
JarAInitialVolume = 0
JarBInitialVolume = 0
JarAMaxVolume = 4
JarBMaxVolume = 4
PassToA = 98
PassToA = 12

#Define functions
def debugFunction():
	global debugRules
	print ("Print debug information? (Y/N)")
	debuginfo = input()
	if ( debuginfo == "N" or debuginfo == "n"):
		debugRules = 0
	else:
		debugRules = 1

def PrintInstructionsWithTime():
	print ("Welcome to the Two Jar problem, where you get problems, with jars, at no cost.")
	time.sleep(0.5)
	print ("There are two Jars. None of the Jars has marks that show the level in any measurement.")
	time.sleep(0.5)
	print ("The purpose is to reach certain amount of water in a Jar given two Jars of different measures.")
	time.sleep(0.5)
	print ("For example: given a Jar of 4 L and another one of 3 L, get 2 L.")
	time.sleep(0.5)
	print ("You can only fill the Jars with new water until they are full. You cannot partially fill any Jar with an arbitrary amount of new water.")
	time.sleep(0.5)
	print ("You can pass water between Jars. However, you cannot know exactly how many liters have been passed to the other Jar by simply puring small amounts of water.")
	time.sleep(0.5)
	print ("However, you deduce the amount of water that a Jar has if you transfer water between them.")
	time.sleep(0.5)
	print ("Let water transfer begin.")
	time.sleep(0.5)
	print ("Jar A has a capacity of 4 liters.")
	time.sleep(0.5)	
	print ("Jar B has a capacity of 3 liters.")
	time.sleep(0.5)	
	print ("You need to reach exactly 2 liters")
	time.sleep(0.5)	
	print ("Start!")
	time.sleep(0.5)

def PrintInstructionsNoTime():
	print ("Welcome to the Two Jar problem, where you get problems, with jars, at no cost.")
	print ("There are two Jars. None of the Jars has marks that show the level in any measurement.")
	print ("The purpose is to reach certain amount of water in a Jar given two Jars of different measures.")
	print ("For example: given a Jar of 4 L and another one of 3 L, get 2 L.")
	print ("You can only fill the Jars with new water until they are full. You cannot partially fill any Jar with an arbitrary amount of new water.")
	print ("You can pass water between Jars. However, you cannot know exactly how many liters have been passed to the other Jar by simply puring small amounts of water.")
	print ("However, you deduce the amount of water that a Jar has if you transfer water between them.")
	print ("Let water transfer begin.")
	print ("Jar A has a capacity of 4 liters.")
	print ("Jar B has a capacity of 3 liters.")
	print ("You need to reach exactly 2 liters")
	print ("Start!")

#Jar X status alerts.
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

# Print starting information
def PrintStartInfo():
	global JarAMaxVolume
	global JarBMaxVolume
	global JarVolume
	print ("Jar A maximum value is: 4 liters")
	print ("Jar A initial value is:", JarAInitialVolume,"liters")
	print ("Jar B maximum value is: 3 liters")
	print ("Jar B initial value is:", JarBInitialVolume,"liters")
	print ("Amount of water to find: 2 liters")

# Function used to print the current water status of both Jars	
def PrintCurrentStatus():
	DisplayA()
	DisplayB()
	print ("")

def PrintFromAtoB( x ):
	print ("You passed",x,"liters of water from Jar A to Jar B ")

def PrintFromBtoA( x ):
	print ("You passed",x,"liters of water from Jar B to Jar A ")	

# Function used to fill both Jars
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
	
	if ( x == PassToA ):
		print ("Passing water from Jar B to Jar A")
		if ( JarB == 0 ):
			JarBEmpty()
		elif (JarA == JarAMaxVolume):
			JarAFull()
		else:
			JarB = JarB - 1
			JarA = JarA + 1
	elif ( x == PassToB) :
		print ("Passing water from Jar A to Jar B")
		if ( JarA == 0 ):
			JarAEmpty()
		elif (JarB == JarBMaxVolume):
			JarBFull()
		else:
			JarB = JarB + 1
			JarA = JarA - 1

# Function used to set the initial values for both Jars
def askForInitialJarsVolume():
	global JarAInitialVolume
	global JarBInitialVolume
	global JarA
	global JarB
	
	print ("Please introduce Jar A initial volume")
	JarAInitialVolume = int(input())
	print ("Please introduce Jar B initial volume")
	JarBInitialVolume = int(input())
	print ("Jar A starts at", JarAInitialVolume,"and Jar B starts at",JarBInitialVolume)
	JarA = JarAInitialVolume
	JarB = JarBInitialVolume
	

# Unused function to introduce maximum volume for Jar A and Jar B as well as to
# set the liters to find.
def askForMaxVolumeInput():
	global JarAMaxVolume
	global JarBMaxVolume
	global JarVolume
	
	print ("Please introduce Jar A volume")
	JarAMaxVolume = int(input())
	#JarBMaxVolume = 5
	print ("Please introduce Jar B volume")
	JarBMaxVolume = int(input())
	#JarBMaxVolume = 3
	print ("Please introduce the liters to find")
	JarVolume = int(input())
	#JarVolume = 2
def runTest():
	for x in range(0,999):
		y = x+1
		print ("Now starting iteration",y)
		PassFromAtoB()
		if ( (JarB == JarVolume) or (JarA == JarVolume) ):
			print ("During iteration:",y,"we found the combination")
			return (True)
	return (False)

def startProgram():
	if ( runTest() == False ):
		print ("Solution not found :(")
		print ("Would you consider changing the numbers? If so, please run the program again!")
	else:
		print ("Finished test run!")
	
# This function fills Jar A
def RuleOne():
	global debugRules
	if ( debugRules == 1 ):
		print ("Rule 1")
		print ("Now filling Jar A")
	FillJar( Jars.A )
	JarAFull()

# This function fills Jar B
def RuleTwo():
	global debugRules
	if ( debugRules == 1 ):
		print ("Rule 2")
		print ("Now filling Jar B")
	FillJar( Jars.B )
	JarBFull()

# Empty Jar A by one liter
def RuleThree():
	global JarA
	global debugRules
	if ( debugRules == 1 ):
		print ("Rule 3")
	if (JarA == 0 ):
		if ( debugRules == 1 ):
			print ("Jar A was already empty :(")
	else:
		JarA = JarA - 1
		if ( debugRules == 1 ):
			print ("Now emptying Jar A a little")

# Empty Jar B by one liter
def RuleFour():
	global JarB
	global debugRules
	if ( debugRules == 1 ):
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
	global debugRules
	if ( debugRules == 1 ):
		print ("Rule 5")
	if ( debugRules == 1 ):
		print ("Emptying Jar A")
	JarA = 0
	JarAEmpty()

# This function will empty Jar B
def RuleSix():
	global JarB
	global debugRules
	if ( debugRules == 1 ):
		print ("Rule 6")
		print ("Emptying Jar B")
		
	JarB = 0
	JarBEmpty()
#Jar A = 4 liters
#Jar B = 3 liters

# This function will pass water from Jar B to Jar A
def RuleSeven():
	global debugRules
	if ( debugRules == 1 ):
		print ("Rule 7")
		print ("Passing water from Jar B to Jar A")
	PassWaterTo( PassToA )

# This function will pass water from Jar A to Jar B
def RuleEight():
	global debugRules
	if ( debugRules == 1 ):
		print ("Rule 8")
		print ("Passing water from Jar A to Jar B")
	PassWaterTo( PassToB )

#This function will pass completely the content of Jar A into Jar B
def RuleNine():
	pass

def RuleTen():
	pass

def RuleEleven():
	pass

def RuleTwelve():
	pass


#End of definitions

#Main program

debugFunction()
askForInitialJarsVolume()
RuleOne()