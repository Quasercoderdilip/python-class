#Encapsulation : 

# class car:
#     def start_car(self):
#         print('Door open');
#         print('Enter into car and Started');
#         self._Accelerate();
    
#     def _Accelerate(self):
#         print('throttle increased');
#         self.__performing();
    
#     def __performing(self):
#         print('Burst inside');
#         print('Car is moving');

# car_1 = car();

# car_1.start_car();


class calci :
    def __init__(self, a = 0, b = 0):
        self.a = a;
        self.b = b;
        self.__Add_result();
    
    def __Add_result(self):
        print(f'Result is {self.__add()}');
    
    def __add(self):
        return self.a + self.b;

math = calci(4,4);





