import random

ball = ['It is certain','It is decidedly so','Without a doubt','Yes, definitely','You may rely on it','As I see it, yes','Most likely','Outlook good','Yes','Signs point to yes','Reply hazy, try again','Ask again later','Better not tell you now','Cannot predict','Concentrate and ask again',"Don't count on it",'My sources say no','Outlook not so good','Very doubtful']
#testball = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print('Welcome to the 8Ball-God.\nIf you would like to quit, say "quit"')
q = 0
x = 3
while q == 0:
  question = input("Your question?")
  question.lower()
  if question.lower() == "what is the music of life":
    print('Silence, my brother')
    q = 1
  elif question.startswith('what') or question.startswith('can'):
    n = random.randint(0,19)
    print(ball[n]+"\n")
  elif question.startswith('who'):
    print('Dude, I dont know anyone but you\n')
  elif question.lower() == "quit":
    print("Thank you for visiting the Eight Ball God")
    q = 1
  elif len(question) <= 0:
    print("If I wanted silence, I would be drinking my tea")
    x-=1
    if x == 0:
      print("\nI've no time for your childishness")
      q = 1
  else:
    print("Listen man, im just an eightball, not a therapist")

