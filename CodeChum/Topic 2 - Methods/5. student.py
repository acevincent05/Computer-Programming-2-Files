class Student:
    def __init__(self):
        self.id_number = 0
        self.name = ""
        self.course = ""
        
    def __str__(self) -> str:
        return f'{self.id_number} - {self.name} - {self.course}'
        
    def validate_info(self) -> None:
        if type(self.id_number) is int and len(str(self.id_number)) == 9 and self.name.replace(" ", "").isalpha():
            print('Student information is valid.')
        else:
            print('Student information is not valid.')