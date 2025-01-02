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


class Fruit():
    def __init__(self):
        self.color = '';
    def display(self):
        print(self.color);

apple = Fruit('red');


apple.display();