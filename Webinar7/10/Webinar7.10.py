# from pathlib import Path
# def create_test_report(project_name,tester_name,passed,failed):
#     project_folder = Path("reports") / project_name
#     project_folder.mkdir(parents=True, exist_ok=True)
#     total = passed + failed
#     if failed  == 0:
#         status = "passed"
#     else:
#         status = "failed"
#     file_path = project_name / "reports.txt"
#     with open(file_path,"w") as file:
#         file.write(f'''
# Project : Testlink
# Tester: Anastasia
# Passed tests : 88
# Failed tests : 22
# Total tests :110
# ''')
# create_test_report("Testlink","Anastasia",88,22)
from pathlib import Path

ROOT_FOLDER: str = "reports"
REPORT_FILE_NAME: str = "report.txt"


def create_test_report(project_name: str, tester_name: str, passed: int, failed: int) -> None:
    project_path = Path(ROOT_FOLDER) / project_name
    project_path.mkdir(exist_ok=True, parents=True)

    with open(project_path / REPORT_FILE_NAME, "w", encoding="utf-8") as file:
        file.write(f"Project: {project_name}\n")
        file.write(f"Tester: {tester_name}\n")
        file.write(f"Passed tests: {passed}\n")
        file.write(f"Failed tests: {failed}\n")
        file.write(f"Total tests: {failed + passed}\n")


create_test_report("Phonebook", "Anna", 18, 2)