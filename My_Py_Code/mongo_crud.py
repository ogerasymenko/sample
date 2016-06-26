'''
Program to make CRUD operations with mongodb
'''

__author__ = 'sashko'

from pymongo import MongoClient

client = MongoClient('localhost:27017')
# creating connection to mongodb
db = client.EmployeeData


def insert():
    '''function to insert data into mongo'''
    try:
        employeeId = input('Enter Employee id: ')
        employeeName = input('Enter Name: ')
        employeeAge = input('Enter age: ')
        employeeCountry = input('Enter Country: ')

        db.Employees.insert_one({
            "id": employeeId,
            "name": employeeName,
            "age": employeeAge,
            "country": employeeCountry
        })
        print('Data inserted successfully\n')

    except Exception as e:
        print(str(e))


def read():
    '''function to read data from mongo'''
    try:
        empCol = db.Employees.find()
        print('All data from EmployeeData Database: ')

        for emp in empCol:
            print(emp)
        print()

    except Exception as e:
        print(str(e))


def update():
    '''function to update record to mongo'''
    try:
        criteria = input('Enter id to update: ')
        name = input('Enter name to update: ')
        age = input('Enter age to update: ')
        country = input('Enter country to update: ')

        db.Employees.update_one({
            "id": criteria}, {
            "$set": {
                "name": name,
                "age": age,
                "country": country}
            })
        print('Records updated successfully\n')

    except Exception as e:
        print(str(e))


def delete():
    '''function to delete record from mongo'''
    try:
        criteria = input('Enter employee id to delete: ')
        db.Employees.delete_many({"id": criteria})
        print('Deletion successful\n')

    except Exception as e:
        print(str(e))


def menu():
    '''generate menu list'''
    while True:
        selection = input('Select:\n1 to insert\n2 to update\n3 to read\n4 to delete\n5 to exit: ')

        if selection == '1':
            insert()
        elif selection == '2':
            update()
        elif selection == '3':
            read()
        elif selection == '4':
            delete()
        elif selection == '5':
            return
        else:
            print('\nINVALID SELECTION \n')
            return

menu()
