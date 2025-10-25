#import for reguler expression
import re
#import for hashing
import hashlib
#Import for datetime
from datetime import datetime 

#Function to hash the password
def hash_password(password):
  return hashlib.sha256(password.encode()).hexdigest()

#Password Checker
def Strong_password(password):
  if len(password) < 8:
    return False, "You must have at least 8 characters"

  if not re.search(r'[A-Z]', password):
    return False, "You must have at least one uppercase letter"

  if not re.search(r'[0-9]', password):
    return False, "You must have at least one number"

  if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
    return False, "You must have at least one special symbol"
    
  return True, "Your password is strong enough"

#login events function

def log_event(event):
  timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  with open("log.txt", "a") as log_file:
    log_file.write(f"[{timestamp}] {event}\n")

#Registration function

def register_user():
  username = input("Enter your username:")
  password = input("Enter your password:")

  is_Valid, Feedback = Strong_password(password)
  if not is_Valid:
    print("Password is not strong enough")
    print(Feedback)
    log_event(f"registreation failed for {username}")
    return
    
#hash the password
  hashed_password = hash_password(password)

  with open("register.txt", "a") as file:
    file.write(f"{username}:{hashed_password}\n")
  print("Registration successful")
  log_event(f"{username} Successfully registered")

#Login function

def login_user():
  username = input("Enter your username:")
  password = input("Enter your password:")

  with open("register.txt", "r") as file:
    register = file.readlines()

  for user in register:
    stored_username, stored_password = user.strip().split(":")
    if username == stored_username and hash_password(password) == stored_password:
      print("login successful")
      log_event(f"{username} Successfully logged in")
      post_login_menu(username)   
      return


  print("Invalid username or password")
  log_event(f"login failed for {username}")

# Function to display post login menu
def post_login_menu(username):
  while True:
    print("\n Post login menu")
    print("1-View log")
    print("2-Logout")
    choice = input("Enter your choice: ")
    
    if choice == "1":
      view_log(username)
    elif choice == "2":
      log_event(f"user '{username}' logged out")
      print("Logging out...")
      break
    else:
      print("Invalid choice. Please choose a valid option.")
  
# To view the log file

def view_log(username):
  print(f"\n log for user '{username}':")
  with open("log.txt","r") as log_file:
    logs = log_file.readlines()

  user_logs = [log.strip() for log in logs if username in log]

  if user_logs:
    for log in user_logs:
      print(log)
  else:
    print("No logs found in this account")
  
      

# Main function
def main():
  while True:
    print("welcome to the user registration system")
    print("1.Register")
    print("2.Login")
    print("3.Exit")

    choice = input("Enter your choice:")

    if choice == "1":
      register_user()

    elif choice == "2":
      login_user()

    elif choice == "3":
      log_event("Exiting the system")
      print("Exiting ...")
      break
    else:
      print("please select a valid option")


main()
