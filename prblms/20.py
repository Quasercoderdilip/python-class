# *Question: Check if Two Arrays Are Equal*


def check_Equal(x,y):

    if len(x) != len(y):
        return False
   
    for index in range(0,len(x)):
        if x[index] != y[index]:
            return False
           

    return True;

print(check_Equal(['Dilip', 'Sriram', 'Sairam'], ['Dilip', 'Sriram', 'Sairam']))