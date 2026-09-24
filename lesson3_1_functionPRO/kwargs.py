def print_configuration(**kwags):
    print(type(kwags),kwags)


print_configuration(browser="Safari",headless=True,timeout=10)

def create_user3(**data):
    return data

user = create_user3(name="Anastasia",role="student")
print(user)
