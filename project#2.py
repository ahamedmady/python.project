# import Reguler Expressions module
import re

# import string module
import string

# import random module

import random

# Import SQLite Module
import sqlite3

# Create Database And Connect
db = sqlite3.connect("app.db")


# Setting Up The Cursor
cr = db.cursor()

def commit_and_close():
  
    # Save (Commit) Changes
    db.commit()

    # Close Database
    db.close()
    print("connection with Database is close")



s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)



caracter_number  = random.randrange(6,21)
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round(caracter_number*(30/100))
part2 = round(caracter_number*(20/100))

password = []

for caracter1 in range(part1):
    
      password.append(s1[caracter1])
      password.append(s2[caracter1])


for caracter2 in range(part2):
      
      password.append(s3[caracter2])
      password.append(s4[caracter2])

random.shuffle(password)

jioned = "".join(password[:])


     
def show_skills():
  """ this method showing the Data """

  password = input("Enter The password:")
  cr.execute(f"select * from skills where password = '{password}'")
  
  results = cr.fetchall() # Assign Data To Variable

  # print(f"the num of row is.{len(results)}")
  
  if len(results) > 0:
      print("showing the data :)") 

      for data in results:

        print(f"your name skill is:{data[0]}, and ",end=" ")
        print(f"your password is:{data[1]}")
        print(f"your email is:{data[2]}, and" ,end=" ")
        print(f"your password is:{data[3]}",f"and your dob is:{data[4]}")

  else:
     print("close App")

  commit_and_close()

def add_skill():
   """ this method adding the Data and chack if the new data is unique """ 
   trys = 5
              
   while trys > 0:
      name = input("put the name :").strip().capitalize()

      generat_password = input("do you want us to make you a strong password yes/no:").strip().capitalize()

      if generat_password == "Yes":
          
          password = jioned

      else:
          password = input("Enter The password:")
    
      cr.execute(f"select name from skills where password = '{password}' ")

      results = cr.fetchone()

      if results == None :
        
            Email = input("enter a email:").strip()
            phone_num = input("enter a phone number:").strip()
            dob = input("enter a Date:").strip()

            search_email = re.search("^[A-z0-9\]+@[A-Z0-9]+\.(\w+)$",Email)
            search_phone = re.search("^(\d{3}\s?)(\d{4}-?\s?)(\(?\d{4}\)?)$",phone_num)
            search_dob = re.search("^(\d)+/(\d)+/(\d{4})$",dob)

            if search_email and search_phone and search_dob:
                  
                  Data = (name, password, Email, phone_num, dob)
                  cr.execute(f"insert into skills (name, password, Email, phone_num, dob) values (?, ?, ?, ?, ?)", Data)
                  commit_and_close()

                  break

            
            else:
              
              print("the Data is not valid")

      else:
        
          print("you can not add it Because there is before")

          trys -= 1


def delete_skill():
  """ this method deleting the Data """ 

  name = input("put the name :").strip().capitalize()
  password = input("Enter The password:")

  cr.execute(f"delete from skills where name = '{name}' and password = '{password}' ")

  commit_and_close()

def update_skill():
  """ this method updating the Data """
  
  name = input("put the name :").strip().capitalize()
  password = input("Enter The password:")
  Email = input("put the new email:").strip()
  phone_num = input("enter a new phone number:").strip()
  dob = input("enter a new Date:").strip()
  
  search_email = re.search("^[A-z0-9\]+@[A-Z0-9]+\.(\w+)$",Email)
  search_phone = re.search("^(\d{3}\s?)(\d{4}-?\s?)(\(?\d{4}\)?)$",phone_num)
  search_dob = re.search("^(\d)+/(\d)+/(\d{4})$",dob)

  if search_email and search_phone and search_dob:
     
       
       cr.execute(f"update skills set (Email, phone_num, dob) = ('{Email}','{phone_num}', '{dob}')  where name = '{name}' and password = '{password}'")
       commit_and_close()
 
  else:

      print("close App")


def chack_password():

  """ this method chacking the password of user to know if he's in the systim or no  """

  password = input("Enter The password:")
  cr.execute(f"select * from skills where password = '{password}'")
  
  results = cr.fetchall() # Assign Data To Variable

  # print(f"the num of row is.{len(results)}")
  
  if len(results) > 0:

        # Input Big Message
        input_message = """
        What Do You Want To Do ?
        "s" => Show All Skills
        "a" => Add New Skill
        "d" => Delete A Skill
        "u" => Update Skill Progress
        "q" => Quit The App
        Choose Option:
        """


        # Input Option Choose
        user_input = input(input_message).strip().lower()

        # Command List
        commands_list = ["s", "a", "d", "u", "q"]


        # Check If Command Is Exists
        if user_input in commands_list:

          print(f"Command Found {user_input}")

          if user_input == "s":

            show_skills()

          elif user_input == "a":

            add_skill()

          elif user_input == "d":

            delete_skill()

          elif user_input == "u":

            update_skill()

          else:
            
            print("App is closed")
            commit_and_close()

        else:

          print(f"Sorry This Command \"{user_input}\" Is Not Found")

  else:
     
     print("sorry we can not find your Data!")

     create_acounte = input("do you want login yes/no:").strip().capitalize()

     if create_acounte == "Yes":
        
        add_skill()


     else:
      
       print("GOOD BY")


chack_password()