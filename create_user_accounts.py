import csv
import sys
from pyad import *

# Connect to the Active Directory
pyad.set_defaults(ldap_server="ldap://active-directory-server")

# Read the CSV file containing user information
with open("users.csv", "r") as file:
    reader = csv.reader(file)
    next(reader) # Skip the header row
    for row in reader:
        username = row[0]
        first_name = row[1]
        last_name = row[2]
        email = row[3]
        
        # Use the information to create a new user account
        user = pyad.User.create(username, ou="ou=users,dc=example,dc=com")
        user.update_attribute("givenName", first_name)
        user.update_attribute("sn", last_name)
        user.update_attribute("mail", email)
