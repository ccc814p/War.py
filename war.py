import random
tile1 = 1
tile2 = 2
p1army = 2
p2army = 2
p1turn = False
p2turn = False
print("Welcome to War.py!")
print(tile1, tile2)
print(p1army, p2army)
rdv = random.randint(1, 2)
if rdv == 1:
  p1turn = True
else:
  p2turn = True
while True:
  if p1turn == True:
    p1 = input("Player 1, what shall you do?\n")
    if p1 == 'attack':
      die1 = random.randint(1, 2)
      if die1 == 1:
        tile2 = 1
        p2army = p2army - 1
      if die1 == 2:
        tile2 = 2
        p1army = p1army - 1
    if p1 == 'increase armies':
      p1army = p1army + 1
    print(tile1, tile2)
    print(p1army, p2army)
    if (tile1 + tile2) == 2: 
      p1turn = False
      p2turn = False
      print("Player 1 wins!")
    else:
      p1turn = False
      p2turn = True
    if p1army == 0:
      p1turn = False
      p2turn = False
      print("Player 2 wins!")
  if p2turn == True:
    p2 = input("Player 2, what shall you do?\n")
    if p2 == 'attack':
      die2 = random.randint(1, 2)
      if die2 == 1:
        tile1 = 2
        p1army = p1army - 1
      if die2 == 2:
        tile1 = 1
        p2army = p2army - 1   
    if p2 == 'increase armies':
      p2army = p2army + 1
    print(tile1, tile2)
    print(p1army, p2army)
    if (tile1 + tile2) == 4: 
      p1turn = False
      p2turn = False
      print("Player 2 wins!")
    else:
      p1turn = True
      p2turn = False
    if p2army == 0:
      p1turn = False
      p2turn = False
      print("Player 1 wins!")