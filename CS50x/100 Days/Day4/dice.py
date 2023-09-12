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
        | o   o |
        |_______|

          ''')

elif dice == 3:
    print(r'''
         _______
        |       |
        | o o o |
        |_______|

          ''')

elif dice == 4:
    print(r'''
         _______
        | o   o |
        |       |
        |_o_ _o_|

          ''')

elif dice == 5:
    print(r'''
         _______
        | o   o |
        |   o   |
        |_o_ _o_|

          ''')

else:
    print(r'''
         _______
        | o   o |
        | o   o |
        |_o__ o_|

          ''')