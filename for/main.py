from helpers import get_countries

""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """

def shortest_names():
    countries_lenght = {}
    sorted_countries_by_lenght = {}
    shortest_countries = []
    for countrie in countries:
        countries_lenght[countrie] = len(countrie);
    sorted_countries_by_lenght = sorted(countries_lenght.items(), key=lambda x:x[1]);
    min_lenght = sorted_countries_by_lenght[0][1]
    for sorted_countrie in sorted_countries_by_lenght:
        if sorted_countrie[1] == min_lenght:
            shortest_countries.append(sorted_countrie[0])  
    print(shortest_countries)
    return shortest_countries


# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """

shortest_names()


