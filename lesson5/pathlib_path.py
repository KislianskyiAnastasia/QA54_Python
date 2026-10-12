from pathlib import Path

deta_folder = Path("data_test")
file_path = deta_folder/"test.csv"
print(file_path)
print(file_path.exists())

screen_folder = Path("screen")
screen_folder.mkdir(exist_ok=True)
reports_folder = Path("reports")/"october" #Path("reports/october")
reports_folder.mkdir(parents=True,exist_ok=True)