# Working with the following string:
description = "strings are..."

#make it all uper case
print(description.upper())

#replace the word "are" to "is"
print(description.replace("are", "is"))

#print just the word "strings"
print(description[0:7])

#In the python shell, Create a variable called my_age, use python to know how old you will be in 123879 years
my_age = 123879 + 2025 -1990
print(my_age)

#Exercise
#Check what is the type of each value, then change it: if it is a string, make it an integer and vice-versa:
bank_balance = '33000'
phone_number = 532287514

print('bank_balance:', type(bank_balance))
print('phone_number:', type(phone_number))

#Umwandlung
bank_balance = int(bank_balance)
phone_number = str(phone_number)

print('bank_balance:', type(bank_balance))
print('phone_number:', type(phone_number))

#Exercise
#In the python shell, Create a variable called first_name and a variable called last_name, and then print your full name using those two variables

first_name = "Anania F."
last_name = "Yangala"
print(first_name + " " + last_name)

#Exercise
#Given the following values:
x = 5
y = 10
z = 0
word1 = "hello"
word2 = "world"

#1. Check if x is less than y and y is greater than z.
print(x < y and y > z)

#2. Check if word1 is not equal to word2.       

print(word1 != word2)

#3. Use the bool() funciton to check the boolean value of z and word1
print(bool(z))
print(bool(word1))