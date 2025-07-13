age = 30
name = "Praveen"
price = 19.99
is_student = True


#Testing type

# print(type(age))
# print(type(name))
# print(type(price))
# print(type(is_student))

##Testing print()

# print(name)
# print("Hello!!!!", name ,"Your Age is", age)

##Testing input(prompt)

# username=input("what is your name?")
# print("your name is :",username)       ##Even if the user types 25, input() gives you "25" (a string). 


## To convert it into int

user_age=input("what is your age :")
age_converted=int(user_age)

print("Your age is :",age_converted) ## we can write like this or below

print(f"Your age is : {age_converted}")

