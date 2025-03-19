import csv
from csv import DictWriter

class Student_Info():
    def __init__(self, student_info: str, field_names: list):
        self.student_info = student_info
        self.field_names = field_names

    @property
    def get_student_info(self):
        return self.student_info
    
    @get_student_info.setter
    def set_student_info(self, info):
        self.student_info = info

    @property
    def get_field_names(self):
        return self.field_names
    
    @get_field_names.setter
    def set_field_names(self, field):
        self.field_names = field

    def view(self):
        with open(self.student_info, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames = field_names)

            print()
            print('='*53)    
            for row in reader:
                print(f"{row['Name']:<15} {row['Program']:<15} {row['Department']:<15} {row['Year']:<5}")
            print('='*53)    
            print()

    def add(self, name: str, program: str, dept: str, year: str):

        new_data = {'Name': name, 'Program': program, 'Department': dept, 'Year': year}
        
        with open(self.student_info,"a",newline="") as csvfile:
            dictwriter_object = DictWriter(csvfile, fieldnames=field_names)
            dictwriter_object.writerow(new_data)
            print("File has been updated")

    def search(self, search_name: str):
        print()
        with open(self.set_student_info, newline="") as csvfile:
            reader = csv.DictReader(csvfile, fieldnames = field_names)

            exist = False
            print()
            print('='*53) 
            print(f"{'Name':<15} {'Program':<15} {'Department':<15} {'Year':<5}")
            for row in reader: 
                if row['Name']==search_name: 
                    print(f"{row['Name']:<15} {row['Program']:<15} {row['Department']:<15} {row['Year']:<5}")
                    exist = True
            print('='*53) 
            print()

            if not exist:
                print("Student not found.")

    def delete(self, username):
    #1. This code snippet asks the user for a username and deletes the user's record from file.
        updatedlist=[]
        with open("student_info.csv",newline="") as csvfile:
            reader=csv.reader(csvfile)
            
            for row in reader: #for every row in the file
                if row[0]!=username: #as long as the username is not in the row .......
                    updatedlist.append(row) #add each row, line by line, into a list called 'udpatedlist'

        with open("student_info.csv","w",newline="") as csvfile:
            Writer=csv.writer(csvfile)
            Writer.writerows(updatedlist)
            print("File has been updated")

def menu():
    strs = ('1. View\n'
            '2. Add\n'
            '3. Search\n'
            '4. Delete\n'
            '5. Exit\n'
            'Enter option: ')
    choice = input(strs)
    return int(choice)


__name__ == "__main__"

print()
print('='*35)
print("STUDENTS' BASIC INFO - MSEUF LUCENA")
print('='*35)
print()

field_names = ['Name', 'Program', 'Department', 'Year']

try:
    with open('student_info.csv', 'r', newline='') as csvfile:
        pass
except:
    with open('student_info.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()

student_info_manager = Student_Info('student_info.csv', field_names)

while True:
    choice = menu()

    if choice == 1:
        student_info_manager.view()
        
    elif choice == 2: 
        name = input('Enter Name: ')
        program = input('Enter Program: ')
        dept = input('Enter Department: ')
        year = input('Enter Year: ')

        student_info_manager.add(name, program, dept, year)
        
    elif choice == 3:
        search_name = input('Search name: ')

        student_info_manager.search(search_name)

    elif choice == 4:
        username=input("Enter the username of the user you wish to remove from file: ")

        student_info_manager.delete(username)

    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice, try again.")



