# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorer_name_0 = "Ruud Gullit"
scorer_name_1 = "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorer_0 = f"{scorer_name_0} {goal_0}" # manier 1 om samen te voegen
scorer_1 = scorer_name_1 + " " + str(goal_1) # manier 2
scorers = scorer_0 + ", " + scorer_1
# print(scorer_total)

report = f"{scorer_name_0} scored in the {goal_0}nd minute\n{scorer_name_1} scored in the {goal_1}th minute"
# print(report)

# splitting first and last name, option 1
player_2 = "Frank Rijkaard"
splitted_player_2 = player_2.split()
first_name_2 = splitted_player_2[0]
last_name_2 = splitted_player_2[1]

# splitting first and last name, option 2
player = "Hans van Breukelen"
x = player.find(" ")
first_name = player[:x]
last_name = player[x+1:]
name_short = first_name[0] + ". " + last_name
last_name_len = len(last_name)


chant = (first_name + "! ") * (len(first_name)-1) + (first_name + "!")
bad_chant = (first_name + "! ") * len(first_name)
good_chant = chant[-1] != " "