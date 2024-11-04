# print("this is my variables file") 04/11/2024

# print("All Around The World"[7].upper())
      
# Variables 

# = is an assignment operator 
# updating a variable by reassigning 
# numbers = intergers 
# word that python recognises e.g. false = boolean 
# snake case - underscores and lowercase. for variables and functions.
# + symbol to join 2 things together - concatination - only strings not numbers

#user input - the information the user gives us, information being input. 

#input allows us to write a prompt to the user, need to make a variable to hold the response  
#whatever you put in the input will always be a string (including numbers)

#arithmatic operators (mathemeatic symbols) = + / * % - modulo, to see if a number is divisible

#casting 

# for example print(1+7)    print(3*2)  print(3**3) - to the power of 

#casting will help you find the mean and the median, it will enable you to work with it properly

#save you time in the cleaning process 

#turning it into the right data type

#variables.

# my_name = "Allisha"

# my_age = 24

# favourite_drink = "Hot chocolate"

# # f string (most readable, and one single string)

# print(f"{my_name} is {my_age} years old, and thier favourite drink is {favourite_drink}")

# # using .format

# print("{} is {} years old, and thier favourite drink is {}".format(my_name, my_age, favourite_drink))

# print(my_name + "is" + my_age + "their favourite drink is" + favourite_drink)

# print(my_name, "'s favourite drink is" + favourite_drink)

# print(my_name, "'s favourite drink is", favourite_drink)

# print("My favourite drink is", favourite_drink)

# print(favourite_drink)

# print(my_name)

#Input code 

# user_name = input("Type your name here:> ")

# print(f"Hello, {user_name}")

# print(type(user_name))

#casting example... this will not work because it was told to multiply string not numbers ...

#you have to CHANGE THE DATA TYPE... which is called casting.

# print("Type in two numbers to multiply them")

# num1 = input( "Number 1:  >  ")
# num2 = input( "Number 2:  >  ")

# print(num1*num2)

# ------------ casting: putting interger infront to go from string to integer ------

# print("Type in two numbers to multiply them")

# num1 = int(input( "Number 1:  >  "))
# num2 = int(input( "Number 2:  >  "))

# print(num1*num2)

#bank example 

Balance =int(input("100"))
amount_to_withdraw =int(input("20"))
print(Balance)
Balance= balance - amount_to_withdraw
print(Balance)