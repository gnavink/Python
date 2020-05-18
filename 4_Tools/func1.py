#func1.py

# Illustrates :
#             i) Creating Functions
#            ii) Positional Arguments
#           iii) Key Word Arguments
#           iv)  Variable Arguments
#           v)   Variable key word Arguments

#def product1(a, b, c) :
def product1(a:int, b:int, c:int) -> int :
    """
        Computes the product of the given integers
    """
    return a * b * c


def product2(a : int, b : int, *args) -> (int , int ):
    """
       Computes the addition of the first 2 arguments & the product of 
       other variable arguments
    """
    valadd = a + b
    valmul = 1
    for i in args:
        valmul *= i
    return valadd, valmul

def do_add(a: int, b: int) -> int:
    return a + b

def do_mul(a: int, b:int) -> int:
    return a * b

#def add_person_details(aadhar : str, first : str, surname : str = None, middle :str = None, **kwargs ):
def add_person_details(aadhar,        first,       surname = None,       middle = None,       **kwargs ):
    """"
        Populates the persons details in a dict and prints them
    """
    print('aadhar No:', int(aadhar))
    print('First name:', first)
    if surname:
        print('surname:', surname) 
    if middle:
        print('Middle name:', middle) 
    for key in kwargs:
        print(f'key = {key},   keyvalue = {kwargs[key]}')

if __name__ == '__main__':
    L = [2, 3, 5]

    ans = product1(2, 3, 5)  # Passing all the positional arguments
    print(ans)

    #ans = product1(*L)       # Unpacking the sequence and building the parameters
    #print(ans)

    #ans = product1(2, *L[1:]) 
    #print(ans)

    #ans = product2(2, 3, 5)
    #print(ans)

    #ans = product2(2, 3, 5, 6, 7)
    #print(ans)

    # If the parameters are other than integers, python integer doesn't check them.
    # The function annotation is only for user convenience
    #ans = product2(2, 3.2, 5, 6.4, 7) 
    #print(ans)

   #add_person_details('1234', 'Navin', surname = 'Kandala', middle = 'Kumar', last = 'GopalaKrishnan', age = 45)
    
    # Key word arguments can be in any order
    #add_person_details('1234', 'Navin', middle = 'Kumar', surname = 'Kandala',  last = 'GopalaKrishnan') 

    # Keyword arguments can take default values if NOT provided
    #add_person_details('1234', 'Navin',  middle = 'Kumar', last = 'GopalaKrishnan', age = 45)