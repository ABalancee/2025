#Exercise 1 : Hello World
print('Hello wolrd')
print('Hello wolrd')
print('Hello wolrd')
print('Hello wolrd')

#Exercise 2 : Some Math
print((99**3) * 8)

#Exercise 3 : What Is The Output ?
#Predict the output of the following code snippets:
print(5 < 3) # False
print(3 == 3) # True
print(3 == "3") # False
print("3" > 3) # Error 
print("Hello" == "hello") # False

#Exercise 4 : Your Computer Brand
computer_brand = "Samsung"
print("I have a", computer_brand, "computer")

#Exercise 5 : Your Information
name = "Anania"
age = 34
shoe_size = 47  
info = "My name is " + name + ", I am " + str(age) + " years old and my shoe size is " + str(shoe_size) + "."
print(info)

#Exercise 6 : A & B
a = 999
b = 212
if a > b:
    print("Hello World")

#Exercise 7 : Odd Or Even
number = int(input("10: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

#Exercise 8 : What’s Your Name ?
my_name  = "Anania"

user_name = input("Anania") 

if user_name == my_name:
    print("WOW, we both have the same name ^^ " + my_name)
else:  
    print("Cool name, my name is " + user_name + ", nice to meet you !")

#Exercise 9 : Tall Enough To Ride A Roller Coaster
height = int(input("Enter your height in cm: "))
if height >= 191:
    print("You are tall enough to ride the roller coaster!")
else:
    print("You are big, need to grow taller to ride the roller coaster.")

#Exercise 1: Hello World- I Love Python
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("I love python")
print("I love python")
print("I love python")
print("I love python")

#Exercise 2 : What Is THe Season ? 
month = int(input(3))
if month == 3 or month == 4 or month == 5:
    print("spring")
    
if month == 6 or month == 7 or month == 8:
    print("Summer")
    
if month == 9 or month == 10 or month == 11:
    print("Autumn")

if month == 12 or month == 1 or month == 2:
    print("Winter")

#EXERCISE XP NINJA
#Exercise 1 : Use The Terminal

print(3 <= 3 < 9) # True
print(3 == 3 ==3) # True
print(bool(0)) # False
print(bool(5 == "5")) # False
print(bool(4 == 4) == bool("4")) # False
print(bool(bool(None))) # False

x = (1 == True) # True
y = (1 == False) # False
a = True + 4 
b = False + 10

print("x is", x)    
print("y is", y)
print("a:", a)
print("b:", b)

#Exercise 4 : How Many Characters In A Sentence ?

my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print(len(my_text))

#Exercise 5 : Longest Word Without A Specific Character

longest_sentence = ""

while True:
    user_sentence = input("beeep beep buup buup")
    if "a" in user_sentence.lower():
        print("Damn there is an 'a' in your sentence, try again")
    else:
        if len(user_sentence) > len(longest_sentence):
            longest_sentence = user_sentence
            print("New record ! THIS IS the longest sentence without an 'a' is now:", longest_sentence)
            