# global dicts for ingredients and recipes
ingredients_dict = {}
recipes_dict = {}

def import_files(ingredients_file, recipes_file):
    # try opening ingredients file
    try:
        with open(ingredients_file, 'r') as f:
            ingredients_data = f.read().strip().split('\n')
    except FileNotFoundError:
        raise FileNotFoundError(f"{ingredients_file} not found")
    
    # try opening recipes file
    try:
        with open(recipes_file, 'r') as f:
            recipes_data = f.read().strip().split('\n')
    except FileNotFoundError:
        raise FileNotFoundError(f"{recipes_file} not found")
    
    # parse ingredients
    for line in ingredients_data:
        parts = line.split(',')
        key = parts[0]
        cost_pounds = float(parts[1])
        pack_size = float(parts[2])
        
        # convert to integer (pence and grams/items)
        if key in ['milk']:
            # milk is in litres, convert to millilitres
            pack_size_int = int(pack_size * 1000)
        elif key in ['eggs', 'lemons']:
            # per items, keep as integer
            pack_size_int = int(pack_size)
        else:
            # kg to grams
            pack_size_int = int(pack_size * 1000)
        
        cost_pence = int(round(cost_pounds * 100))
        
        ingredients_dict[key] = (cost_pence, pack_size_int)
    
    # parse recipes
    for line in recipes_data:
        parts = line.split(',')
        recipe_name = parts[0]
        quantity = int(parts[1])
        ingredients = {}
        
        # iterate over ingredient-quantity pairs
        for i in range(2, len(parts), 2):
            ing = parts[i]
            qty = float(parts[i+1])
            
            # convert qty to integer based on ingredient type
            if ing in ['milk']:
                qty_int = int(qty * 1000)  # litres to millilitres
            elif ing in ['eggs', 'lemons']:
                qty_int = int(qty)  # items
            else:
                qty_int = int(qty * 1000)  # kg to grams
            
            ingredients[ing] = qty_int
        
        recipes_dict[recipe_name] = (quantity, ingredients)

def export_data():
    # return list of ingredients and recipes dicts
    return [ingredients_dict, recipes_dict]

def total_ingredients(order_list):
    if not isinstance(order_list, list):
        raise TypeError("orders should be a list")
    
    if len(order_list) % 2 != 0:
        raise TypeError("malformed orders list")
    
    total = {}
    
    for i in range(0, len(order_list), 2):
        recipe = order_list[i]
        qty = order_list[i+1]
        
        if not isinstance(recipe, str) or not isinstance(qty, int):
            raise TypeError("malformed orders list")
        
        if qty <= 0:
            raise ValueError("invalid order quantity")
        
        if recipe not in recipes_dict:
            raise ValueError(f"recipe {recipe} not found")
        
        recipe_qty, ingredients = recipes_dict[recipe]
        
        if qty % recipe_qty != 0:
            raise ValueError("ordered qty not multiple of recipe production")
        
        factor = qty // recipe_qty
        
        for ing, amt in ingredients.items():
            total[ing] = total.get(ing, 0) + amt * factor
    
    return total

def total_cost(ingredients_required):
    total = 0
    cost_details = {}
    
    for ing, req_amt in ingredients_required.items():
        if ing not in ingredients_dict:
            raise ValueError(f"ingredient {ing} not found")
        
        cost_pence, pack_size = ingredients_dict[ing]
        
        # calculate packs needed
        packs = req_amt // pack_size
        if req_amt % pack_size != 0:
            packs += 1
        
        total_pack_cost = packs * cost_pence
        total += total_pack_cost
        cost_details[ing] = (packs, total_pack_cost)
    
    return [total, cost_details]

# example usage:
if __name__ == "__main__":
    # simulate file contents
    with open('Ingredients.csv', 'w') as f:
        f.write("""flour,1.56,1.50
butter,2.1,0.25
sugar,4.73,1.00
cocoa,9.9,0.50
yogurt,2.4,1.00
blueberries,2.35,0.15
oats,10.4,3.00
milk,1.55,2.27
eggs,1.9,10
lemons,1.15,4""")
    
    with open('Recipes.csv', 'w') as f:
        f.write("""chocolate,6,flour,0.125,eggs,1,sugar,0.060,milk,0.100,yogurt,0.140,cocoa,0.025
blueberry,12,flour,0.250,butter,0.100,eggs,2,sugar,0.140,milk,0.010,yogurt,0.140,blueberries,0.125
lemon,6,flour,0.115,butter,0.100,eggs,2,sugar,0.100,yogurt,0.100,lemons,2
oat,9,butter,0.020,eggs,2,milk,0.100,oats,0.200""")
    
    # import data
    import_files('Ingredients.csv', 'Recipes.csv')
    
    # export data
    data = export_data()
    print(data)
    
    # calculate total ingredients
    orders = ['chocolate', 6]
    ingredients_needed = total_ingredients(orders)
    print(ingredients_needed)
    
    # calculate total cost
    cost = total_cost(ingredients_needed)
    print(cost)

import_files('Ingredients.csv', 'Recipes.csv')
print(total_ingredients(['chocolate', 6])) 