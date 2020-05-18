#scope2.py

#Illustrates:
# usage of global keyword

total = 0

def add_to_total(n):
    "Updates the variable global variable total"
    global total
    total = total + n

if __name__ == '__main__':
    add_to_total(5)
    print(total)
