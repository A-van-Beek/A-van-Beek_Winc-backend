from re import T
from xxlimited import foo


example_one = 'I am a string.'
example_two = "Me too!"
example_three = """I too am a string.
                    I am, in fact, a multiline string!"""

example_four = 'I\'m a string.'
example_five = "I'm a string."
example_six = 'He said: "I\'m a string"'

example_seven = "I'm a string. \nwith a new line \n\tand a new line with tab." #note: no space after \n
print(example_seven)

print('foo\nbar')
print('''This string has a single (') and a double (") quote.''')
print('Jump!' * 5)

print(type (str(5) in 'We were lucky that they had a table for 5.'))
print('Samuel' in 'We went out for dinner with with Anne, Samuel and Bob.')
print('You' == 'Me')

letter_grades = 'ABCDF'
print(letter_grades[0])

waltz = 'onetwothree'
waltz[0:3]
# We don't need to specify the 0 if we start at the beginning
waltz[:3]
waltz[3:6]
waltz[6:11]
# Same goes for the end -- we can leave it empty
waltz[6:]
# We can specify a step size if we don't want a continuous slice
print(waltz[0:11:2])

# -----------------------
# string interpolation
# -----------------

# option 1: The + Operator
s = 'foo'
t = 'bar'
u = 'baz'
total = s + t
print(total)

# option 2: The * Operator
'''The * operator creates multiple copies of a string.
If s is a string and n is an integer, either of the following expressions
returns a string consisting of n concatenated copies of s'''
s = 'foo'
total = s * 4
print(total)

# option 3: The in Operator
'''Python also provides a membership operator that can be used with strings.
The in operator returns True if the first operand is contained within the second,
and False otherwise:'''
s = "foo"
question = s in 'That\'s food for thought.'
print(question)

s = "foo"
question = s not in 'That\'s food for thought.'
print(question)



answer = 42
qa = f'The answer is.. {answer}'
print(qa)