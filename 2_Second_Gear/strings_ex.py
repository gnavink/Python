#strings_ex.py

# Shows the usage of ' , ", """ quotes

a = "Single 'quotes' are fine; \"doubles\" must be escaped."
b = 'Single \'quotes\' must be escaped; "doubles" are fine.'

text = """A triple quoted string like this can include 'quotes' and "quotes" without 
formality. We can also escape newlines \
so this particular string is actually only two lines long."""

s = 'Light ray'

if __name__ == "__main__":
    print(a)
    print(b)
    print(text)
    
    print('s =',s, 'Len s =', len(s))
    print(s[0], s[-9])
    print(s[8], s[-1])

