def pchecker(N):
    if (N != 0) or (type(N) == "<type 'int'>"):
        i = 2
        while i < N:
            if N == 2:
                return 'prime'
            elif N == 1:
                return 'non-prime'
            elif N % i == 0:
                return 'non-prime'
            i = i + 1
        else:
            return 'prime'
     
        
def p2n(a):
    i=1
    while i<a:
        if pchecker(i) == 'prime':
            print str(i)
        i=i+1
