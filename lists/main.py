# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line
# opdracht 1: sorteer list
filmlist = [
    "Valley of the Dolls",
    "Goodbye, Mr. Chips",
    "Fiddler on the Roof"
]

def alphabetical_order(list):
    list.sort()
    return list

alphabetical_order(filmlist)

# opdracht 2: check of film in list staat
golden_globe_films = [
    "fiddler on the roof",
    "jaws",
    "star wars",
    "E.T. the Extra-Terrestrial",
    "schindler's list",
    "memoirs of a geisha"

]

def won_golden_globe(film):
    if film.lower() in golden_globe_films:
        return True
    else:
        return False

won_golden_globe("memoirs of a geisha")

# opdracht 3: verwijder item uit list
toto_albums = [
    "Fahrenheit",
    "The Seventh One",
    "Toto XX",
    "Old Is New"
]

mixed_list = [
    "The Seventh One",
    "valley of the volls",
    "goodbye, Mr. chips",
    "Fiddler on the Roof",
    "Toto XX",
]

print(mixed_list)
def remove_toto_albums(mixed_list):
    new_list = []
    for x in mixed_list:
        if x in toto_albums:
            print(f"remove: {x}")
        else:
            print(f"keep: {x}")
            new_list.append(x)
    return new_list

remove_toto_albums(["Old is new"])