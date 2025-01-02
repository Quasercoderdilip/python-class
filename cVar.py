#class variables types :

#instance variables types :

#Instance variables are variables that are specific to each object 
# (or instance) of a class.
#  They hold data that is unique to that particular instance.

class head:
    def __init__(self,width,height,weight):
        self.width = width;#these are the instance variables.
        self.height = height;#these are the instance variables.
        self.weight = weight;#these are the instance variables.
    def display(self):
        print(f'width is "{self.width}" , height is "{self.height}" , weight is "{self.weight}"');


goat = head('5px','10px','12kg');
goat.display();
print();


#class variables types : 

#Class variables are variables that are shared across all instances of a class. 
# They are defined at the class level and are not specific to any particular object (or instance). 
# Class variables maintain a single copy of their value, 
# and any change to a class variable affects all instances of the class.


class mobile:
    chargerType = 'C - USB port type';#these are the class variables.
    def __init__(self,model,color):
        self.model = model;#these are the instance variables.
        self.color = color;#these are the instance variables.
        
    def display(self):
        print(f'model is "{self.model}" , color is "{self.color}" , chargerType is "{self.chargerType}"');


iphone = mobile('max Pro','white');
iphone.display();
samsung = mobile('samsung','Red');
samsung.display();
micro = mobile('Micro-Max','Black');
micro.display();