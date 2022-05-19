def initials(name):
    first = name[0].upper()
    last = name[name.find(' ')+1].upper()
    return f'{first}. {last}.'

initials('Ex Ample')
initials('Bob Cat')
initials('Function Nice')

def multiply(a, b):
    return a * b

multiply(2, 2)
multiply(9, 2.3)
multiply(29, 'Hey! ')