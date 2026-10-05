import csv

with open("user_csv.csv","w",encoding="utf-8",newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["name","email","role"])
    writer.writerow(["Lena","LenD@gnail.com","QA"])
    writer.writerow(["Ivan","IvKis@gnail.com","dev"])

with open("user_csv.csv") as file:
    reader = csv.reader(file)
    print(type(reader))
    for row in reader:
        print(row)
        print(row[1]) #email

with open("user_csv.csv","r",encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        print(row["name"],"-",row["role"])