##Skills practiced: defining functions, dictionaries, input(), and return values.

def insert_username( name, age, email, phone):
    """ here im defining insert_username and storing name, age, email, phone """

    return {
        "name":name,
        "age":age,
        "email":email,
        "phone":phone

    }

##----Main Program-----------

users=[] ##im creating a empty list

print("Enter user details. Type 'q' at name prompt to quit.\n")

while True:
   name = input("what is your name? or (type q to quit) :")
   if name.lower()=='q':
      break
   age=input("what is your age?")
   email=input("enter you email id :")
   phone=input("phone numer :")
   
   record=insert_username( name, age, email, phone) ##inster the details in insert_username
   users.append(record)
   print("✔ User added!\n")
   
   print("\nAll users inserted:") # After loop, show all users
   for i, u in enumerate(users, start=1):
      print(f"{i}. {u}")


