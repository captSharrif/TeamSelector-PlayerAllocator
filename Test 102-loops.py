# for counter in range(1,4):
#     print(counter)

# print("Go!")


# groupname = ["Sue", "Anna", "Emily", "Simar"]

# print("The Red Team members are: ")
# for player in groupname:
#     print(player)



# answer = input("Should I keep going? (y/n)")
# while answer == "y":
#     answer = input("Should I keep going? (y/n)")

# while True:
#     print("There's no stopping me now!")


# answer = input("launch another spacerocket? (y/n)")
# while answer == "y":
#     for count in range (10, 0, -1):
#         print(count)
#     print("LIFT OFF")

#     answer = input("Launch another spacerocket? (y/n)")

# sensor_readings = [3, 5, 4, -1, 6, 7]
# total = 0

# for sensor_reading in sensor_readings:
#     if sensor_reading < 0:
#         break
#     total = total + sensor_reading



# print("total is: " +str(total))




readings = [3, 5, 4, -1, 6, 7]
total = 0

for reading in readings:
    
    if reading < 0:
        continue

    total = total + reading



print("total is: " +str(total))




teams1 = [
        ["Red Team", "Adam", "Anjali", "Colin", "Anne"], 
        
    ]

teams2 = [
        ["Blue Team", "Greg", "Sophie", "June", "Sara"], 
    ]

def list_teams(x,y):
    for team in x:
        for name in team:
            print(name)
        print("\n")

    for team in y:
        for name in team:
            print(name)
        print("\n")


# list_teams(teams2,teams1)






