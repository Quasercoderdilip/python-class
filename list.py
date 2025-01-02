from collections import OrderedDict

# fruits = ['apple','orange','banana','pineapple','guova'];

# print(fruits);

# for fruit in fruits:
#     print(fruit);

setfruits = {'apple','orange','banana','pineapple','guova'};

print(type(setfruits));

my_list = list(OrderedDict.fromkeys(setfruits));
print(my_list);

my_list[3] = 'hoiii hoiii';
print(my_list);

setfruits = OrderedDict.fromkeys(my_list);
#print(setfruits.keys());
print(setfruits);

