
# Active Directory User Account Creation using Python

## Purpose

This code is used to automate the process of creating user accounts on an Active Directory. It takes information about users from a CSV file and uses it to create new user accounts in the Active Directory. This saves time compared to manually creating each account.

## Prerequisites

Before you can use this code, you will need:

-   A computer with Python installed
-   The `pyad` library installed on your computer. You can install it by running the following command in your terminal or command prompt: `pip install pyad`
-   A CSV file containing information about the users you want to create accounts for. The file should have a header row with the following columns: `username`, `first_name`, `last_name`, `email`.
-   Access to an Active Directory and the appropriate permissions to create user accounts in it.

## Running the Code

To run this code, you need to do the following steps:

-   Open your terminal or command prompt
-   Change the current directory to the location where you saved the code file
-   Run the following command: `python create_user_accounts.py`
-   The code will now connect to the Active Directory, read the CSV file, and create new user accounts for each row in the file.

## What the Code Does

The code does the following things:

-   Connects to the Active Directory using the `pyad` library
-   Reads the CSV file containing user information
-   For each row in the CSV file, the code creates a new user account in the Active Directory using the `pyad` library
-   The code sets the user's `first_name`, `last_name`, and `email` using the information from the CSV file

## Modifying the Active Directory or CSV File

If you need to change the Active Directory or the CSV file, you can do so by modifying the code. Here's how:

-   To change the Active Directory, you need to modify the following line of code: `pyad.set_defaults(ldap_server="ldap://active-directory-server")`. Replace `active-directory-server` with the hostname or IP address of your Active Directory.
-   To change the CSV file, you need to modify the following line of code: `with open("users.csv", "r") as file:`. Replace `users.csv` with the name of your CSV file. Make sure the header row of your CSV file has the columns `username`, `first_name`, `last_name`, `email`.

Sample data for the `users.csv` file:
```python
username,first_name,last_name,email
jane_doe,Jane,Doe,jane.doe@example.com
john_doe,John,Doe,john.doe@example.com
jim_smith,Jim,Smith,jim.smith@example.com
sarah_lee,Sarah,Lee,sarah.lee@example.com
```
