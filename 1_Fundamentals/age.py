#age.py
# This program keeps prompting the user to enter a valid age.
# If a valid integer is enter, it prints and exits the function

def get_int(msg):
     while(True):
         try:
             i = int(input(msg))
             return i
         except ValueError as err:
             print(err)

if __name__ == '__main__' :
    age = get_int('Enter your age:')
    print('age = ', age)