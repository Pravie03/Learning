##Skills practiced: defining functions, dictionaries, input(), and return values.

def insert_username( name, age, email, phone):
    """ here im defining insert_username and storing name, age, email, phone """

    user_record = {
        "name":name,
        "age":age,
        "email":email,
        "phone":phone

    }

    return user_record

##----Main Program-----------

##getting input from the user

name=input("what is your name?")
age=input("what is your age?")
email=input("enter you email id :")
phone=input("phone numer :")

##inster the details in insert_username

new_user=insert_username( name, age, email, phone)

print("user record inserted successfully")
print(new_user)



