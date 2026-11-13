def validate_ip():
    #user input for ip address
    ip_address = input("Please enter an IP Address: ")
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
                break
            if int(select) < 0 and int(select) > 255:
                print("Your IP address is not in the correct format, please try again.")
                break

        #if all checks are complete print out that IP address is valid and restart the loop
        print("Your IP Address is correct!!")
        return True

