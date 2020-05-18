# string_ex4.py
#Demonstrates :
#               i)string methods eg. join, split. 
#              ii) Replication operator

# India fights Corona
s1 = ['India', 'fights', 'Corona']
s4 = 'Gandhiji*1869-10-02*1948-01-31'

def split_fields(record) :
    fields = record.split('*')
    print(fields)
    B_day = fields[1].split('-')
    D_day = fields[2].split('-')
    num_yrs_lived = int(D_day[0]) - int(B_day[0])
    return num_yrs_lived

if __name__ == '__main__':
    s2 = ' '.join(s1)
    print(s2)

    s3 = '=' * 5
    print(s3)
    print(len(s3))
    
    num_yrs_lived = split_fields(s4)
    print(f'Gandhiji lived for {num_yrs_lived} years')