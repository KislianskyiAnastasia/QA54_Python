#======================1==================
import csv


def save_test_ids(test_ids):
    with open("tests.txt","w",encoding="utf-8") as file:
        for test_ids in test_ids:
            file.write(test_ids + "\n")

save_test_ids(["QA-1001", "QA-1002", "QA-1003"])

def add_test_id(test_id):
    with open("tests.txt","a",encoding="utf-8") as file:
        file.write(test_id + "\n")

add_test_id("QA-1004")

def load_test_ids(filename):
    test_ids = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            test_id = line.strip()

            if test_id:
                test_ids.append(test_id)

        return test_ids
result = load_test_ids("tests.txt")
print(result)


#=====================2=======================

with open("results.csv","w",encoding="utf-8") as file:
    file.write("test_id,status,duration_ms\n")
    file.write("QA-1001,PASSED,120\n")
    file.write("QA-1002,FAILED,230\n")
    file.write("QA-1003,PASSED,150\n")

def get_test_statistics(filename):
    total = 0
    passed = 0
    failed = 0
    total_duration_ms = 0
    failed_ids = []

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += 1
            total_duration_ms += int(row["duration_ms"])

            if row["status"] == "PASSED":
                passed += 1

            if row["status"] == "FAILED":
                failed += 1
                failed_ids.append(row["test_id"])

    result = {
        "total": total,
        "passed": passed,
        "failed": failed,
        "total_duration_ms": total_duration_ms,
        "failed_ids": failed_ids
    }
    return result

print(get_test_statistics("results.csv"))



