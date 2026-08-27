import datetime
import os

# sets the reference path for our csv file
data_file_path = "ZooData.csv"


def convertData(val):
    #perform temperature conversion (F to C)
    return (val - 32) * (5 / 9)
# opens or creates a csv file in append mode and writes a line of data
def insertData(csv_file_path, data_string):
    try:
        file = open(csv_file_path, "a")
        file.write(data_string + "\n")
        file.close()
    except Exception as e:
        print("Error writing to file:", e)
# reads the csv file and prints it location and contents        
def viewData(csv_file_path):
    try:
        # gets the full path to show where the file is
        full_path = os.path.abspath(csv_file_path)
        print("The file {full path}")
        file = open(csv_file_path, "r")
        contents = file.read()
        print(contents, end="")
        file.close()
    except Exception as e:
        print("Error reading file:", e)
#gets user input, converts the temp, and saves each entry to the csv
def getInput(csv_file_path="ZooData.csv"):
    '''
    #handles user interaction for data entry:
    #promps for the number of entries.
    #Loops to collect date and measurement inputs
    #Calls converdata to perform calculation
    #Prints confirmation of saved data with the current timestamp.
    '''
    # Ask the user for the total count of data records to enter
    print("How many entries are you inputting?")
    num_entries = int(input())  

    # Iterate through the requested number of data entries
    for _ in range(num_entries):
        # Prompt for entry date
        print("Enter a date:\n")
        date = input()

        #Prompt for numerical input value 
        print("Enter the highest temp for the inputted date: ")
        val_input = float(input())

        converted_val = convertData(val_input)

        if val_input.is_integer():
            temp_display = int(val_input)
        else:
            temp_display = val_input

        row = f"{date},{temp_display},{converted_val}"

        try:
            insertData(csv_file_path, row)
            now = datetime.datetime.now()
            print(f"The following was saved at {now}")
            print(row)
        except Exception as e:
            print("Could not save entry:", e)
            

#Main application flow
#set student id for menu header
student_id = "ArtKem2260"
#print header and instructions
print(f"{student_id}'s Spreadsheet Automation Menu")
print("Choose a number from the following options")
#define menu options with a list data structure
menu_options = ["1 Input Data", "2 View Current Data", "3 Generate Report"]
#display menu option to the console using a for loop
for option in menu_options:
    print(option)
#capture user input
choice = input()
#list recognized menu options for basic validation
valid_choices = ["1", "2", "3"]
# validate whether input exists within allowed options
if choice in valid_choices:
    current_time = datetime.datetime.now()
    #print acknowledgement containing user selection and exact current timestamp
    print(f"You selected {choice} at {current_time}")
    #check if selected option is available for execution
    if choice == "1":
        getInput(data_file_path)
    elif choice == "2":
        viewData(data_file_path)
else:
    #handle inputs outside of 1,2,3
    print("Error: Invalid choice selected.")

