#class method : 

#Class methods are methods that are bound to the class rather than an 
#  of the class. They can be used to access and modify class-level data 
# (such as class variables). Class methods are marked with the 
# @classmethod decorator and take the class itself as their first parameter, 
# conventionally named cls.


class pc:
    ram = 32;
    def __init__(self,cpu,proc,color):
        self.cpu = cpu;
        self.proc = proc;
        self.color = color;
    
    def display(self):
        print(f'CPU is {self.cpu}.');
        print(f'processor is {self.proc}.');
        print(f'color is {self.color}.');
        print(f'Ram is {self.ram}GB')
    
    @classmethod           #class method
    def changeRam(cls,new):
        cls.ram = new;
    
    @staticmethod
    def stat():
        print('this is static method');


soft = pc('i5','intel', 'black');
soft.display();
print();
soft.changeRam(90);
print();
soft.display();
soft.stat();