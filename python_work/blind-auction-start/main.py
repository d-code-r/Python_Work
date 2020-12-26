from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art
print(art.logo)

name_list = []
nu_list = []

start = True
while start:
    name = input("what's your name ")
    bid = int(input("enter your bid "))

    my_dict = {}
    my_dict[name] = bid
    clear
    for i in my_dict:
        name_list.append(i)
        nu_list.append(my_dict[i])
        clear()
    more_bid = input("Any one want to bid? type yes or no ").lower()
    if more_bid == "yes":
        start = True

    elif more_bid == "no":
        start = False
    else:
        print("Enter valid choice yes or no")

winner = name_list[nu_list.index(max(nu_list))]
print(f"the winner is {winner} and the bid is {max(nu_list)}$")


# winner = max(my_dict, key=my_dict.get)
# print(f"The winner is {winner}")


""" 
k = list(my_dict.keys())
v = list(my_dict.values())
print(k[v])
"""
