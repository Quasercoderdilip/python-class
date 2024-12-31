#lets build low level calculator : 

operator = str(input('Enter an operator(+ , - , * , /) : '));
num_1 = int(input('Enter a num_1 : '));
num_2 = int(input('Enter a num_2 : '));

calculater(operator, num_1, num_2);

def calculater(operator, num_1, num_2):
    if operator == '+' :
        result = (num_1 + num_2);
        print(result);
        return result ; 
    elif operator == '-' :
        result = (num_1 - num_2);
        print(result);
        return result ;
    elif operator == '*' :
        result = (num_1 * num_2);
        print(result);
        return result ;
    elif operator == '/' :
        result = (num_1 / num_2);
        print(result);
        return result ;
    else:
        print('Invaild input');