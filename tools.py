import os 
import time 

def clear():
    # this will pass the 'cls' command to the power shell session running the program
    os.system('cls')

def sleep(seconds = 2):
    # this makes the interpreter 'sleep' for given seconds
    time.sleep(seconds)

def quit():
    clear()
    print("bye byee...")
    sleep(3)
    os.system('exit')
