#scope.py

# Illustrates:
#   i) meaning of scope 
#  ii) local & global scope

x = 'Hello World'
p = 5

def func():
    " Demonstrates the local scope "
    x = 2
    print(f'Inside "func", x has a value {x}')

def outer_func():
    y = 3

    def inner_func():
        z = y + p
        return z

    return inner_func()

if __name__ == '__main__':
    func()
    print(f'Outside "func", x has a value {x}')
    val = outer_func()
    print('val = ', val)
