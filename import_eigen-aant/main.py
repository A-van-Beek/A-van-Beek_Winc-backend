# import mod
# print(mod.s)


from mod import s, foo

# from <module_name> import <name(s)>
print(s)

from mod import *

# from <module_name> import *
# neemt alle namen mee, behalve de private (begint met underscore)


# from <module_name> import <name> as <alt_name>[, <name> as <alt_name> …]
# import <module_name> as <alt_name>

# een import kan ook vanuit binnen een functie.
# let op: dan niet met asterix *
def bar():
    from mod import foo

    foo("corge")


try:
    # non-existend module
    import baz
except ImportErros:
    print("module not found")
