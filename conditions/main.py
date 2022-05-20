# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line
# farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True)
# 'fertilize pasture'

def farm_action(weather, time_of_day, cow_milking_status, location_of_cows, season, slurry_tank, grass_status):
    if (cow_milking_status == True and location_of_cows == "pasture") or (slurry_tank == True and (weather != "sunny" or weather != "windy") and location_of_cows == "pasture") or (grass_status == True and season == "spring" and weather == "sunny" and location_of_cows == "pasture"):
        # bijzondere voorwaarden ! meer taakregels
        if cow_milking_status == True and location_of_cows == "pasture":
            # alleen eerste
            return "take cows to cowshed\nmilk cows\ntake cows back to pasture"
        elif slurry_tank == True and (weather != "sunny" or weather != "windy") and location_of_cows == "pasture":
            # alleen tweede
            return "take cows to cowshed\nfertilize pasture\ntake cows back to pasture"
        elif grass_status == True and season == "spring" and weather == "sunny" and location_of_cows == "pasture":
            # alleen derde
            return ("take cows to cowshed\nmow grass\ntake cows back to pasture")
    elif (location_of_cows == "pasture" and time_of_day == "night") or (location_of_cows == "pasture" and weather == "rainy"):
        return ("take cows to cowshed")
    elif cow_milking_status == True and location_of_cows == "cowshed":
        return ("milk cows")
    elif slurry_tank == True and location_of_cows == "cowshed" and (weather != "sunny" or weather != "windy"):
        return  ("fertilize pasture")
    elif grass_status == True and season == "spring" and weather == "sunny" and location_of_cows != "pasture":
        return ("mow grass")
    else:
        return ("wait")

# weather (rainy, sunny, windy, neutral)
# time_of_day (day, night)
# cow_milking_status (need milking: True, False)
# location_of_cows (pasture, cowshed)
# season (winter, spring, summer, fall)
# slurry_tank (full: True, False)
# grass_status (long: True, False)

farm_action('sunny', 'day', True, 'pasture', 'spring', False, True)