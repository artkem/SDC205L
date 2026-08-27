import datetime

student_id = "ArtKem2260"

print(f"{student_id}'s Spreadsheet Automation Menu")
print("Choose a number from the following options")

menu_options = ["1 Input Data", "2 View Current Data", "3 Generate Report"]

for option in menu_options:
    print(option)

choice = input()

valid_choices = ["1", "2", "3"]

if choice in valid_choices:
    current_time = datetime.datetime.now()
    print(f"You selected {choice} at {current_time}")
else:
    print("Error: Invalid choice selected.")

