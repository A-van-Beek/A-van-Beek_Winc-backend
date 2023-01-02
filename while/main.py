from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"


def unique_koala_facts(number):
    if number > 1000:
        return print("try less")
    while number > 0:
        print("___", random_koala_fact())
        number -= 1

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
# if __name__ == "__main__":
    # print(random_koala_fact())

unique_koala_facts(15)