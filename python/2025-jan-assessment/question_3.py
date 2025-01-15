# global dicts for storing data
ingredients = {}
recipes = {}

def import_files(ing_file, rec_file):
    """
    # imports files into global dicts
    # converts floats to ints to avoid precision errors
    """
    global ingredients, recipes
    
    try:
        # read ingredients file
        with open(ing_file, 'r') as f:
            for line in f:
                name, cost, weight = line.strip().split(',')
                # converts to ints (pence and g/ml/count)
                cost_pence = int(float(cost) * 100)
                # converts weight to base units
                weight_base = int(float(weight) * 1000) if name not in ['milk','eggs','lemons'] else int(float(weight) * 100)
                ingredients[name] = (cost_pence, weight_base)
    
        # read recipes file        
        with open(rec_file, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                name = parts[0]
                muffin_count = int(parts[1])
                
                # parse ingredients
                recipe_ingredients = {}
                for i in range(2, len(parts), 2):
                    ing_name = parts[i]
                    amount = parts[i+1]
                    # converts to base units (g/ml/count)
                    amount_base = int(float(amount) * 1000) if ing_name not in ['milk','eggs','lemons'] else int(float(amount) * 100)
                    recipe_ingredients[ing_name] = amount_base
                    
                recipes[name] = (muffin_count, recipe_ingredients)
                
    except FileNotFoundError:
        raise FileNotFoundError("file not found")

def export_data():
    """returns global dicts as list"""
    return [ingredients, recipes]

def total_ingredients(orders):
    """
    # calculates total ingredients needed for orders
    # validates orders format and quantities
    """
    if len(orders) % 2 != 0:
        raise TypeError("malformed order list")
        
    total_ings = {}
    
    # process each order
    for i in range(0, len(orders), 2):
        if not isinstance(orders[i], str) or not isinstance(orders[i+1], int):
            raise TypeError("malformed order list")
            
        recipe_name = orders[i]
        quantity = orders[i+1]
        
        if recipe_name not in recipes:
            raise ValueError("invalid recipe")
        if quantity <= 0:
            raise ValueError("invalid quantity")
            
        recipe_yield, recipe_ings = recipes[recipe_name]
        if quantity % recipe_yield != 0:
            raise ValueError("invalid quantity multiple")
            
        # calculate scaling factor
        batches = quantity // recipe_yield
        
        # add scaled ingredients
        for ing, amount in recipe_ings.items():
            if ing in total_ings:
                total_ings[ing] += amount * batches
            else:
                total_ings[ing] = amount * batches
                
    return total_ings

def total_cost(ingredients_needed):
    """
    # calculates total cost and packs needed
    # ingredients can only be bought in full packs
    """
    total = 0
    packs_cost = {}
    
    for ing, amount in ingredients_needed.items():
        pack_cost, pack_size = ingredients[ing]
        packs = (amount + pack_size - 1) // pack_size
        cost = packs * pack_cost
        total += cost
        packs_cost[ing] = (packs, cost)
        
    return (total, packs_cost)

def shopping_list(ing_file, recipe_file, orders):
    """
    # generates a formatted shopping list
    # imports data, calculates ingredients needed, determines cost and packs
    """
    import_files(ing_file, recipe_file) # no error handling, let exceptions from import_files propagate
    ingredients_needed = total_ingredients(orders) # no error handling here either
    total, packs_cost = total_cost(ingredients_needed)
    
    # format output
    output = "Ingredient    Qty     Cost\n"
    for ing, (qty, cost) in packs_cost.items():
        output += f"{ing:<12}{qty:^4}    £{(cost / 100):>4.2f}\n"
    output += f"Total Cost: £{(total / 100):>4.2f}\n"
    
    return output

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

    # print(total_ingredients(['chocolate', 6]))  # Output for valid orders
    # print(total_ingredients(orders2))  # Raises ValueError
    # print(total_ingredients(orders3))  # Raises TypeError
    # ing = {'flour': 250, 'eggs': 2, 'sugar': 120, 'milk': 200, 'yogurt': 280, 'cocoa': 50}
    # print(total_cost(ing))

    ing_file = 'Ingredients.csv'
    recipe_file = 'Recipes.csv'
    orders = ['chocolate', 96]
    print(shopping_list(ing_file, recipe_file, orders))

except FileNotFoundError as e:
    print(e)
except ValueError as e:
    print(e)
except TypeError as e:
    print(e)