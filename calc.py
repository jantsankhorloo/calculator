def calc(a, b, c):
    while True:
        try:
            if b == '+':
                return a+c
            elif b == '-':
                return a-c
            elif b == '*':
                return a*c
            elif b == '/':
                return a/c
            else:
                return 'Invalid operation'
        except:
            return 'Invalid input!'
 
        
        
