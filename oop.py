#1

class shape:
    def area(self):
        return 0;

class rectangle(shape):
    def area(self,length = 0, width = 0):
        self.length = length;
        self.width = width;
        shape_area  = self.length * self.width;
        return shape_area;

squid = rectangle();

print(squid.area(60,120));
        