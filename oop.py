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



