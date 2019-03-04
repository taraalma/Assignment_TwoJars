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

JarAInitialVolume = 0
JarBInitialVolume = 0
JarAMaxVolume = 4
JarBMaxVolume = 4

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
	print("")

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
	
	if ( x == JarA ):
		print("Passing water from Jar B to Jar A")
		
		if ( JarB == 0 ):
			print("Jar B is empty! Refill Jar B to continue")
			FillJar(Jars.B)
			print("Jar B is full again and Jar A contains",JarA,"liters")
			
		elif (JarA == JarAMaxVolume):
			print("Jar A is full! Empty the Jar to continue...")
			JarA = 0
			print("Jar A is now empty and Jar B contains",JarB,"liters")
			
		else:
			JarB = JarB - 1
			JarA = JarA + 1
		
		
	else :
		print("Passing water from Jar A to Jar B")
		for x in range(0,JarAMaxVolume):
			if ( JarA == 0 ):
				print("Jar A is empty! Refill Jar A to continue")
				FillJar(Jars.A)
				print("Jar A is full again and Jar B contains",JarA,"liters")
				break
			elif (JarB == JarBMaxVolume):
				print("Jar B is full! Empty the Jar to continue...")
				JarB = 0
				print("Jar B is now empty and Jar A contains",JarA,"liters")
				break
			else:
				JarB = JarB + 1
				JarA = JarA - 1
		print("The status of the Jars for this iteration is the following:")
		PrintCurrentStatus()

# Function used to set the initial values for both Jars
def askForInitialJarsVolume():
	global JarAInitialVolume
	global JarBInitialVolume
	
	print("Please introduce Jar A initial volume")
	JarAInitialVolume = int(input())
	print("Please introduce Jar B initial volume")
	JarBInitialVolume = int(input())
	print("Jar A starts at", JarAInitialVolume,"and Jar B starts at",JarBInitialVolume)

# Unused function to introduce maximum volume for Jar A and Jar B as well as to
# set the liters to find.
def askForMaxVolumeInput():
	global JarAMaxVolume
	global JarBMaxVolume
	global JarVolume
	
	print("Please introduce Jar A volume")
	JarAMaxVolume = int(input())
	#JarBMaxVolume = 5
	print("Please introduce Jar B volume")
	JarBMaxVolume = int(input())
	#JarBMaxVolume = 3
	print("Please introduce the liters to find")
	JarVolume = int(input())
	#JarVolume = 2
def runTest():
	for x in range(0,999):
		y = x+1
		print("Now starting iteration",y)
		PassFromAtoB()
		if ( (JarB == JarVolume) or (JarA == JarVolume) ):
			print("During iteration:",y,"we found the combination")
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
	FillJar( Jars.A )
	JarAFull()

# This function fills Jar B
def RuleTwo():	
	FillJar( Jars.B )
	JarBFull()

# Empty Jar A by one liter
def RuleThree():
	global JarA
	if (JarA == 0 ):
		print("Can't empty something already void :(")
	else:
		JarA = JarA - 1

# Empty Jar B by one liter
def RuleFour():
	global JarB
	if (JarB == 0):
		print("Can't empty something already void :(")
	else:
		JarB = JarB - 1

# This function will empty Jar A
def RuleFive():
	global JarA
	JarA = 0
	JarAEmpty()

# This function will empty Jar B
def RuleSix():
	global JarB
	JarB = 0
	JarBEmpty()
# This function will pass water from Jar B to Jar A
def RuleSeven():
	PassWaterTo( JarA )
# This function will pass water from Jar A to Jar B
def RuleNine():
	PassWaterTo( JarB )

def RuleTen():
	pass

def RuleEleven():
	pass

def RuleTwelve():
	pass


#End of definitions

#Main program

