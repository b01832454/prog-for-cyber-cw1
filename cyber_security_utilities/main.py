#imports security_tools.py to main
import security_tools

#asks user for inputs
password = input("Please enter a password: ")
ip_address = input("Please enter an IP Address: ")

#calls the fuctions from the security tools module
check_pass = security_tools.validate_password(password)
check_ip = security_tools.validate_ip(ip_address)
