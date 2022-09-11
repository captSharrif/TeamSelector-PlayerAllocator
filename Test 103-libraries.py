# 1. IMPORT
# import time

# offset = time.timezone 
# print("Your offset in hours from \ UTC time is: ", offset)

# # 2. from IMPORT
# from random import randint 

# dice_roll = randint(1,6)
# print("Your threw a", dice_roll)

# # 3. from IMPORT as
# from webbrowser import open as show_me 

# url = input("enter a URl: ")
# show_me(url)

team2 = players[len(players)//2:]
print("\nTeam 2 captain: " + random.choice(team2))
print("Team 2:")
for player in team2:
    print(player)

players = ["Martin", "Craig", "Sue",
            "Claire", "Dave", "Alice",
            "Sonakshi", "Harry", "Jack",
            "Rose", "Lexi", "Maria",
            "Thomas", "James", "William",
            "Ada", "Grace", "Jean",
            "Marissa", "Alan"]