def calc(a, b, c):
    while True:
        try:
            if b=='+':
                return a+c
            elif b == '-':
                return a-c
            elif b == '*':
                return a*c
            elif b == '/':
                return a/c
                break
        except:
            return 'Well, shit!'
            
    
 
        
        
