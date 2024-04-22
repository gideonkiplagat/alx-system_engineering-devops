#!/usr/bin/python3

"""
task #0, extend your Python script to export data in the CSV format.
"""

from requests import get
from sys import argv
import csv


if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos')
    data = response.json()
    
    row = []
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()

    for i in data2:
        if i['id'] == int(argv[1]):
            employee = i['username']
            print("employee", employee, sep=" ")
            break
            
    filename = argv[1] + '.csv'        
    with open(filename, quotechar='"', mode='w', newline='') as file:
        write = csv.writer(file, quoting=csv.QUOTE_ALL, lineterminator= '\n')

        for i in data:
            row = []
            if i['userId'] == int(argv[1]):
                row.append(i['userId'])
                row.append(employee)
                row.appendi['completed']
                row.append(i['title'])

                write.writerow(row)
