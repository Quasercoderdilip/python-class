try:
    a = int(input());
    b = (input());
    print(a / b);
    #print(d);

except ValueError as V :
    print('ValueError',V);
except TypeError as T :
    print('TypeError',T);
except NameError as N :
    print('NameError',N);




