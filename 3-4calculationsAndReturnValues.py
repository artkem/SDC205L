import datetime

def convertData(val):
    #perform temperature conversion (F to C)
    return (val - 32) * (5 / 9)

def getInput():
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
        # Function: convertData
        # Argument required: val_input (float) representing raw numerical input
        # Expected return value: converted float value
        converted_val = convertData(val_input)

        #display the timestamp at which this specific record is recorded
        print(f"The following was saved at {datetime.datetime.now()} :")
        #print the comma-separated output: Data, Raw value, Converted value
        print(f"{date},{int(val_input) if val_input.is_integer() else val_input},{converted_val}")
        




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
        getInput()
else:
    #handle inputs outside of 1,2,3
    print("Error: Invalid choice selected.")

