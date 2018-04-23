import random

def shuffled_deck():
    basic_deck = list(range(2, 15)) * 4
    random.shuffle(basic_deck)
    return basic_deck
    
deck = shuffled_deck()
p1deck,p2deck = deck[::2],deck[1::2]
p1point,p2point = 0,0
holder = []

#-----Having an issue here where I append the values to the holder function
    holder.append(p1deck[x])
    holder.append(p2deck[x])
    war(p1deck[x],p2deck[x])
  elif p1 < p2:
    if len(holder) > 0:
        chng = 2
    p2point +=chng
  else: 
    if len(holder) > 0:
        chng = 2
    p1point +=chng

def turn(turnnum):
    global p1point
    global p2point
    p1 = p1deck[turnnum]
    p2 = p2deck[turnnum]
    if p1 > p2:
        p1point+=1
    elif p1 == p2:
        war()
    else:
        p2point+=1

for x in range(len(p1deck)):
    turn(x)
    x+=1
print(p1points, p2points)
