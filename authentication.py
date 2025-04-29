"""
This module will handle authentication
"""
import tools as t

import getpass
# user list
users = []

# this function takes information and returns a user dictionary object
def register(username, password):
  for user in users: # iterating through every dictionary in the users list
    if user['username'].lower() == username.lower(): # checking if any user dictionary has this username
      error = f"user_exists_already with this username...{username}"
      return error
  else: # when the username doesn't exist already
    user = {
        'username' : username,
        'password' : password
        }
    # print(user)
    users.append(user)
    return user

def registerPage():
  t.clear()
  print("Welcome to the registeration page ...")
  username = input("Enter username : ")
  password = getpass.getpass("Enter your password : ")
  confirm_password = getpass.getpass("Confirm password : ")
  if password == confirm_password:
    response = register(username, password)
    if isinstance(response, str):
      print(response)
      t.sleep(2)
      return None
    else:
      print(f"User registered successfully : {response['username']}")
      # mainMenu()
      loginPage()
  else:
    print("Passwords did not match...\nTry again!!!")
    t.sleep()
    registerPage()

def profile(user):
  t.clear()
  print(f"Welcome to your profile {user['username']}")
  choices = """
  0. Logout
  """
  choice = input(choices)
  try:
    choice = int(choice)
  except:
    print("Wrong input")
    return profile(user)
  match choice:
    case 0:
      print("Logging out...")
      return None
    case _:
      print("Wrong input")
      return profile(user)


# while True:
#   registerPage()
def loginPage():
  t.clear()
  print("Please sign in to continue...")
  user_in = input("Enter your username : ")
  pwd_in = getpass.getpass("Enter your password : ")
  for user in users:
    if user['username'] == user_in and user['password'] == pwd_in:
      print(f"Logging in...\n Welcome {user_in}...")
      return profile(user)
  print("Please check your credentials...")
  t.sleep(2)
  return None