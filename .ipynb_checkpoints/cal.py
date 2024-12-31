#lets build low level calculator : 

def calculater(operator, num_1, num_2):
    if operator == '+' :
        result = round(num_1 + num_2);
        print(result);
        return result ; 
    elif operator == '-' :
        result = round(num_1 - num_2);
        print(result);
        return result ;
    elif operator == '*' :
        result = round(num_1 * num_2);
        print(result);
        return result ;
    elif operator == '/' :
        result = round(num_1 / num_2);
        print(result);
        return result ;
    else:
        print('Invaild input');


operator = str(input('Enter an operator(+ , - , * , /) : '));
num_1 = float(input('Enter a num_1 : '));
num_2 = float(input('Enter a num_2 : '));

calculater(operator, num_1, num_2);