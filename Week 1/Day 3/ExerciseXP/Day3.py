#Day3Exercises
#Given this list:
#list1 = [5, 10, 15, 20, 25, 50, 20]
#find the value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value

list1 = [5, 10, 15, 20, 25, 50, 20]
pos = list1.index(20)
print(pos)

list1[pos] = 200
print(list1)
#Exerciese DONE

#Exercise 2: Unpack the following tuple into 4 variables and print each variable:
a_tuple = (10, 20, 30, 40)

a, b, c, d = a_tuple
print(a)
print(b)        
print(c)
print(d)
#Exercise DONE

#Sets

# Example: working with sets
my_set = set()

my_set.add("Rick")
my_set.add("Morty")
my_set.add("Rick")   # duplicate, will be ignored

print(my_set)  
# Output: {"Rick", "Morty"}

this_set = {"banana", "apple", "cherry", "apple"}  
print(this_set)  
# Output: {"banana", "cherry", "apple"}  # no duplicates

#Exercise: Accept a number from the user and print its multiplication table

user_input = int(input("Enter a number: "))

for i in range(1, 11): 
    print(f"{user_input} * {i} = {user_input * i}")

#Exercise DONE

#Exercise 4: Loop 1 to 10

i = 1
while i <= 10:
    print(i)
    i += 1
#Exercise DONE

