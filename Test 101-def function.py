def add (x,y):
    sum = (5 + 3)
    return sum
print(add)

def add (x,y):
    sum = (x+y)
    return sum
print(add(5,3))

def minus (x,y):
    sum = (x-y)
    return sum
print(minus(5,3))

def multiply (x,y):
    sum = (x*y)
    return sum
print(multiply(5,3))

def divided (x,y):
    sum = (x/y)
    return sum
print(divided(9,3))

def function_a():
    return 25

def function_b():
    answer = 2 * function_a()
    return answer

number = function_a() + function_b()
print(number)


for counter in range (1,4):
    print(counter)
print("Go!")

red_team = ["Sue", "Anna", "Emily", "Simar"]

print("The Red Team members are:")
for player in red_team:
    print(player)

def count_letter_e(word):
    total_letter_e = 0

    for letter in word:
        if letter == "e":
            total_letter_e = total_letter_e + 1
    return total_letter_e

    

user_name = input("Enter your name: ")
total_es_in_name = count_letter_e(user_name)

print("There are " + str(total_es_in_name) + " E's in your name")


name = input("What is your name? ")

print("Hello " + name)



mylist = [1,2,3,4]
mylist.append(5)
print(mylist)


