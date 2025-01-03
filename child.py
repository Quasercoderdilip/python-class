#Inheritance : 

class teacher:
    def __init__(self,no,name,reg):
        self.no = no;
        self.name = name;
        self.reg_no = reg;
    def display(self):
        print(f'Name of teacher - {self.no} = {self.name}.');
        print(f'Register_no of teacher - {self.no} = {self.reg_no}.');

class student(teacher):
    def __init__(self,no,name,reg,id):
        super().__init__(no,name,reg)
        self.id = id;
    def display(self):
        print(f'No : {self.no}.')
        print(f'Name of student : {self.name}.')
        print(f'Id of student : {self.id}.');


std_1 = student(1,'dk',1234,12);
std_1.display();