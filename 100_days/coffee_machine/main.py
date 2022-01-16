
# Data ---------------------------------------------------------------------------------------------
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Functions ----------------------------------------------------------------------------------------
# Print the remaining resources
def report():
    print(resources)

# Reduce the amount of specific resource
def reduce(ingredient, amount):
    resources[ingredient] -= amount

# Return how much the drink costs
def cost(drink):
    return MENU[drink]["cost"]

# Return how much ingredient is used
def recipe(drink, ingredient):
    if ingredient == "water":
        return MENU[drink]["ingredients"]["water"]
    elif ingredient == "coffee":
        return MENU[drink]["ingredients"]["coffee"]
    elif ingredient == "milk":
        return MENU[drink]["ingredients"]["milk"]
    else:
        return 0

# Cost logic
def check_cost(drink, input_amount):
    required = cost(drink)
    if required > input_amount:
        return False
    else:
        return True

# Ensure sufficient ingredient are present and reduce the amount if true
def check_resouce(drink, ingredient):
    required = recipe(drink, ingredient)
    left_over = resources[ingredient]
    if required > left_over:
        return False
    else:
        return True

# Convert quarters to dollars
def dollar_amount(quarters):
    return (quarters * 0.25)

# Calculate how much to give back to the user
def money_back(user_input, cost):
    return (user_input - cost)

# Select Order -------------------------------------------------------------------------------------
def game():
    sufficient_ingredient = True
    drink_oi = ""
    user_money = ""
    
    while drink_oi == "":
        drink_oi = input("What would you like? [e]spresso, [l]atte, [c]appuccino\n>").lower()
        
        if drink_oi in ["e", "espresso"]:
            drink_oi = "espresso"
        elif drink_oi in ["l", "latte"]:
            drink_oi = "latte"
        elif drink_oi in ["c", "cappuccino"]:
            drink_oi = "cappuccino"
        else:
            drink_oi = ""
            report()

    while not user_money.isnumeric():
        print(f"That would be ${MENU[drink_oi]['cost']}")
        user_money = input("How many quarters ($0.25) do you have?\n>")

    user_money = float(user_money)
    user_dollars = dollar_amount(user_money)

    # Check Money ----------------------------------------------------------------------------------
    if check_cost(drink_oi, user_dollars):
        sufficient_amount = True
    else:
        sufficient_amount = False

    # Check Resource -------------------------------------------------------------------------------
    ings = ["water", "coffee", "milk"]
    if drink_oi == "espresso":
        ings = ["water", "coffee"]

    check_ings = []
    for i in ings:
        check_ings.append(check_resouce(drink_oi, i))

    if all(check_ings):
        sufficient_ingredient = True
    else:
        sufficient_ingredient = False

    # Subtrack Resource & Money --------------------------------------------------------------------
    if (sufficient_amount and sufficient_ingredient):
        for i in ings:
            ing_amount = recipe(drink_oi, i)
            reduce(i, ing_amount)
        
        cost_of_drink = cost(drink_oi)
        return_to_user = money_back(user_dollars, cost_of_drink)
        print(f"Your return amount is ${return_to_user}")
        report()
    else:
        print(f"Bruh. ${user_dollars}?")
        print("Returning coins...")
    
    try_again = input("Would you like to try again? [y/n]\n>").lower()
    if try_again == "y":
        game()
    else:
        print("Have a good day!")

game()
