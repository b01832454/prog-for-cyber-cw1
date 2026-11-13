#imports libraries that we will use in the program below
import random
from datetime import datetime
import socket

#allows us to get an ip address when attempting login
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip_address = s.getsockname()[0]

#credentials that are valid
correct_username = "jordan"
correct_password = "student"

#allows us to give a random event id from random library
event_id = random.randint(1000, 9999)
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
s.close()

#loop to allow the user to input credentials, outputting if it has failed or successful
while True:
    username_input = input("Please enter a username: ")
    password_input = input("Please enter a password: ")
    if username_input == correct_username and password_input == correct_password:
        print(f"Event ID: {event_id}")
        print(f"Username: {username_input}")
        print(f"IP Address: {ip_address}")
        print("Event: Successful login")
        print(f"Timestamp: {timestamp}")
    else:
        print(f"Event ID: {event_id}")
        print(f"Username: {username_input}")
        print(f"IP Address: {ip_address}")
        print("Event: Failed login")
        print(f"Timestamp: {timestamp}")
