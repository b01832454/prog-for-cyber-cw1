#dictionary storing the elements
security_incidents = {"username": "Jordan", "ip" : "8.8.8.8", "event type" : "failed login", "risk level" : "high"}

#prints the username and ip address in the dictionary
print(security_incidents["username"], security_incidents["ip"])

#adds a new key "status" with value "open" and prints
security_incidents["status"] = "open"
print(security_incidents["status"])

#updates the risk level to low and prints it
security_incidents["risk level"] = "low"
print(security_incidents["risk level"])

#deletes an item in the dictionary "event type" and prints all remaining keys and values
del security_incidents["event type"]
print(security_incidents)

#outputs total keys and values
print("Keys: ", len(security_incidents.keys()), "Values: ", len(security_incidents.values()))