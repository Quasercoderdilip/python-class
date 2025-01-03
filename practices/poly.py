#polymorphism : 

# class dad:
#     def action(self, a = 0, b = 0, c = 0, d = 0):#pubilc function.
#         print(f'result : {a+b+c+d}');
    
#     def __private(self):
#         print('this is a private function.');

# class first_son(dad):
#     def Music(self):
#         print('singing beautifully');




# son_1 = first_son();
# son_1.action(2,1);#polymorphism
# son_1.action(2,1,3);#polymorphism
# son_1.action(2,1,3,4);#polymorphism
# son_1.Music();
# son_1._dad__private();#we can access private methods like this but it is not recommended.


#1:

class Animal:
    def sound(self):
        print('Animal makes a sound.');

class Dog(Animal):
    def sound(self):
        # super().sound();
        print('Dog barks.');

class Bird(Animal):
    def sound(self):
        # super().sound();
        print('Bird sings.');


bai = Bird();
bai.sound();
