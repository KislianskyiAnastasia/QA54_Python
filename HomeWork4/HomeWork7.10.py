#=======================1=========================
import csv


def save_books(books):
    with open("books.txt","w", encoding="utf-8") as file:
        for book in books:
            file.write(book + "\n")

books = [ "Harry Potter", "The Hobbit","1984", "The Little Prince", "Farmyard"]
save_books(books)

#===================2===========================
import csv
with open("products.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["product", "price"])
    writer.writerow(["Coffee", "25"])
    writer.writerow(["Tea", "18"])
    writer.writerow(["Chocolate", "12"])


def read_products(filename):
    with open("products.csv","r",encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for pr in reader:
            print(f"Product: {pr['product']}({pr['price']})")

read_products("products.csv")

#========================3======================
# def save_user(username,email,country):
#     with open("user.json","w", encoding="utf-8") as file:
#         file.write(f' "username": "{username}",\n')
#         file.write(f' "email": "{email}",\n')
#         file.write(f' "country": "{country}"\n')
#
# save_user("Anastasia","Kisliamskyian@gmail.com","Israel")

#==============================3.1===================
import json

def save_user(username, email, country):
    user = {
        "username": username,
        "email": email,
        "country": country
    }

    with open("user.json", "w", encoding="utf-8") as file:
        json.dump(user, file, indent=4)

save_user("Anastasia","Kisliamskyian@gmail.com","Israel")

#=======================4==============Не делала===========
