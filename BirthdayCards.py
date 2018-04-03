#This assignment was intended to introduce the concept of functions to the class, though this was all done within the span of 20 mins.
#------------------------------

import random

#Variables
number = ['Ace', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suit = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
name = "" 

#Functions
def birthday_song (name):
  print("Happy birthday " + name)
  
def pick_a_card():
  n = number[random.randint(0,13)]
  s = suit[random.randint(0,3)]
  print(n+' of '+s)
  
print('Enter "next function to shuffle the deck"')  
#Birthday Function
while name != "next function":  
  name = input("Who's birthday is it?")
  if name != "next function":
    birthday_song(name)
  else:
    print("Shuffling the deck... \b")
    
#Pick a card Function
x = int(input("How many cards would you like?"))
for m in range(x):
  pick_a_card()
  
  
