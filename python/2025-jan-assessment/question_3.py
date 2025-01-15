# global dictionaries to store ingredient and recipe data
ingredients_data = {}
recipes_data = {}

def import_files(ingredients_file, recipes_file):
    """
    imports ingredient and recipe data from files into global dictionaries.

    args:
        ingredients_file: path to the 'ingredients.csv' file.
        recipes_file: path to the 'recipes.csv' file.

    raises:
        FileNotFoundError: if either of the files does not exist.
    """
    global ingredients_data, recipes_data

    # import ingredients
    try:
        with open(ingredients_file, 'r') as f:
            for line in f:
                row = line.strip().split(',')
                ingredient, cost, weight = row
                ingredients_data[ingredient] = (int(float(cost) * 100), int(float(weight) * 1000 if ingredient not in ['eggs', 'lemons'] else float(weight)))

    except FileNotFoundError:
        raise FileNotFoundError(f"the file '{ingredients_file}' was not found.")

    # import recipes
    try:
        with open(recipes_file, 'r') as f:
            for line in f:
                row = line.strip().split(',')
                recipe_name, quantity = row[0], int(row[1])
                ingredients = {}
                for i in range(2, len(row), 2):
                    ingredient, amount = row[i], row[i + 1]
                    ingredients[ingredient] = int(float(amount) * 1000 if ingredient not in ['eggs', 'lemons'] else float(amount))
                recipes_data[recipe_name] = (quantity, ingredients)

    except FileNotFoundError:
        raise FileNotFoundError(f"the file '{recipes_file}' was not found.")

def export_data():
    """
    returns the contents of the global ingredient and recipe dictionaries.

    returns:
        a list containing the ingredients dictionary and the recipes dictionary, in that order.
    """
    return [ingredients_data, recipes_data]

def total_ingredients(orders):
    """
    calculates the total ingredients needed for a list of orders.

    args:
        orders: a multidimensional list of orders, where each order is a pair: [recipe_name, quantity].

    returns:
        a dictionary of ingredients and their required quantities.

    raises:
        ValueError: if quantity is zero or less, or not a multiple of recipe production quantity.
        TypeError: if the list of orders is malformed (not pairs of [recipe_name, quantity]).
    """
    total_ingredients_needed = {}

    if len(orders) % 2 != 0:
        raise TypeError("malformed list of orders: orders must be in pairs of [recipe_name, quantity].")

    for i in range(0, len(orders), 2):
        try:
            recipe_name, quantity = orders[i], orders[i+1]
        except (TypeError, IndexError):
            raise TypeError("malformed list of orders: orders must be in pairs of [recipe_name, quantity].")

        if not isinstance(recipe_name, str) or not isinstance(quantity, int):
            raise TypeError("malformed list of orders: orders must be in pairs of [recipe_name, quantity].")

        if recipe_name not in recipes_data:
            raise ValueError(f"recipe '{recipe_name}' not found.")
        
        recipe_quantity, recipe_ingredients = recipes_data[recipe_name]

        if quantity <= 0:
            raise ValueError("quantity ordered must be greater than zero.")

        if quantity % recipe_quantity != 0:
            raise ValueError(f"quantity ordered must be a multiple of {recipe_quantity} for '{recipe_name}'.")

        multiplier = quantity // recipe_quantity

        for ingredient, amount in recipe_ingredients.items():
            total_ingredients_needed[ingredient] = total_ingredients_needed.get(ingredient, 0) + amount * multiplier

    return total_ingredients_needed


# example usage
try:
    import_files('Ingredients.csv', 'Recipes.csv')
    data = export_data()
    # print("ingredients:", data[0])
    # print("recipes:", data[1])

    orders1 = ['chocolate', 48, 'blueberry', 12]
    orders2 = ['oat', 16, 'chocolate', 11, 'lemon', 0]
    orders3 = [48, 'chocolate', 'blueberry']
    orders4 = ['chocolate', 6]

    print(total_ingredients(['chocolate', 6]))  # Output for valid orders
    # print(total_ingredients(orders2))  # Raises ValueError
    # print(total_ingredients(orders3))  # Raises TypeError

except FileNotFoundError as e:
    print(e)
except ValueError as e:
    print(e)
except TypeError as e:
    print(e)# example usage