from random import randint as rng

dist = 2000
days = 303
food = 500
health = 5
family = []

def start():
    global family
    global familyname
    global alive
    family = []
    familyname = str(input("Your family name?"))
    famsize = int(input("How large is your family?"))
    if famsize == 1:
        print("You're bold to head west alone.")
    else:
        for name in range(famsize):
            name = input("What is your family member's name?")
            family.append(name)
            print("Okay, got " + name + " " + familyname)
        for member in family:
            print(member + " " + familyname)
        print("Alright, I've you on the roster. You're good to go!\n")
    alive = True

#-----Base Functions-----

def travel():
    global days
    global dist
    global health
    global food
    trvdist = rng(100,250)
    damage = rng(0,1)
    if trvdist > 150 and damage == 1:
        print("Your wagon was damaged...")
        health-=1
    dist -= trvdist
    days -= 1
    food -= rng(50,100)

def rest():
    global days
    global health
    global food
    health +=1
    attack = rng(0,1)
    if attack == 0:
        food-=rng(50,150)
        print("You were robbed in the night and lost some food")
        days=-rng(2,5)
    else:
        food-=25
        days-=1



def hunt():
    prey = input("What are you hunting for?\nBison | Rabbits | Deer | People")
    hunt = True
    while hunt == True:
        if prey.lower() == "people":
            print("Well that is unlawful.")
            loot = rng(100,200)
            global family
            global health
            if loot >= 170:
                victim = family[rng(1,len(family))]
                family = family.remove(victim)
                print("In the attack, "+str(victim)+" was found dead....")
            hunt = False
        elif prey.lower() == "bison":
            print("You spot some bison in the distance.")
            loot = rng(150,200)
            hunt = False
        elif prey.lower() == "rabbits":
            print("You find rabbit droppings nearby and set out some snares.")
            loot = rng(50,150)
            hunt = False
        elif prey.lower() == "deer":
            print("You spotted some deer in the distance.")
            loot = rng(100,150)
            hunt = False
    print("You loot "+str(loot)+" from your hunt.")
    global food
    food += loot
    if food >= 500:
        food = 500
    global days
    days -=rng(2,5)
    return food

def status(food, health, dist):
    print("Food : "+str(food)+"\nHealth : "+str(health)+"\nDistance : "+str(dist))

def help(dist):
    print("You are "+str(dist)+"from your destination.\n")
    print("You can REST, HUNT, TRAVEL, STATUS.\n")

print("-----Welcome to Westward!-----")
start()
while alive == True:
    if food <= 0:
        print("You starved to death")
        alive = False
        break
    elif days == 0:
        print("Winter came before you could make it.")
        alive = False
        break
    elif health <= 0:
        print("Your wagon crashed and your family was stranded.")
        alive = False
        break
    print("---Day "+str(days)+"---")
    action = str(input("What would you like to do today?"))
    if action.lower() == "rest":
        rest()
    elif action.lower() == "travel":
        travel()
    elif action.lower() == "hunt":
        hunt()
    elif action.lower() == "status":
        status(food, health, dist)
    elif action.lower() == "help":
        help()
    elif action.lower() == "quit":
        print("Thank you for playing")
        break
