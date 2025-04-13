import mysql.connector
from mysql.connector import errorcode
import os

# class for Pre_Enrollees_DB CRUD with the implementation of Encapsulation and Composition
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

    # connect to MySQL
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

    # calls the connect method and cursor 
    def connection_cursor(self):
        connected = self.connect()
        cursor = connected.cursor()
        return connected, cursor

    # adds enrollees data
    def add(self, student_ID, name, age, shs_strand, program):
        try:
            connection, cursor = self.connection_cursor() # connects the SQL while also calling in the cursor

            add_query = "INSERT INTO new_students (ID, name, age, shs_strand, chosen_program) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(add_query, (student_ID, name, int(age), shs_strand, program))

            connection.commit()
            print('Enrollee data saved.')

        except mysql.connector.Error as err:
            print(f'Error: {err}') # displays the error from the SQL database

        finally: # logs out the SQL once functions are done wether it has an error or not 
            if connection.is_connected():
                cursor.close()
                connection.close()

    # displays all the enrollee data
    def display_all_enrollees(self):
        try:
            connection, cursor = self.connection_cursor()

            query = "SELECT * FROM new_students"
            cursor.execute(query)

            # retrieves all rows
            rows = cursor.fetchall()

            print(f"{'ID':<10} | {'Name':<15} | {'Age':<5} | {'Strand':<10} | {'Program':<6}") 
            print("-" * 60)

            # print each rows
            for row in rows:
                print(f"{row[0]:<10} | {row[1]:<15} | {row[2]:<5} | {row[3]:<10} | {row[4]:<6}")  

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    # updates the enrollee data
    def update_enrollee(self, student_ID, name, age, shs_strand, program):
        try:
            connection, cursor = self.connection_cursor()

            update_query = """
            UPDATE new_students
            SET name = %s, age = %i, shs_strand = %s, chosen_program = %s
            WHERE ID = %s
            """

            cursor.execute(update_query, (name, age, shs_strand, program, student_ID))
            
            connection.commit()
            print('Enrollee data updated.')

        except mysql.connector.Error as err:
            print(f'Error: {err}')

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    # delete enrollee data
    def delete_enrollee(self, student_ID):
        try:
            connection, cursor = self.connection_cursor()

            delete_query = "DELETE FROM new_students where ID = %s"

            cursor.execute(delete_query, (student_ID,))
            
            connection.commit()
            print('Enrollee data deleted.')

        except mysql.connector.Error as err:
            print(f'Error: {err}')

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

# getting the values for the sql headers
def get_student_info():
    student_ID = input('Enter ID: ')
    name = input('Enter name: ')
    age = input('Enter age: ')
    shs_strand = input('Enter strand: ')
    program = input('Enter program: ')
    return student_ID, name, age, shs_strand, program

# requiring the user to enter the credentials of the SQL database 
def DB_credentials():
    user = input('Enter user: ')
    password = input('Enter password: ')
    host = input('Enter host: ')
    db_select = input('Enter Database: ')

    # SQL_Pre_Enrollees_DB = Pre_Enrollees_DB('root', 'CS2025EU', 'localhost', 'Pre_Enrollees')
    global SQL_Pre_Enrollees_DB # to access SQL_Pre_Enrollees_DB in the menu
    SQL_Pre_Enrollees_DB = Pre_Enrollees_DB(user, password, host, db_select)

# the main menu
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
            SQL_Pre_Enrollees_DB.update_enrollee(student_ID, name, age, shs_strand, program)

        elif choice == '4':
            os.system('cls')

            student_ID = input('Enter ID: ')
            SQL_Pre_Enrollees_DB.delete_enrollee(student_ID)

        elif choice == '0':
            print("Exiting program")
            break
        else:
            print("Invalid choice. Please try again.")

# allows the program to run directly when opening
if __name__ == "__main__":
    DB_credentials()
    main()