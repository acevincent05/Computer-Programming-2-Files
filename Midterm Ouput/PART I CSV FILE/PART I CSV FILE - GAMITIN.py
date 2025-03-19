import csv
from csv import DictWriter #Read and writes data of the CSV using dictionaries

#Implementation of OOP with Encapsulation and Composition
class Student_Info():
    def __init__(self, student_info: str, field_names: list): #CSV file name and headers 
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

    #Shows the contents of the CSV file
    def view(self):
        with open(self.student_info, mode='r', newline='') as csvfile: #accesses the CSV file
            reader = csv.DictReader(csvfile, fieldnames = field_names) #accesses the CSV file as a dictionary with its header

            next(reader, None) #Skips reading the header

            if any(reader): #checks if CSV file has contents excluding the header
                csvfile.seek(0)  # Go back to the start of the file
                reader = csv.DictReader(csvfile, fieldnames = field_names) #Reinitialize the reader to access it again in dictionary form
                print()
                print('='*53)
                for row in reader:
                    print(f"{row['Name']:<15} {row['Program']:<15} {row['Department']:<15} {row['Year']:<5}") #prints each rows 
                print('='*53)    
                print()
            else:
                print('The file has not content.')

    #Allows the user to add contents in the CSV file
    def add(self, name: str, program: str, dept: str, year: str):

        new_data = {'Name': name, 'Program': program, 'Department': dept, 'Year': year} #Organizes inputted data in a dictionary form based on the header
        
        with open(self.student_info,"a",newline="") as csvfile:
            dictwriter_object = DictWriter(csvfile, fieldnames=field_names)
            dictwriter_object.writerow(new_data) #adds the new data from user input
            print("File has been updated")

    #Verifies the user's input if it exists in the CSV file
    def verify_search(self, verify_name):
        with open(self.set_student_info, newline="") as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=field_names)

            for row in reader:  #checks all rows
                if row['Name'] == verify_name:  #if the name is found
                    return {
                        'Name': row['Name'], 
                        'Program': row['Program'], 
                        'Department': row['Department'], 
                        'Year': row['Year']
                    } #brings back the verified dictionary

            # If the student doesn't exist
            return False

    #Allows the user to search the info of a student by typing the name
    def search(self, search_name: str):

        verified = self.verify_search(search_name) #Implemented Method Composition to verify the existence of the inputted name and info in the CSV file
        
        if verified:  #if the input exists
            print()
            print('=' * 53) 
            print(f"{'Name':<15} {'Program':<15} {'Department':<15} {'Year':<5}") # displays the header 
            print(f"{verified['Name']:<15} {verified['Program']:<15} {verified['Department']:<15} {verified['Year']:<5}") #displays the searched student info
            print('=' * 53) 
            print()
        else:
            print('Student not found.')

    #Allows the user to delete a student info 
    def delete(self, username):
        verified = self.verify_search(username) #Implemented Method Composition to delete of the inputted name and info in the CSV file

        if verified: #if the input exists
            with open(self.student_info, "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile, fieldnames=field_names)
                
                # puts all items except for the user's input in another list 
                updatedlist = [item for item in reader if item != verified]

            # writes the updated list back to the file
            with open(self.student_info, "w", newline="") as csvfile:
                dictwriter_object = DictWriter(csvfile, fieldnames=field_names)
                dictwriter_object.writerows(updatedlist)  
            print("Student record deleted successfully.")
        else:
            print("Student not found.")

#For Display the Menu Options
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

#The header of the CSV file
field_names = ['Name', 'Program', 'Department', 'Year']

#Handling the file error 
try: #Checks if the CSV is already created 
    with open('student_info.csv', 'r', newline='') as csvfile:
        pass
except: #Creates a new CSV file if not yet created
    with open('student_info.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()

#Puts the CSV file name and header to the Student_Info class
student_info_manager = Student_Info('student_info.csv', field_names)

#User menu navigation
while True:
    choice = menu()

    if choice == 1:
        student_info_manager.view() #calls the view method
        
    elif choice == 2: 
        name = input('Enter Name: ')
        program = input('Enter Program: ')
        dept = input('Enter Department: ')
        year = input('Enter Year: ')

        student_info_manager.add(name, program, dept, year) #calls the add method and gives the user input
        
    elif choice == 3:
        search_name = input('Search Student name: ')

        student_info_manager.search(search_name) #calls the search method and gives the name to be search

    elif choice == 4:
        username=input("Enter the name you wish to delete: ")

        student_info_manager.delete(username) #calls the delete method and gives the name of the student that will be deleted

    elif choice == 5: 
        print("Exiting...") 
        break #Exits the program
    else:
        print("Invalid choice, try again.")
