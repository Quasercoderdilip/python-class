#1:

# class shape:
#     def area(self):
#         return 0;

# class rectangle(shape):
#     def area(self,length = 0, width = 0):
#         self.length = length;
#         self.width = width;
#         shape_area  = self.length * self.width;
#         return shape_area;

# squid = rectangle();

# print(squid.area(60,120));
        

#2:

# class person:
#     def __init__(self,name):
#         self.name = name;

# class student(person):
#     def __init__(self,name,grade):
#         super().__init__(name)
#         self.grade = grade
#     def display(self):
#         print(f'Name is {self.name} and Grade is {self.grade}');


# rajesh = student('Rajesh','A');

# rajesh.display();



#3:

# class vehicle:
#     def start(self):
#         print('Vehicle started');

# class car(vehicle):
#     def start(self):
#         print('Car started');

# v = vehicle();
# c = car();

# v.start();
# c.start();



#4:

# class Employee:
#     def __init__(self,name = 'someone',salary = 0):
#         self.name = name;
#         self.salary = salary;

# class Manager(Employee):
#     def __init__(self, name = 'Rajesh', salary = 0, department = 'IT'):
#         super().__init__(name,salary)
#         self.department = department;
#     def display(self):
#         print(f'Name is {self.name} and Salary is {self.salary} and Department is {self.department}.');

# m = Manager('siva',35000,'IOT');

# m.display();