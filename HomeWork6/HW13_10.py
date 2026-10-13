#======================1====================

def get_product(products,index):
    try:
        product = products[index]
        return product
        # return (f"Product: {product}")
    except IndexError:
        return "Product index is out of range"
products = ["coffee","tea","milk"]
# index = int(input("Product № :"))

print(get_product(products,0))
#======================2====================
def get_settings_value(settings,key):
    try:
        value = settings[key]
        return value
    except KeyError:
        return "Setting was not found"
settings = {"language":"English",
            "them":"dark"}

print(get_settings_value(settings,"them"))
#======================3===================
def calculate_total_price(price,quantity):
    try:
        price = float(price)
        quantity = float(quantity)
        result = price * quantity
        return result
    except ValueError:
        return "Value must be a number"
    except TypeError:
        return "Invalid data type"

print(calculate_total_price("12.5","4"))
print(calculate_total_price("coffee","4"))
print(calculate_total_price(None,"4"))
print(calculate_total_price("0","0"))
print(calculate_total_price("4.3","tea"))
#=======================4=======================
def read_temperature():
    try:
        temp = float(input("Enter the temperature: "))
        # temp = float(temp)
        print("Temperature was entered successfully")
    except ValueError:
        print("Invalid temperature")
    print("Program finished")

read_temperature()

#======================5========================
def validate_discount(discount):
    if discount >= 0 and discount <= 100:
        return discount
    else:
        if discount < 0:
            raise ValueError("Discount cannot be negative")
        elif discount > 100:
            raise ValueError("Discount cannot be greater than 100")


try:
    discount = int(input("Enter discount: "))
    print(validate_discount(discount))
except ValueError as error:
    print(error)
