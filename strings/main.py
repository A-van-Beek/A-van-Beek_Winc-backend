# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player_1 = "Ruud Gullit"
player_2 = "Marco van Basten"

goal_1 = "32"
goal_2 = "54"

scorer_1 = f"{player_1} {goal_2}"
scorer_2 = player_2 + " " + goal_2
# print(scorer_2)

report = f"{player_1} scored in the {goal_1}nd minute\n{player_2} scored in the {goal_2}th minute."
# print(report)

# splitting first and last name, option 1
player_3 = "Frank Rijkaard"
splitted_player_3 = player_3.split()
first_name_3 = splitted_player_3[0]
last_name_3 = splitted_player_3[1]
# print(first_name_3)
# print(last_name_3)

# splitting first and last name, option 2
player_4 = "Hans van Breukelen"
x = player_4.find(" ")
first_name_4 = player_4[:x]
last_name_4 = player_4[x+1:]
# print(first_name_4)
# print(last_name_4)
name_short_4 = first_name_4[0] + ". " + last_name_4
# print(name_short_4)

chant = (first_name_4 + "!") * len(first_name_4)
print(chant)

print(2 != 3)
print(2 != 2)