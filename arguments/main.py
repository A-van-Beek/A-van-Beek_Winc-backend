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
planets = {
    "sun": 274,
    "juputer": 24.9,
    "neptune": 11.1,
    "saturn": 10.4,
    "earth": 9.7,
    "uranus": 8.8,
    "venus": 8.8,
    "mars": 3.7,
    "mercury": 3.7,
    "moon": 1.6,
    "pluto": 0.5,
}


def force(mass: float, body="earth"):
    gravity = planets[body]
    total_force = mass * gravity
    return total_force


print(force(1))
