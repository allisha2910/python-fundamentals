#activity 1 : create a program which asks a user for thier name, age, and favourite colour
                #print these in a sentence using an f string.

name = input("Type your name here:> ")
print(f"What's your name? {name}")
age = int(input("Type your age here:> "))
print(f"What's your age? {age}")
favourite_colour = input("Type your favourite colour here:> ")
print(f"What's your favourite colour? {favourite_colour}")
print(f"{name} is {age} years old, and thier favourite colour is {favourite_colour}")

#activity 2: create a program which accepts 2 inputs from a user (num 1 and num 2)
#            use these imputs for each operator, (+ - * ** / %), print equation and output

print("Type in two numbers")
num1 = int(input( "Number 1:  >  "))
num2 = int(input( "Number 2:  >  "))
print(f"{num1} x {num2} = {num1*num2}")
print(f"{num1} + {num2} = {num1+num2}")
print(f"{num1} - {num2} = {num1-num2}")
print(f"{num1} / {num2} = {num1/num2}")
print(f"{num1} is divisible by {num2} = {num1%num2}")
print(f"{num1} to the power of {num2} = {num1**num2}")

#Activity 3: A shop sells apples for 25p per apple, and bananas for 50p per banana.
#           create a program which asks a user how many apples they want to buy? 
#           and how many bananas they want to buy.
#           Display the total cost of apples, and the total cost of bananas and the
#           cost combined.

print("How many apples do you want to buy?")
Apples = int(input("Enter amount: "))
Apples_price = (0.25)
print(f"Total cost of Apples = {Apples*Apples_price}")
print("How many bananas do you want to buy?")
Bananas = int(input("Enter amount: "))
Bananas_price = (0.50)
print(f"Total cost of bananas = {Bananas*Bananas_price}")
print(f"Total cost of apples and bananas = {Apples*Apples_price+Bananas*Bananas_price}")

#answers

my_name = input("What is your name?").capitalize()
age = int(input("What is your age?"))
favourite_colour = input("What is your favourite colour?").lower()
print(f"Hello my name is {my_name}, I am {age} years old. My favourite colour is {favourite_colour}.")

num1 = int(input("Type in a first number: "))
num2 = int(input("Type in a second number: "))
add_result = num1+num2print(f"{num1} + {num2} = {add_result}")
print(f"{num1} + {num2} = {num1+num2}")
print(f"{num1} - {num2} = {num1-num2}")
print(f"{num1} * {num2} = {num1*num2}")
print(f"{num1} ** {num2} = {num1**num2}")
print(f"{num1} / {num2} = {num1/num2}")
print(f"{num1} % {num2} = {num1%num2}")

apple_cost = 25
apple_amount = int(input("How many apples would you like to buy?"))
apple_total = apple_cost * apple_amountbanana_cost = 50
banana_amount = int(input("How many bananas would you like to buy?"))
banana_total = banana_cost * banana_amounttotal = 
apple_total + banana_totalprint(f"You bought {apple_amount} apples")
print(f"You bought {banana_amount} bananas")
print(f"Your total is {total}p")
print(f"Your total is £{total/100:.2f}") 
