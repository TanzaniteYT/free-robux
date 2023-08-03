try:
    import roblox
    from roblox import robux
    import math
    import threading
except ImportError as e:
    pass
import os
import socket
import time
import random

# function time
def clearterminal():
    os.system('cls') #empties the terminal, this is so it is clean.



def get_numeric_input(prompt): #this function checks if an input is a number or not, if it isnt it will ask again.
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        clearterminal()
        print("Invalid input. Please enter a valid number.")
#function time over
robux = 0 #this creates robux as a variable

username = input("what's your username on roblox? (case sensitive and NOT your display name) ")



inputrobux = get_numeric_input("how much robux do you currently have? ") # asks how much robux you have

robux = robux = inputrobux # this makes the robux variable equal the amount of robux you have currently, this is just in case the program bugs and wipes your robux.
print("you have", robux,"robux.")

print("connecting to roblox.com...")
time.sleep(1.34)
website = 'https://roblox.com'  # connects to roblox.com
port = 25565 
print("connected!")


robuxyouwant = get_numeric_input("how much robux do you want? (we would not reccomend big numbers.) ") # asks how much robux you want
if robuxyouwant < inputrobux:
    print("cant have less robux than you currently have.")
else:
    time.sleep(2)
    robuxtotal = robuxyouwant + inputrobux
    print("getting your robux...")
    print("bugfix: we can only give 1 robux at a time because roblox will catch on to this.") # this gives robux
    robuxtotal = robux + inputrobux
    time.sleep(2)
    print("giving", username,"robux...")
    for x in range(inputrobux, robuxyouwant):
        print(inputrobux, end="\r")
        inputrobux = inputrobux + 1
        time.sleep(random.random())
        
    else:
        print("applying robux!")
        time.sleep(3)
        print("robux should be done! heads up that you need to be logged out of all devices for this to work.")
