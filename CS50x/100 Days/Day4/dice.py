import random
print(r'''
  _______
  /\ o o o\
 /o \ o o o\_______
<    >------>   o /|
 \ o/  o   /_____/o|
  \/______/     |oo|
        |   o   |o/
        |_______|/
''')

dice = random.randint(1,6)
print(dice)

if dice == 1:
    print(r'''
        ________
        |       |
        |   o   |
        |_______|

         ''')

elif dice == 2:
    print(r'''

         _______
        |       |
        | o  o  |
        |_______|

          ''')