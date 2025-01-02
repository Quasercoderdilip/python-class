#constructor and self keyword : 

class oi:
    def __init__(self):
        self.name = '';  
        self.age = 0;
        self.gender = '';
    
    def display(self):
        print(f'Name = {self.name}');
        print(f'Age = {self.age}');
        print(f'Gender = {self.gender}');

hi = oi();

hi.name = 'dk';
hi.age = 23;
hi.gender = 'male';

hi.display();