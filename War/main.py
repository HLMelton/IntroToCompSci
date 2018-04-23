import random

def shuffled_deck():
    basic_deck = list(range(2, 15)) * 4
    random.shuffle(basic_deck)
    return basic_deck
    
deck = shuffled_deck()
p1deck,p2deck = deck[::2],deck[1::2]
p1point,p2point = 0,0
holder = []

def war (p1,p2):
    chng = 1
    if p1 == p2:
        #issue present here with appending the card to the holder
        holder.append(p1deck[x])
        holder.append(p2deck[x])
        holderlen = len(holder)
        war(p1deck[x+1],p2deck[x+1])
    elif p1 < p2:
        if len(holder) == 2:
            chng +=1
        p2point +=chng
        holder = []
    else: 
        if len(holder) == 2:
            chng +=1
        p1point +=chng
        holder = []
def turn(turnnum):
    global p1point
    global p2point
    p1 = p1deck[turnnum]
    p2 = p2deck[turnnum]
    if p1 > p2:
        p1point+=1
    elif p1 == p2:
        war(p1,p2)
    else:
        p2point+=1

for x in range(25):
    turn(x)
print(p1point, p2point)
