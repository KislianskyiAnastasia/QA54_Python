#===========================1=======================
def clean_name(name):
    name = name.strip().title()
    return name
print(clean_name( "   ANASTASIA KISLIANSKYI       " ))

#===================2=====================
def normalize_email(email):
    email = email.strip().lower()
    return email
print(normalize_email("       Kislianskiyan@gmail.com      "))
#=====================3====================
def is_python_file(filename):
    if filename.lower().endswith(".py"):
        return True
    return False

print(is_python_file("Lesson.py"))
print(is_python_file("Lesson.txt"))
print(is_python_file("Lesson.PY"))
#====================4====================
def fix_message(message):
    message = message.replace("Bad","Good").replace("bad","good")
    return message
message = "Bad weather, bad mood"
result = fix_message(message)

print(result)
print(message)
#================5========================
def count_letter(text, letter):
    text = text.lower()
    letter = letter.lower()
    count = text.count(letter)
    return count

print(count_letter("Programming","m"))
print(count_letter("Internationalization", "I"))
#================6=========================
def create_login(first_name, last_name):
    first_name = first_name.strip().lower()
    last_name =last_name.strip().lower()
    result = first_name + "." +last_name
    return result
print(create_login("Anastasia    ", "Kislianskiy  "))
#===================== Bonus 1 ========================
def split_name(full_name):
    full_name = full_name.strip()
    result = full_name.split()
    return result
print(split_name("Anastasia Kislianskiy"))

#===================== Bonus 2 ========================
def check_password(password):
    if len(password) >= 8 and " " not in password and not password.isalpha():
        return True
    else:
        return False

print(check_password("Asdasdasd"))
print(check_password("Asdasd43"))
print(check_password("A2"))




