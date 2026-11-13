#imports random library
import random

#password validator, checks length, upper, lower and digits. suggests password if user does not meet criteria
def validate_password(password):
#password must be greater or equal to 10 characters
    if len(password) >= 10:
        count_upper = 0 #variable to count upper chars
        count_lower = 0 #variable to count lower chars
        count_digit = 0 #variable to count digits

        for char in password: #loops the input and adds 1 to each variable if meets criteria
            if char.isupper():
                count_upper += 1
            elif char.islower():
                count_lower += 1
            elif char.isdigit():
                count_digit += 1
        if count_upper >= 1 and count_digit >= 1 and count_lower >= 1: #if input is correct displays message
            print("Password is accepted.. ")
            return True
        else:
            print("Please try a stronger password...") #if criteria isnt met, displays message and suggests strong pass
            generate_password()
            return False
    else:
        print("Please create a password longer than 10 characters..") #if criteria isnt met, displays message and suggests strong pass
        generate_password()
        return False

#ip address checker, will display results if user inputs address incorrect, outputs if address is a valid format
def validate_ip(ip_address):
    while True:
        #loops round checking if each part meets the correct criteria
        parts = ip_address.split(".")
        #check if ip address contains any dots
        if "." not in ip_address:
            print("Your IP address is not in the correct format, please try again.")
            return False
        #checks if ip address has 3 dots included
        if ip_address.count(".") != 3:
            print("Your IP address is not in the correct format, please try again.")
            return False
        #checks if the ip address contains 4 parts
        if len(parts) != 4:
            print("Your IP address is not in the correct format, please try again.")
            return False
        #checks via a loop if the parts are digits and if the parts are in the range 0-255 for binary
        for select in parts:
            if not select.isdigit():
                print("Your IP address is not in the correct format, please try again.")
                return False
            if int(select) < 0 and int(select) > 255:
                print("Your IP address is not in the correct format, please try again.")
                return False

        #if all checks are complete print out that IP address is valid and restart the loop
        print("Your IP Address is correct!!")
        return True


def generate_password():
    pass_length = random.randint(10,16) #gives a password length between 10 and 16
    password = "" #variable to allow password to be stored
    valid_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@!£$%&" #list of allowed characters to select from
    for chars in range(pass_length): #loops round valid characters generating randomly a password between 10-16
        password += random.choice(valid_chars)
    print(f"Here is a randomly generated strong password {password}") #prints said password

