
def convertTopounds(weigh):
    pounds = weigh * 2.20462;
    print('pounds : ' + str(pounds));

def convertTokgs(weigh):
    kgs = weigh / 2.20462;
    print('kgs : ' + str(kgs));

weight = float(input('Enter your weight : '));
weight_type = str (input('Enter your type of weight(kg/pound) :'));

if weight > 0 and isinstance(weight,(int,float)) :
    if weight_type == 'pound':
        convertTopounds(weight);
    elif weight_type == 'kg':
        convertTokgs(weight);
    else:
        print('Invalid input, follow the instructions above');
        weight = float(input('Enter your weight : '));
        weight_type = str (input('Enter your type of weight(kg/pound) :'));
        if weight_type == 'pound':
            convertTopounds(weight);
        elif weight_type == 'kg':
            convertTokgs(weight);
        else:
            print('Invalid input, last chance to try...');
            weight = float(input('Enter your weight : '));
            weight_type = str (input('Enter your type of weight(kg/pound) :'));
            if weight_type == 'pound':
                convertTopounds(weight);
            elif weight_type == 'kg':
                convertTokgs(weight);
            else:
                print('Invalid input, final chance is over bye bye...');
else :
    print('Invalid weight');
