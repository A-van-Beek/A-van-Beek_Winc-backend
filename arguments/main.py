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
    "neptune": 11.2,
    "saturn": 10.4,
    "earth": 9.8,
    "uranus": 8.9,
    "venus": 8.9,
    "mars": 3.7,
    "mercury": 3.7,
    "moon": 1.6,
    "pluto": 0.6,
}


def force(mass: float, body="earth"):
    gravity = planets[body]
    total_force = mass * gravity
    return total_force


# print(force(1))
def pull(m1: float, m2: float, d: float):
    G = 6.674 * (10**-11)
    F = G * ((m1 * m2) / d**2)
    F_rounded = round(F, 10)
    return F_rounded


m1 = 0.1  # massa van 1 appel
m2 = 5972 * (10**24)  # massa van de aarde
d = 6371 * (10**6)  # afstand in meters

print(pull(800, 1500, 3))
