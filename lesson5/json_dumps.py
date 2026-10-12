#dumps()- pyton->json str
#loads() -json-> pyton object str
import json

#dump() save Pyton object-> file.json(file)
#load() file.json -> pyton


user = {"username":"Anastasia","age":26,"is_admin":True}
json_str = json.dumps(user)
print(json_str)
print(type(json_str))


user = json.loads(json_str)
print()
print(user)
print(type(user))
print(user["username"])

test_config = {
    "url": "http://127.0.0.1:8000",
    "username": "Anastasia",
    "password": "Aa123456!",
    "timeout": 20
}

with open("config.json","w",encoding="utf-8") as file:
    json.dump(test_config,file,indent=4,ensure_ascii=False)

with open("config.json","r",encoding="utf-8") as file:
    config = json.load(file)
    print(config)
    print(config["url"])
    print(config["username"])
    print(config["password"])

#Advanced
def save_profile(name,age,city):
    profile = {
        "name":name,
        "age":age,
        "city":city
    }
    with open("profile.json","w",encoding="utf-8") as file:
        json.dump(profile,file,indent=4)
save_profile("Nastya","26","Yokneam-Illit")

with open("profile.json","r",encoding="utf-8") as file:
    profile = json.load(file)
    print(profile["name"])
