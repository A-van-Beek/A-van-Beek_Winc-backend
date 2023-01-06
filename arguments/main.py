# Do not modify these lines
__winc_id__ = "7b9401ad7f544be2a23321292dd61cb6"
__human_name__ = "arguments"

# Add your code after this line


def greet(name, greet_template="Hello, <name>!"):
    greet_template_elements = []
    for element in greet_template.split("<"):
        if element.find(">") != -1:
            greet_template_elements.append(name)
            greet_template_elements.append(element.split(">")[1])
        else:
            greet_template_elements.append(element)
    greeting = "".join(greet_template_elements)
    return greeting


# print(greet("Piet", "wat leuk, <name>"))
