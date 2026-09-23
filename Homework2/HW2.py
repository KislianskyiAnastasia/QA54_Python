#======================1====================
def clean_card(cart):
    if not isinstance(cart,list):
        return "Card must be a list"

    while "sold out" in cart :
        cart.remove("sold out")
    return cart

print(clean_card(["milk", "sold out", "bread", "sold out","tee"]))

#=======================2=======================
def temperature_report(temperatures):
    if not isinstance(temperatures,list):
        return "temperatures must be a list"
    result = []

    for temperature in temperatures:
        if temperature > 25:
            result.append(temperature)

    return result


print(temperature_report([21, 28, 19, 31, 25, 27]))

#=========================3======================

def fix_balances(balances):
    if not isinstance(balances,list):
        return "balances must be a list"
    for i in range(len(balances)):
        if balances[i] < 0:
            balances[i] = 0
    return balances

print(fix_balances([-1,8,39,-43]))

#===================4====================
def unique_items(items):
    if not isinstance(items,list):
        return "Error, items must be a list"
    result = []

    for item in items:
        item = item.strip()

        if item not in result:
            result.append(item)

    return result

print(unique_items([" green", "red", "red", "black ", " green"]))

