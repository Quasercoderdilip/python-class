#Inheritance : 

class teacher:
    def __init__(self,no,name,reg,class_in,section):
        self.no = no;
        self.name = name;
        self.reg_no = reg;
        self.class_in = class_in;
        self.section = section;
    def display(self):
        print(f'Name of teacher - {self.no} = {self.name}.');
        print(f'Register_no of teacher - {self.no} = {self.reg_no}.');

class student(teacher):
    def __init__(self,no,name,reg,class_in,section,id):
        super().__init__(no,name,reg,class_in,section)
        self.id = id;
    def display(self):
        print(f'No : {self.no}.')
        print(f'Name of student : {self.name}.')
        print(f'Id of student : {self.id}.');
        print(f'class of student : {self.class_in}.');
        print(f'section of student : {self.section}.');


std_1 = student(1,'Dilip kumar','nil','5th','C',12077);
std_1.display();


std_2 = student(2,'Manoj','nil','5th','C',12078);
std_2.display();

std_3 = student(3,'Surya','nil','5th','C',12079);
std_3.display();

std_4 = student(4,'Harpik khan','nil','5th','C',12080);
std_4.display();

std_5 = student(5,'Ashok nilavan','nil','5th','C',12081);
std_5.display();