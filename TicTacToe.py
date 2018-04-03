tic = ['-','-','-']
tac = ['-','-','-']
toe = ['-','-','-']
game = [tic,tac,toe]
win = 0
switch = 1
changex = 0
changey = 0
symbol = 'X'
turn = 0

print(game[0][0],'  |  ',game[0][1],'  |  ',game[0][2])
print('-------------------')
print(game[1][0],'  |  ',game[1][1],'  |  ',game[1][2])
print('-------------------')
print(game[2][0],'  |  ',game[2][1],'  |  ',game[2][2])
input('Welcome to Tic Tac Toe\nPress enter to continue')

def boardupdate(chgx,chgy):
  # / Change the value of ChangeOfY in the boolean \  
  # \ rather than when converting it to an integer /
  if chgx == 1:
    tic[chgy-1] = symbol
  elif chgx == 2:
    tac[chgy-1] = symbol
  else:
    toe[chgy-1] = symbol
def symbchg(k):
  if k == 'X':
    k = 'O'
  else:
    k = 'X'
  return k

while win != 1 or turn < 9:
  chgx = int(input('What row would you like to change?'))
  chgy = int(input('What column would you like to change?'))
  
  # ++Update board, symbol and turn++
  boardupdate(chgx,chgy)
  symbol = symbchg(symbol)
  turn =+1
  
  # ++Print screen++
  print( )
  print(game[0][0],'  |  ',game[0][1],'  |  ',game[0][2])
  print('-------------------')
  print(game[1][0],'  |  ',game[1][1],'  |  ',game[1][2])
  print('-------------------')
  print(game[2][0],'  |  ',game[2][1],'  |  ',game[2][2],)
