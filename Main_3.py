"""
name = input ("Enter your name: ")
nickname = input ("Enter your nickname: ")
color = input ("Enter favorite color: ")
print (name, "--", nickname, "--", color)

user_num1 = input ("Enter a number: ")
user_num2 = input ("Enter another number: ")
print (user_num1 + user_num2) # concatenation
num1 = int(user_num1)
num2 = int(user_num2)
print (num1+num2)
"""
""""
num1 = int(input("Enter a number"))
num2 = int(input("Enter another number"))
print (num1+num2)
"""
"""
answer = input ("Do you like Ice? Y/N ")

if answer == "Y" or answer =="y":
    print ("Great! ")
else:
    print ("Oh ddd")

print("TNX")
"""
"""
number = int(input("Enter a number: "))
if number < 0:
    print ("U entered a negative num")
elif number == 0:
    print ("U enterd 0 ")
else:
    print ("this is a positive num")

print ("TNX for playing")
"""
current_number = 1
max_print_num = 10
while current_number <= max_print_num:
    print (current_number)
    current_number +=1
print ("end")
