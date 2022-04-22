history = []
operator = input("Please enter the sign of the oprator = ")

while (operator == "/" or operator == "*" or operator == "+" or operator == "-" or operator == "history") :
    
    if (operator == "/" or operator == "*" or operator == "+" or operator == "-"):
        num01 = int(input("Plese enter frist number = "))
        num02 = int(input("Plese enter second number = "))
        result = 0
    
        if operator == "/" :
            result = num01 / num02
        elif operator == "*" :
            result = num01 * num02
        elif operator == "+" :
            result = num01 + num02
        elif operator == "-" :
            result = num01 - num02
            
        Display = (f'{num01} {operator} {num02} = {result}') 
        
        print (f'{Display}')
        history.append(Display)
        operator = input("Please enter the sign of the oprator = ")
    
        pass
    
    elif operator == "history" :
        print(history)
        break
        
    elif operator == "x" :
        print(history)
        break