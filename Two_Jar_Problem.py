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
from Module_Definitions import PrintInstructionsWithTime, PrintInstructionsNoTime

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
JarBMaxVolume = 3
PassToA = 98
PassToB = 12

#Define functions
def debugFunction():
	global debugRules
	print ("Print debug information? (Y/N)")
	debuginfo = input()
	if ( debuginfo == "N" or debuginfo == "n"):
		debugRules = 0
	else:
		debugRules = 1

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
			#print(JarB)
		elif (JarA == JarAMaxVolume):
			JarAFull()
		else:
			JarB = JarB - 1
			JarA = JarA + 1
	elif ( x == PassToB) :
		print ("Passing water from Jar A to Jar B")
		if ( JarA == 0 ):
			JarAEmpty()
			#print(JarB)
		elif (JarB == JarBMaxVolume):
			JarBFull()
		else:
			JarB = JarB + 1
			JarA = JarA - 1

def PassAllWaterTo( x ):
	global JarA
	global JarB
	
	if ( x == PassToA ):
		print ("Passing ALL water from Jar B to Jar A")
		while True:
			if ( JarB == 0 ):
				JarBEmpty()
				print(JarA)
				break
			if ( JarA == JarAMaxVolume ):
				JarA = 0
				print("Rule 5 / Rule 12")
			JarB = JarB - 1
			JarA = JarA + 1	
		
	elif ( x == PassToB) :
		print ("Passing ALL water from Jar A to Jar B")
		while True:
			if ( JarA == 0 ):
				JarAEmpty()
				print(JarB)
				break
			if ( JarB == JarBMaxVolume ):
				JarB = 0
				print("Rule 6")
			JarA = JarA - 1
			JarB = JarB + 1
			

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
	global debugRules
	if ( debugRules == 1 ):
		print ("Rule 9")
	pass

#This function will pass completely the content of Jar B into Jar A
def RuleTen():
	global debugRules
	if ( debugRules == 1 ):
		print ("Rule 10")
	pass
#This function will pass 2 liters of water from Jar B into Jar A
def RuleEleven():
	global debugRules
	if ( debugRules == 1 ):
		print ("Rule 11")
	pass

#This function will completely empty Jar A
def RuleTwelve():
	global debugRules
	if ( debugRules == 1 ):
		print ("Rule 12")
	pass


#End of definitions

#Main program


debugFunction()
askForInitialJarsVolume()
PassAllWaterTo(PassToB)