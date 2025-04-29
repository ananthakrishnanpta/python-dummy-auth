import authentication as at
import tools as t

def mainMenu():
  t.clear()
  choices = """
  1. Login
  2. Register
  0. Exit
  """
  choice = input(choices)
  try:
    choice = int(choice)
  except:
    print("Wrong input")
    return mainMenu()

  match choice:
    case 1:
      at.loginPage()
    case 2:
      at.registerPage()
    case 0:
      return "exit"
    case _:
      print("Your input does't match any given choices.")
      return mainMenu()

while True:
    x = mainMenu()
    if x == 'exit':
      t.quit()
      break
