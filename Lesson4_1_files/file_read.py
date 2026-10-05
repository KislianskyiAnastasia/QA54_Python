with open("user.txt","w",encoding="utf-8") as file:
    file.write("Anastasia\n")
    file.write("Nicole\n")


#READ весь файл полностью

with open("user.txt","r",encoding="utf-8") as file:
    content = file.read()
    print(content)
    print(len(content))

#READLINES() возырват списка где каждый элемент отдельная
with open("user.txt","r",encoding="utf-8") as file:
    lines = file.readlines()
    print(lines)
    for line in lines:
        print(line.strip())

#FOR

with open("user.txt","r",encoding="utf-8") as file:
    for line in file:
        print(line.strip())