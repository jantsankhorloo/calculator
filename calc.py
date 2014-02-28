def gcd(a, c):
    while (c != 0):
        r = a%c
        a = c
        c = r
    return a

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
                return float(a)/c
            elif b == '**':
                return a**float(c)
            elif b == '%':
                return (float(c)/a)*100
            elif b == 'root':
                return a**(1.0/c) 
            elif b == 'gcd':
                return gcd(a, c)                                      
            else:
                return 'Invalid operation'
        except:
            return 'Please, check your inputs!'
 
        
        
