#Import the required packages
import os
import csv

#Import the csv file
csvpath = os.path.join("Resources/budget_data.csv")

#Open the csv file
with open(csvpath, errors = "ignore") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Define the headings
    csv_header = next(csvreader)

    #Total Number of Months & Total Profit/Loss over the dataset period
    Number_of_Months = 0
    Total_PL = 0
    Months_list = []
    PL_list = []

    for row in csvreader:
        Number_of_Months = Number_of_Months + 1
        Total_PL = Total_PL + int(row[1])
        Months_list.append(row[0])
        PL_list.append(int(row[1]))

    #Average Change per Month + Min & Max Changes
    Change = 0
    Average_Change = 0
    Change_List = []
    Current_Max = 0
    Current_Min = 0

    for i in range(0, (len(PL_list) - 1)):
        Change = PL_list[(i + 1)] - PL_list[i]
        Average_Change = Average_Change + Change
        if (Change > Current_Max):
            Current_Max = Change
            Change_Max_Month = i + 1
        elif (Change < Current_Min):
            Current_Min = Change
            Change_Min_Month = i + 1

    Average_Change = Average_Change / (Number_of_Months - 1)

    #Format & Save Analaysis Lines
    line1 = "Financial Analysis"
    line2 = "----------------------------------"
    line3 = f'Total Months: {Number_of_Months}'
    line4 = f'Average Change: ${round(Average_Change, 2)}'
    line5 = f'Greatest Increase in Profits: {Months_list[Change_Max_Month]} (${Current_Max})'
    line6 = f'Greatest Decrease in Profits: {Months_list[Change_Min_Month]} (${Current_Min})'

    #List of lines
    lines = [line1, line2, line3, line4, line5, line6]

    #Print Analysis & Write results to a text file
    with open("analysis/output.txt", "w") as f:
        for line in lines:
            print(line)
            f.write(line)
            f.write('\n')
    