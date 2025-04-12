import mysql.connector
from mysql.connector import errorcode
import os


class Pre_Enrollees_DB:
    def __init__(self, user: str, password: str, host: str, database: str):
        self.user = user
        self.password = password
        self.host = host
        self.database = database

    @property
    def get_user(self):
        return self.user
    
    @get_user.setter
    def set_user(self, user):
        self.user = user

    @property
    def get_password(self):
        return self.password

    @get_password.setter
    def set_password(self, password):
        self.password = password
    
    @property
    def get_host(self):
        return self.host
    
    @get_host.setter
    def set_host(self, host):
        self.host = host

    @property
    def get_database(self):
        return self.database
    
    @get_database.setter
    def set_database(self, database):
        self.database = database

    def connect(self):
        try:
            con = mysql.connector.connect(user=self.user, 
                                        password=self.password, 
                                        host=self.host, 
                                        database=self.database)
            print('Connection successful')
            return con
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def add(self, student_ID, name, age, shs_strand, program):
        try:
            connected = self.connect()
            cursor = connected.cursor()

            add_query = "INSERT INTO new_students (ID, name, age, shs_strand, chosen_program) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(add_query, (student_ID, name, int(age), shs_strand, program))

            connected.commit()
            print('Data saved.')

        except mysql.connector.Error as err:
            print(f'Error: {err}')

        finally:
            if connected.is_connected():
                cursor.close()
                connected.close()

    def display_all_enrollees(self):
        try:
            connection = self.connect()
            cursor = connection.cursor()

            query = "SELECT * FROM new_students"
            cursor.execute(query)

            # Fetch all rows at once
            rows = cursor.fetchall()

            print(f"{'ID':<10} | {'Name':<15} | {'Age':<5} | {'Strand':<10} | {'Program':<6}")
            print("-" * 60)

            # Loop through each row
            for row in rows:
                print(f"{row[0]:<10} | {row[1]:<15} | {row[2]:<5} | {row[3]:<10} | {row[4]:<6}") #prints each rows 

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def update_student(self, student_ID, name, age, shs_strand, program):
        try:
            connected = self.connect()
            cursor = connected.cursor()

            update_query = """
            UPDATE new_students
            SET name = %s, age = %s, shs_strand = %s, chosen_program = %s
            WHERE ID = %s
            """

            cursor.execute(update_query, (name, age, shs_strand, program, student_ID))
            
            connected.commit()
            print('Data updated.')

        except mysql.connector.Error as err:
            print(f'Error: {err}')

        finally:
            if connected.is_connected():
                cursor.close()
                connected.close()

def get_student_info():
    student_ID = input('Enter ID: ')
    name = input('Enter name: ')
    age = input('Enter age: ')
    shs_strand = input('Enter strand: ')
    program = input('Enter program: ')
    return student_ID, name, age, shs_strand, program

SQL_Pre_Enrollees_DB = Pre_Enrollees_DB('root', 'CS2025EU', 'localhost', 'Pre_Enrollees')

def main():
    while True:
        print("\n=== EARLY ENROLLMENT REGISTRATION ===")
        print("1. View Enrollee Records")
        print("2. Add Enrollee Records")
        print("3. Update Enrollee Records")
        print("4. Delete Enrollee Records")
        print("0. Exit Program")

        choice = input("Enter your choice: ")

        if choice == '1':
            os.system('cls')

            SQL_Pre_Enrollees_DB.display_all_enrollees()

        elif choice == '2':
            os.system('cls')

            student_ID, name, age, shs_strand, program = get_student_info()
            SQL_Pre_Enrollees_DB.add(student_ID, name, age, shs_strand, program)
        
        elif choice == '3':
            os.system('cls')

            student_ID, name, age, shs_strand, program = get_student_info()
            SQL_Pre_Enrollees_DB.update_student(student_ID, name, age, shs_strand, program)

        elif choice == '4':
            os.system('cls')

        elif choice == '0':
            print("Exiting program")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()