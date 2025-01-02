#classes and objects :

class tour:
    drink ='';
    def party(self):#self keyword is must.
        print('lets party....');
    def beach(self):
        print('Enjoy the beach');

don = tour();

don.party();
don.beach();

class person:
    name = '';
    age = '';
    address = '';

ramesh = person();

ramesh.name = 'Ramesh';
ramesh.age = 23;
ramesh.address = 'chennai';

print(ramesh.name,ramesh.age,ramesh.address);