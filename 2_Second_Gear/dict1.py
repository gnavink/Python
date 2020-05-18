# dict1.py

#Illustrates :
#   i)  creating dict, 
#   ii) fetching dict keys & values

d0 = {}
d = { 'root': 18,  'blue': [75, 'R', 2],  21:'venus',
      -14:None,  'mars': 'Rover',  (4,11): 18,  0:45 }


if __name__ == '__main__':
    print(d0)
    print(d)
    print('\n')

    print('Printing the dictionary')
    for key,item in d.items():
        print(key, d[key])
        
    print('\n\n')

    print('Print only the dictionary keys')
    print(d.keys())
    for i in d.keys():
        print(i)

    print('Print only the dictionary values')
    print(d.values())
    for i in d.values():
        print(i)

