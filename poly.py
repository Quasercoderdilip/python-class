#polymorphism : 

class dad:
    def action(self):#pubilc function.
        print('He is a left hand user.');
    
    def __private(self):
        print('this is a private function.');

class first_son(dad):
    def Music(self):
        print('singing beautifully');




son_1 = first_son();
son_1.action();
son_1.Music();
# son_1._dad__private();#we can access private methods like this but it is not recommended.