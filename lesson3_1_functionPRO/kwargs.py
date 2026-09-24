def print_configuration(**kwags):
    print(type(kwags),kwags)


print_configuration(browser="Safari",headless=True,timeout=10)

def create_user3(**data):
    return data

user = create_user3(name="Anastasia",role="student")
print(user)

# user=create_user3("name": "Kris")
def for_example(a,b=15,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

for_example(2,3,4,5,name="Anastasia")