def great(name):
    return f"Hello,{name}!"
result =great("Nastya")
print(result)
#result2 = great()
#print(result2)

def create_user(name,role="user"):
    return {"name":name,"role": role}
print(create_user("Alex"))
print(create_user("Nastya","admin"))

def cal_discount(price,discount=20):
    return price - (price*discount/100)

print(cal_discount(2000))
print(cal_discount(2000,25))

def add_tests(name,results=[]):
    results.append(name)
    return results

print(add_tests("test_registration"))
print(add_tests("test_login"))

def add_tests(name,results=None):
    if results is None:
        results = []
    results.append(name)
    return results

print(add_tests("test_registration"))
print(add_tests("test_login"))

def create_user2(username,email,role):
    return f"{username} ({email}) - {role}"
print(create_user2("Nastya","Test@gmail.com","student"))

print(create_user2(role="Student",username="Anastasia",email="Test2@gmail.com"))

print(create_user2("Anastasia",email="Test3@gmail.com",role ="QA"))

