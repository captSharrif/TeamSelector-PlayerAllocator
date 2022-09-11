import random



players = ["Martin", "Craig", "Sue",
            "Claire", "Dave", "Alice",
            "Sonakshi", "Harry", "Jack",
            "Rose", "Lexi", "Maria",
            "Thomas", "James", "William",
            "Ada", "Grace", "Jean",
            "Marissa", "Alan",
            "Jed", "Art", "Ladjid", "Sharrif", "Tahseen",
            "Abdullah.M", "Suliman", "Yasser", "Yazeed", "Toqueer"]

# print("Welcome to Team Allocator")

# while True:
#     random.shuffle(players)
    
#     team1 = players[:len(players)//3]
#     print("Team 1 captain: " + random.choice(team1))

#     print("Team 1:")
#     for player in team1:
#         print(player)

#     team2 = players[len(players)//3: (len(players)//3)*2]
#     print("\nTeam 2 captain: " + random.choice(team2))
#     print("Team 2:")
#     for player in team2:
#         print(player)
    
#     team3 = players[(len(players)//3)*2:]
#     print("\nTeam 3 captain: " + random.choice(team3))
#     print("Team 3:")
#     for player in team3:
#         print(player)

#     response = input("Pick team again? Type y or n: ")
#     if response == "n":
#         break

print("Welcome to Team / Player Allocator")

while True:
    random.shuffle(players)
    response = input("\nIt is a team or individual sport? \
                \ntype team or individual:")
    
    if response == "team":
        team1 = players[:len(players)//2]
        team2 = players[len(players)//2:]

        print("\nteam1:")

        for player in team1:
            print(player)

        print("\nteam2:")

        for player in team2:
            print(player)

    
    else: 
        print("\n")
        for i in range (0, 20, 2):
            print(players[i] + " vs " + players[i+1])
        
        
        # start = random.randrange (i, i+2)
        # # print(players[start] + " start")

        

    