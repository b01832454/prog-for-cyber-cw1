#user menu asking for input
while True:
    user_input = input("Please input an option 1 - 4: ")
    #first tool (security event counter) has 10 attempts to enter passwords, storing how many attempts it takes and outputting
    if user_input == "1":
        print("Security event counter")
        correct_pass = "admin" #accepted password
        correct = 0 #variable to store correct attempts
        fail = 0 #variable to store failed attempts
        total_attempts = 0 #variable to store total attempts
        while total_attempts < 10: #allows up to 10 attempts
            password = input("Please enter a password to begin: ")
            if password == correct_pass:
                correct += 1
                total_attempts += 1
            else:
                fail += 1
                total_attempts += 1
                if fail >= 5:
                    print("You have failed to enter the correct password more that 50%!!")
        print(f"You have had {correct} attempts successful") #displays how many attempts were correct
        print(f"You have had {fail} attempts failed") #displays how many attempts were failed
#second tool asking user to input a password, correct password being "Cybersecurity". If failed 5 times, exits loop
    elif user_input == "2":
        print("Brute Force Simulation")
        max_attempts = 0 #variable for max attempts 
        correct_pass = "Cybersecurity" #correct password to succeed
        while max_attempts < 5: #five attempts before breaking out of loop
            user_input = input("Please enter a password to begin: ")
            if user_input == correct_pass:
                print("Password is correct! ")
                break
            else:
                print("Please try again!!")
                max_attempts += 1
        print("You have guessed incorrectly for the maximum amount, please try again later.")
#third tool authenticating logins, correct username "admin" and password "student", allows 3 attemps
    elif user_input == "3":
        print("Login Authenticator")
        username = "admin" #correct username
        password = "student" #correct password 
        attempts = 0 #variable for max attempts
        while attempts < 3: #loops 3 times, if failed more than 3 times, breaks loop
            username_input = input("Please input your username: ")
            password_input = input("Please input your password: ")
            if username_input == username and password_input == password:
                print("You have successfully logged in! ")
            else:
                print("The username and password you have entered is not correct, please try again")
                attempts += 1
        print("You have incorrectly entered the password 3 or more times, the account has been frozen for 24 hrs.")

#option for user to exit tool
    elif user_input == "4":
        print("Thank you for using the security tool, now exiting...")
        break

#if option 1-4 isnt user alerts user of options
    else:
        print("Please select option 1 - 4")