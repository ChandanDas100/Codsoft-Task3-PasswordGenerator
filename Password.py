
import string
import random

# Getting password length
length = int(input("Enter password length: "))

print('''Select character set for password from these : 
        1. Digits
        2. Letters
        3. Special characters
        4. Exit''')

characterList = ""
while(True):
    choice = int(input("Pick a number "))
    if(choice == 1):
        
        characterList += string.ascii_letters
    elif(choice == 2):
        
        
        characterList += string.digits
    elif(choice == 3):
        
         # characters
        characterList += string.punctuation
    elif(choice == 4):
        break
    else:
        print("Please pick a valid option!")

password = []

for i in range(length):

     
    # character list
    randomchar = random.choice(characterList)
    
    
    password.append(randomchar)

# printing  the password as a string
print("The random password is " + "".join(password))
