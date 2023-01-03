from helpers import get_countries

""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """

def shortest_names(countries):
    countries_length = {}
    sorted_countries_by_length = {}
    shortest_countries = []
    for countrie in countries:
        countries_length[countrie] = len(countrie);
    sorted_countries_by_length = sorted(countries_length.items(), key=lambda x:x[1]);
    min_length = sorted_countries_by_length[0][1]
    for sorted_countrie in sorted_countries_by_length:
        if sorted_countrie[1] == min_length:
            shortest_countries.append(sorted_countrie[0])  
    # print("kortste landen:", shortest_countries[0:2])
    return shortest_countries

def most_vowels(countries):
    countries_by_vowels = {}
    sorted_countries_by_vowels = {}
    countries_most_vowels = []
    for countrie in countries:
        num_vowels = 0
        for char in countrie:
            if char.lower() in "aeiou":
                num_vowels += 1
        countries_by_vowels[countrie] = num_vowels
        sorted_countries_by_vowels = sorted(countries_by_vowels.items(), key=lambda x:x[1], reverse=True);
    for sorted_countrie_by_vowels in sorted_countries_by_vowels:
        countries_most_vowels.append(sorted_countrie_by_vowels[0])
    # print("meeste klinkers:", countries_most_vowels[0:3])
    return countries_most_vowels[0:3]


# volgorde weinig -> z, q, j, x, k, v b p g
countries_alphabet=[]

def add_new_country(next_char, countries):
    for countrie in countries:
        for char in countrie:
            if char.lower() == next_char:
                countries_alphabet.append(countrie)
                return

def check_in_countries_alphabet(next_char, countries):
    for countrie in countries_alphabet:
        for char in countrie:
            if char.lower() == next_char:
                return
    add_new_country(next_char, countries)

def alphabet_set(countries):
    for next_char in "zqjxkvbpgacdefhilmnorstuwy":
        check_in_countries_alphabet(next_char, countries)
    return countries_alphabet
    # print("countries_alphabet:", countries_alphabet, len(countries_alphabet))

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()
    shortest_names(countries)
    most_vowels(countries)
    alphabet_set(countries)

    """ Write the calls to your functions here. """






