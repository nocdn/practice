LOCATIONS = {'Belgium': ['Zedelgem', 'Kontich', 'Roeselare'],
             'France': ['Valence', 'Paris'],
             'Italy': ['Florence', 'Milan']
                }

RESTAURANTS = {'Bar Bulot': ['Zedelgem', 1],
               'Enoteca Pinchiorri': ['Florence', 3],
               'Kei':['Paris', 3],
               'Fortuin': ['Kontich', 1 ],
               'Boury': ['Valence', 3],
               'La Voile': ['Valence', 2],
               'Contraste': ['Paris', 1],
               'Andrea Aprea':['Milan', 2],
               'Seta':['Milan', 2],
               'Boury':['Roeselare', 3]}

#start writting your code after this line

def format_details(details):
    restaurant, location, stars = details
    return f"{restaurant} is located in {location} and has {stars * '*'} stars."

def find_restaurants(country, stars):
   """
   function that finds restaurants in a country with a certain number of stars.

   args:
         country: a string representing the country.
         stars: an integer representing the number of stars.
   returns:
         array: a list of strings representing the restaurants that match the criteria.
   raises:
         ValueError: if the country is not in the directory or if the stars are not between 1 and 3.
   """ 
   
   if country not in LOCATIONS:
        raise ValueError(f"{country} is not in the directory.")
   if stars not in range(1, 4):
        raise ValueError("Stars must be between 1 and 3.")

   formatted_restaurants = []
   for restaurant, details in RESTAURANTS.items():
        if details[0] in LOCATIONS[country] and details[1] == stars:
            formatted_restaurants.append(format_details([restaurant] + details)) # add restaurant name to details

   if len(formatted_restaurants) == 0:
        stars_string = stars * "*"
        return f"""There are no {stars_string} star restaurants in {country}.
        """
   else:
        return formatted_restaurants
   
print(find_restaurants('Italy', 1))