"""
This module saves a welcome message.
"""

import json

def welcome():
    message = "Welcome to Orquestra!"

    with open("welcome.json",'w') as f:
        f.write(json.dumps(message, indent=2)) # Write message to file as this will serve as output artifact