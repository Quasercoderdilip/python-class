#constructor and self keyword : 

# class oi:
#     def __init__(self):
#         self.name = '';  
#         self.age = 0;
#         self.gender = '';
    
#     def display(self):
#         print(f'Name = {self.name}');
#         print(f'Age = {self.age}');
#         print(f'Gender = {self.gender}');

# hi = oi();

# hi.name = 'dk';
# hi.age = 23;
# hi.gender = 'male';

# hi.display();


# class student:
#     def __init__(self):
#         self.Name = '';
#         self.Register_no = '';
#     def display(self):
#         print(f'Name of student = {self.Name}.');
#         print(f'Register.no of student = {self.Register_no}.');


# std_1 = student();
# std_1.Name = 'Dk';
# std_1.Register_no = '32056';

# std_1.display();


# class Fruit():
#     def __init__(self,color):
#         self.color = color;
#     def display(self):
#         print(self.color);

# apple = Fruit('red');


# apple.display();


# class employee:
#     def __init__(self, name, age, salary):
#         self.name = name;
#         self.age = age;
#         self.salary = salary;

#     def display(self):
#         print(f'his name is {self.name} and age is {self.age}, his salary is {self.salary}');



# emp = employee('dilip',23,35500);
# emp.display();


# class teacher:
#     def __init__(self,no,name,reg):
#         self.no = no;
#         self.name = name;
#         self.reg_no = reg;
#     def display(self):
#         print(f'Name of teacher - {self.no} = {self.name}.');
#         print(f'Register_no of teacher - {self.no} = {self.reg_no}.');


# t_1 = teacher(1,'Meera','120766');
# t_1.display();

# t_2 = teacher(2,'pooja','120767');
# t_2.display();


# class calci:
#     def __init__(self,a,b):
#         self.a = a;
#         self.b = b;

#     def add_display(self):
#         print(f'answer of add : {int(self.a + self.b)}');

#     def sub_display(self):
#         print(f'answer of sub : {int(self.a - self.b)}');

#     def mul_display(self):
#         print(f'answer of multiply : {int(self.a * self.b)}');

#     def div_display(self):
#         print(f'answer of division : {int(self.a / self.b)}');


# num_1 = calci(15,3);
# num_1.add_display();
# num_1.sub_display();
# num_1.mul_display();
# num_1.div_display();