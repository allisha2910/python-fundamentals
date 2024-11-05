#activity 1: create a variable called password
            #check how many letters are in the password
            #if there are fewer than 8 print that the password is too short
            #otherwise print the password.

# password = input(" Type your password here :> ")

# if len(password) <8:
#     print("password is too short")

# else:
#     print(password)

#activity 2: create a variable called num. if num is divisible by 3 print "fizz" if its divisible by 7 print "buzz" if its divisible by both 3 and 7 print "fizzbuzz". otherwise print num

# num = 21  

# if num % 3 == 0 and num % 7 == 0:
#     print("fizzbuzz")
# elif num % 3 == 0:
#     print("fizz")
# elif num % 7 == 0:
#     print("buzz")
# else:
#     print(num)


# activity 3: correct the code on the following slide so it functions as expected.
#             can you use anything to make sure 'London' and 'london' are accepted as correct answers.

# print("What is the capital of England?")

# answer = input("Type your answer here>>")

# if answer == "London" or answer == "london":
#     print(f"corect! The answer is {answer}")

# else:
#     print(f"Incorrect, the answer is 'London', not {answer}")

#activity 4: create a variable called word that takes a string
#            create an if statement that checks if the last letter is the same as the first.
#            if the return is true, otherwise return false.

# word = input("Type your word here>")

# if word[0] == word[-1]:
#     print("true")
# else:
#     print("false")

#activity 4: create a variable called word that takes a string
            #create an if statement that checks if the whole strong is a palindrome

# word = input("Type your word here>")

# if word == word [::-1]:
#     print("true")

# else:
#     print("false")