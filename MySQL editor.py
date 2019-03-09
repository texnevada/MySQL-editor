#!/usr/bin/python3
"""
Program name: Tap06
Author: Christer G. Sorensen
Created: 06.03.19 - Europe
Made for: Python 3.6
"""

#python -m pip install mysql-connector
import mysql.connector
import getpass

import os
#New function that clears the command line terminal
def clear():
    #do cls if os name is NT/Windows else do clear which is used on Linux & mac
    os.system("cls" if os.name=="nt" else "clear")

print("MySQL Database login")
user = input("Username: ")
pswd = getpass.getpass("Password: ")
n = 0
try:
    # Connect to the database
    mydb = mysql.connector.connect(host="localhost", user=user, passwd=pswd,)
    n = +1
except:
    print("Could not connect to MySQL service")
selectdb = "none"
selecttable = "none"
if n == 1:
    clear()
    sql = mydb.cursor()
    q = 1
    while q == 1:
        print(f"You are logged in as {user}")
        print(f"Selected db: {selectdb}\nSelected table: {selecttable}\n")
        print("Choose between the following.")
        print("1. Create a Database.")
        print("2. Create table (You must select a database first!)")
        print("3. Select Database")
        print("4. Select a table")
        print("You must have selected a table first before selecting the following.\n")
        print("5. Display all data on all Databases & Tables")
        print("6. insert to table")
        print("7. edit a table.")
        print("8. Delete a table.")
        print("Use \"q\" to exit the program\n")
        i = input("[1-7]: ")
        #Create database
        if i == "1":
            clear()
            print(f"You are logged in as {user}")
            print("What is the name of the database you wish to make?")
            newdb = input("Name: ")
            try:
                sql.execute(f"CREATE DATABASE {newdb}")
                clear()
                print(f"You have successfully made a new database named: {newdb}\n")
            except:
                print("Error: Could not create a new database\n")
        #Create table. Database must be selected
        elif i == "2":
            clear()
            print("Creating a new table")
            createtable = input("Table name: ")
            print("\nInput the values of the table")
            print("Example: name VARCHAR(255), address VARCHAR(255)\n")
            tablevalues = input("Values: ")
            sql.execute(f"CREATE TABLE {createtable} ({tablevalues})")
            clear()
            sql.execute("SHOW TABLES")
            print(f"You created [{createtable}] table with values:\n{tablevalues}\n")
        #Select database
        elif i == "3":
            clear()
            print("Select database")
            selectdb = input("db name: ")
            clear()
            sql.execute(f"USE {selectdb}")
            print(f"{selectdb} is selected\n")
        #Select table
        elif i == "4":
            clear()
            print("Select db table")
            selecttable = input("Table name: ")
            sql.execute(f"SELECT * FROM {selecttable}")
            clear()
            print(f"{selecttable} table is selected\n")
        #Display all data
        elif i == "5":
            try:
                clear()
                tableresult = sql.fetchall()
                for x in tableresult:
                    print(str(x))
                print()
            except:
                print("Error: No database or table selected\nPlease select a table & database\n")
        #Insert to table
        elif i == "6":
            if selecttable != "none":
                clear()
                print(f"Inserting into\nDatabase: {selectdb}\nTable: {selecttable}\n")
                print("Insert table columns and seperate with comma\nExample: games, year, time")
                inserttable = input("Column: ")
                print("Insert values in the order of the columns. Seperate with comma\nExample: Chess, 1942, 15:00")
                inserttablev = input("Value: ")
                try:
                    sql.execute(f"INSERT INTO {selecttable} ({inserttable}) VALUES ({inserttablev})")
                    print(f"{sql.rowcount} record inserted\n")
                except:
                    print("Unable to insert data\n")
            else:
                print("You need to select a database!\n")
        #Delete table
        elif i == "7":
            if selecttable != "none"
                print(f"Are you sure you want to delete {selecttable}?")
                print("Default input: N unless specified")
                deletetable = input("[y/n]: ")
                if deletetable == "y" or "yes" or "Y" or "Yes":
                    sql.execute(f"DROP TABLE {selecttable}")
            else:
                print("You must select a table!")
        #exit program
        elif i == "q" or "quit" or "Q" or "Quit":
            mydb.close()
            q = -1
