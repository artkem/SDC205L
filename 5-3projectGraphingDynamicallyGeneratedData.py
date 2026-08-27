import datetime
import os
import openpyxl
from openpyxl.chart import BarChart, LineChart, Reference

#sets student id as variable for menu header and chart title
student_id = "ArtKem2260"
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

#function: createChart
#Required arguments: csv_file_path (str), chart_type (str)
# Expected return value: None
# Reads CSV data, writes it into final.xlsx with openpyxl, and builds a LineChart or BarChart
def createChart(csv_file_path, chart_type):
    try:

        #ask the user which column of data they want to chart
        print("Choose the data source to generate:")
        print("1 Fahrenheit")
        print("2 Celsius")
        data_choice = input()


        #read the csv rows and split the values
        file = open(csv_file_path, "r")
        lines = file.readlines()
        file.close()


        #create a new openpyxl workbook and get active sheet
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Data"


        # set up proper headers based on user choice
        if data_choice == "1":
            unit_label = "Farenheit"
            data_col_index = 1
        else:
            unit_label = "Celsius"
            data_col_index = 2


        ws.append(["Date", unit_label])
        #write each record into the Excel sheet with proper type casting
        for line in lines:
            parts = line.strip().split(",")
            if len(parts) >= 3:
                date_val = parts[0]
                temp_val = float(parts[data_col_index])
                ws.append([date_val, temp_val])


        # choose the chart type
        if chart_type.lower() == "bar":
            chart = BarChart()
        else:
            chart = LineChart()

        #set chart title and axis labels
        today_date = datetime.date.today().strftime("%m/%d/%Y")
        chart.title = f"{student_id} {today_date}"
        chart.x_axis.title = "Date"
        chart.y_axis.title = unit_label

        #define data values and date categories
        total_rows = len(ws["A"])
        data_ref = Reference(ws, min_col=2, min_row=1, max_row=total_rows)
        cats_ref = Reference(ws, min_col=1, min_row=2, max_row=total_rows)

        chart.add_data(data_ref, titles_from_data=True)
        chart.set_categories(cats_ref)

        #place chart on the sheet and save the workbook
        ws.add_chart(chart, "D2")
        wb.save("final.xlsx")
        print("Chart successfully generated and saved to final.xlsx")

    except Exception as e:
        print("Error creating chart:", e)

#function: generateReport
#required arguments: csv_file_path (str)
# expected return value: None
#prompts the user for a chart type and call createChart with the file path
def generateReport(csv_file_path):
    print("Which graph type would you like to create?")
    print("Type 'line' or 'bar':")
    chosen_type = input()
    createChart(csv_file_path, chosen_type)

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
    elif choice == "3":
        generateReport(data_file_path)
else:
    #handle inputs outside of 1,2,3
    print("Error: Invalid choice selected.")

