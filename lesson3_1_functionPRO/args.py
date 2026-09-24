def total(*args):
    print(type(args),args)
    return sum(args)

print(total(1,3,2))
print(total(10,11))
print(total(12,20,30,50))
print(total())

def print_scores(students,*scores):
    print(f"Students:{students}")
    print("scores:", scores)

print_scores("Anastasia",26,6,20)
print_scores("Alla", 20)

def check_status_code(*codes):
    for code in codes:
        assert code == 200

print(check_status_code(200,200,200))
#print(check_status_code(200,400,500))
