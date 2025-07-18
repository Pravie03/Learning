####Ask the user for two numbers, add them, and print the total.

number_1 = input("Enter number 1:")
number_2 = input("Enter number 2:")
total = int(number_1) + int(number_2)

print("Total:",total)

###Ask for a word, print its length and uppercase version.

word = input("Enter a word:")

print("Length of the word:",len(word))
print("converting to uppercase",word.upper())

###Take a string, turn it into a number, add 5, print the result.

##reusing number_1 here

Addition = int(number_1) + 5
print("Added value:",Addition)