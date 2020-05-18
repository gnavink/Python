#func2.py

#Illustrates:
#  i)  Importing Sys module
#  ii) Command line arguments
#  iii) Exceptions  in action 

import sys     #sys is an  Standard Python module
import func1   # func1 is our own external module

d = {'add': None, 'mul': None, 'div': None}
opt = sys.argv[1]

def do_op(op, a, b) :
    error = None
    try:
        val = d[op]  #To check whether its a valid operation
        l = []
        l.extend([a,b])
        if opt == 'add':
            return l, func1.do_add(a,b)
        elif opt == 'mul':
            return l, func1.do_mul(a, b)
        else :
            return l, a // b 

    except KeyError as err:
        error = 'Exception'
        print(f'InValid Operation {op}')
    except ZeroDivisionError as err:
        error = 'Exception'
        print('Denominator is zero', err)
            
    finally:
        if error:
            print('Exception occured')
        print('Successful execution of the function')


if __name__ == '__main__':
    a = 10 
    b = 5
    #b = 0

    ans = do_op(opt, a, b)
    if ans:
        print(ans)

    


