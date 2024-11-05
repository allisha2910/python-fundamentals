#if statement includes a conditional
# = assignment operator
#"string" = (variable)

#example 1

# music = "no music"

# print(music)

# print(music == "classical")

# music = input("What music would you like?").lower
# if music == "classical":
#     print("Oh no, not Classical again!")
# elif music == "no music":
#     print("Alexa, play some music!")
# else:
#     print("I've not heard this before!")

    # indentation is important in python
    #else if
    #provided conditions 

    #comparison operators
        # == equal to
        # != not equal to
        # < less thean
        # <= less than or equal to 
        # > more than
        # >= more than or equal to

# example 2

# reads from top to bottom 
# important to rearrange - the most specific thing should probably be first 

# music = "Oasis"

# if music == "Oasis":
#     print("The best!")
# elif music != "britpop":
#     print("i want to listen to brit pop")
# else:
#     print("yay! britpop!")

#activity 

# age = 20
# location = "uk"

# if age >= 18 and location == "uk":
#     print("Yes i can serve you.")
# else:
#     print("you are not old enough.")

# logical operator e.g AND

# place = "mcr"
# weather = "cloudy"

# if place == "mcr" and weather == "sunny":
#     print("check again")
# elif place == "mcr" and weather == "rain":
#     print("obvs")
# else:
#     print("what?, it isnt raining?")

    # true + false = false overall, need to get both true in order for it to be true 
    # two parts of inofrmation, you need your username AND password

#and if it has to be WITH something, its a pairing, one does not work without the other.
    #true and true =true 
    #true and false = false 
    #fasle and false = false

#using OR - if there is mulitple things for saying something 
    #true and true = true 
    #true and flase = true 
    #false and false = false 

#example of OR

# day = "Saturday"
# bank_holiday = True

# if day == "Saturday" or day == "Sunday" or bank_holiday == True:
#     print("A day off!")
# else:
#     print("Off to work I go")