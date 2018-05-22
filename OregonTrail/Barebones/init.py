from random import randint as rng
import json

initstr = "  __Westward__\n"+"   New || Load " +"\n"+"\n-Select Game Type-"+"\n__________________"
dist = 2000
time = 24
exhaustion = False
days = 45
distday = "Days to Winter = " + str(days)
#--------------------------------------------------------------
def write():
	pass

def loadg():
	pass

def init():
	inq = str(input(initstr)).lower()	
	while loopa == 1:	
		if inq == "load":
			loadg()
		elif inq == "new":
			write()
		else:
			print("Enter Valid Option")
#--------------------------------------------------------------
def start():
	global family
	global familyname
	family = []
	familyname = str(input("Your Surname?"))
	famsize = int(input("How large is your family?"))
	if famsize == 1:
		print("You're bold to head west alone.")
	else:
		for name in range(int(input())):
			name = input("What is your family member's name?")
			family.append(name)
			print("Okay, got "+name+" "+familyname)
		for member in family:
			print(member + " " + familyname)
		print("Alright, I've you on the roster. You're good to go!")

#def travel():
#	sprint = input("Would you like to sprint today's distance")
#	if sprint.lower() == "yes":
#		roll = rng(1,10)
#		rollcp = rng(1,10)
#		if roll > rollcp:
#			status = True
#		else:
#			status = False
#		sprint(status)
#	else:
#		hours = input("How many hours would you like to travel?")
#		while heure < 16:
#			if hours > 8:
#				global exhaustion
#				exhaustion = True
#			else: 
#				trvl = rng(1,250)
#				global dist
#				dist = dist - trvl	

def travel(dist):
	
	trvdist = rng()
	
	dist = dist + trvdist
	return dist
			
def admin():
	global dist
	dist = input("Distance?")

def rest(dmg):
	sleep = input("Would you like to SLEEP or REST")
	global exhaustion
	if sleep == "SLEEP":
		pass
		#add a day to the 
	elif sleep == "REST":
		pass
		#subtract hours from the day
	pass
	
def hunt(food):
	
	pass

def status(dmg, food, family, supp):
	#presents the status of the wagon
	pass
	
def help():
	pass
	
def quit():
	pass
	
def endgame():
	pass
	
def settings():
	menu = input("Which meny would you like to access?\nHelp\nQuit\nAdmin")
	if menu == help:
		help()
	elif menu == quit:
		gamerunning == false	
	
def day():
	global date
	global dist
	date=+1
	print("Your are "+str(dist))
	heure = 0
	while heure < 16:
		wake()
		actioninq = str(input("What would you like to do today?"))
		if actioninq.lower() == "hunt":
			hunt()
		elif actioninq.lower() == "rest":
			rest()
		elif actioninq.lower() == "travel":
			travel()
		elif actioninq.lower() == "settings":
			settings()		
	
travel()
