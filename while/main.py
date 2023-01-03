from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

def unique_koala_facts(number):
    i = 0
    if number > 1000:
        return print("try less")
    while i < number:
        print(random_koala_fact())
        i += 1

def num_joey_facts():
    list_facts = []
    number = 1000
    while number > 0:
        new_fact = random_koala_fact()
        if new_fact.find("joey") != -1:
            list_facts.append(new_fact)
            count = list_facts.count(new_fact)
            if count == 10:
                result = set(list_facts)
                return len(result)  
        number -= 1

def koala_weight():
    number = 1000
    while number > 0:
        new_fact = random_koala_fact()
        if new_fact.find("kg") != -1:
            for i in new_fact.split():
                if i.find("kg") != -1:
                    weight_kg = i
                    for x in weight_kg.split("k"):
                        if x.isdigit():
                            return int(x)
            return
        else:
            number -= 1



# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    print(random_koala_fact())
    unique_koala_facts(2)
    num_joey_facts()
    koala_weight()
