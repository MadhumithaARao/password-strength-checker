import re

def check_strength(password):
    score=0
    message=[]

    if len(password)>=8:
        score+=1
    else:
        message.append("Add atleast 8 characters.")

    if re.search("[A-Z]",password):
        score+=1
    else:
        message.append("Add an uppercase letter")
    
    if re.search("[a-z]",password):
        score+=1
    else:
        message.append("Add a lowercase letter")

    if re.search("[0-9]",password):
        score+=1
    else:
        message.append("Add a number")
    
    if re.search("[!@#$%^&*]",password):
        score+=1
    else:
        message.append("Add a special character")

    
    if score<=2:
        strength="Weak"
    elif score<=4:
        strength="Medium"
    else:
        strength="Strong"
    
    return strength, message

password=input("Enter password:")
strength, message=check_strength(password)
print("Password Strength:",strength)
if message:
    print("Suggestions:")
    for tip in message:
        print('-',tip)