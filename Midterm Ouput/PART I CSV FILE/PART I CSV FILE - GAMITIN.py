import csv
from csv import DictWriter

data = [
    {'Name': 'Nicole', 'Program': 'BSCS', 'Department': 'CCMS', 'Year': '1'},
    {'Name': 'Jade', 'Program': 'BSCE', 'Department': 'CEng', 'Year': '2'},
    {'Name': 'Chesca', 'Program': 'BS Psych ', 'Department': 'CAS', 'Year': '1'},
    {'Name': 'Jake', 'Program': 'BSBA ', 'Department': 'CBA', 'Year': '3'},
]

field_names = ['Name', 'Program', 'Department', 'Year']

with open('student_info.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(data)

def delete():
    updatedlist=[]
    with open("student_info.csv",newline="") as csvfile:
      reader=csv.reader(csvfile)
      username=input("Enter the username of the user you wish to remove from file:")
      
      for row in reader:
        if row[0]!=username: 
            updatedlist.append(row) 
      updatefile(updatedlist)
        
def updatefile(updatedlist):
    with open("student_info.csv","w",newline="") as csvfile:
        Writer=csv.writer(csvfile)
        Writer.writerows(updatedlist)
        print("File has been updated")

def add():
    name = input('Enter Name: ')
    program = input('Enter Program: ')
    dept = input('Enter Department ')
    year = input('Enter Year: ')

    new_data = {'Name': name, 'Program': program, 'Department': dept, 'Year': year}
    
    with open("student_info.csv","a",newline="") as csvfile:
        dictwriter_object = DictWriter(csvfile, fieldnames=field_names)
        dictwriter_object.writerow(new_data)
        print("File has been updated")
         
def search():
    search_name = input('Search name: ')
    print()
    with open("student_info.csv",newline="") as csvfile:
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

def view():
    with open('student_info.csv', mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames = field_names)

        print()
        print('='*53)    
        for row in reader:
            print(f"{row['Name']:<15} {row['Program']:<15} {row['Department']:<15} {row['Year']:<5}")
        print('='*53)    
        print()

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

while True:
    choice = menu()

    if choice == 1:
        view()
    elif choice == 2: 
        add()
    elif choice == 3:
        search()
    elif choice == 4:
        delete()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice, try again.")



