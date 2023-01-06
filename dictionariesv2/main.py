# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line


def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    passport_dict = {
        "name": name,
        "date_of_birth": date_of_birth,
        "place_of_birth": place_of_birth,
        "height": height,
        "nationality": nationality,
    }
    return passport_dict


def add_stamp(person, country):
    if country == person.get("nationality"):
        return person
    if person.get("stamps"):
        if country in person["stamps"]:
            return "already stamped"
        else:
            person["stamps"].append(country)
            return person
    else:
        person["stamps"] = [country]
        return person


# create a person
person_1 = create_passport("Pietje Puk", 2002 - 12 - 31, "Zwolle", 1.54, "Nederland")
person_1_add_stamp1 = add_stamp(person_1, "Engeland")
person_1_add_stamp2 = add_stamp(person_1, "France")
person_1_add_3 = add_stamp(person_1, "Nederland")
person_1_add_4 = add_stamp(person_1, "Engeland")
print(person_1)


def create_biometric(name_biometric, value_biometric, date_biometric):
    new_biometric = {"date": date_biometric, "value": value_biometric}
    return new_biometric


def add_biometric_data(person, name_biometric, value_biometric, date_biometric):
    if person.get("biometric"):  # biometric bestaat al, updaten of toevoegen?
        biometric = person.get("biometric")
        name_new_biometric = create_biometric(
            name_biometric, value_biometric, date_biometric
        )
        if name_biometric in biometric:  # hier updaten
            biometric[name_biometric] = name_new_biometric
        else:  # hier toevoegen nieuwe
            biometric[name_biometric] = name_new_biometric
        return person
    else:
        name_new_biometric = create_biometric(
            name_biometric, value_biometric, date_biometric
        )
        person["biometric"] = {name_biometric: name_new_biometric}

    return person


omari = create_passport("Omari Muchumba", "1995-07-16", "Kampala", 184.31, "Uganda")
omari_add_1 = add_biometric_data(omari, "eye_color_left", "blue", "2020-05-05")
omari_add_2 = add_biometric_data(omari, "eye_color_right", "red", "2020-06-06")
omari_edit_1 = add_biometric_data(omari, "eye_color_left", "brown", "2022-01-10")


# Add fingerprints too: just another value, but this is also a dict.
fingerprint_data = {
    "left_pinky": "2378945",
    "left_ring": "2349081",
    "left_middle": "132890",
    "left_index": "9823234",
    "left_thumb": "0924131",
    "right_thumb": "6234923",
    "right_index": "13249734",
    "right_middle": "34023784",
    "right_ring": "12332538",
    "right_pinky": "32458970",
}

omari_add_fingerprints = add_biometric_data(
    omari, "finger_prints", fingerprint_data, "2022-01-12"
)


print(omari)
