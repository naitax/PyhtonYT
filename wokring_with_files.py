#employees.txt
# Jim - Salesman
# Dwight - Salesman
# Pam - Receptionist
# Michael - Manager
# Oscar - Accountant


### reading files
#1. open txt file (absolute path/name file), store open file in variable
# a - append
# w-write
# r-read
# r+ - read and write
employee_file = open('employees.txt', 'r') #read from the file
print(employee_file.readable()) #boolean 
print(employee_file.read()) #display whole file
print(employee_file.readline()) #read first line (displays just one line)
print(employee_file.readlines()) #display each line from file in a form of a list
print(employee_file.readlines()[1]) #to access specific line in a list - enter index in []


for employee in employee_file.readlines():
    print(employee)
    
#Always close the file!
employee_file.close()

### writing to files
# a - append text to the end of the file
employee_file = open('employees.txt', 'a') #read from the file

employee_file.write('Toby - Human Resources')
employee_file.write('\nKelly - customer service')

employee_file = open('employees.txt', 'w') #overwrite the entire file
employee_file.write('Kelly - customer service') # only Kelly in the file

employee_file = open('employees1.txt', 'w') #create a new file - employees1.txt

#Always close the file!
employee_file.close()
