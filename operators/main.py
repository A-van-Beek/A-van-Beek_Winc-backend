# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line
spain_language_spoken = "Castilian Spanish"
switzerland_language_spoken = "German"
check_0 = spain_language_spoken == switzerland_language_spoken
print(check_0)

spain_prevalent_religion = "Roman Catholic"
switzerland_prevalent_religion = "Roman Catholic"
check_1 = spain_prevalent_religion == switzerland_prevalent_religion
print(check_1)

spain_name_length_capital = len("Madrid")
switzerland_name_length_capital = len("Bern")
check_2 = spain_name_length_capital != switzerland_name_length_capital
print(check_2)

spain_GDP = 1,714,860,000,000
switzerland_GDP = 590,710,000,000
check_3 = spain_GDP > switzerland_GDP
print(check_3)

spain_population_growth = 0.13
switzerland_population_growth = 0.65
check_4 = spain_population_growth < 1 and switzerland_population_growth < 1
print(check_4)

spain_population = 47163418
switzerland_population = 8508698
# 10 million = 10,000,0003
check_5 = spain_population > 10000000 or switzerland_population > 10000000
print(check_5)
check_6 = (spain_population > 10000000 and switzerland_population < 10000000) or (spain_population < 10000000 and switzerland_population > 10000000)
print(check_6)
