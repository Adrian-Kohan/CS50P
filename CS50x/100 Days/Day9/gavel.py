logo = r'''


                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\
'''

max = secret_auction[0][0]
    for i in range(len(secret_auction)):
        if secret_auction[0][0] < secret_auction[i][0]:
            max = secret_auction[i][0]
    print(f"The winner is {input_name} with a bid of {max}")
