#Import the required packages
import os
import csv

#Import the csv file
csvpath = os.path.join("Resources/election_data.csv")

#Open the csv file
with open(csvpath, errors = "ignore") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Define the headings
    csv_header = next(csvreader)

    #Total Number of Votes, List of Unique Candidates
    Number_of_Votes = 0
    Candidates = []
    Candidate_Number = 0
    Votes = []

    for row in csvreader:
        Number_of_Votes = Number_of_Votes + 1
        if row[2] not in Candidates:
            Candidates.append(row[2])
            Votes.append(0)
        for i in Candidates:
            if (row[2] == i):
                Votes[Candidate_Number] = int(Votes[Candidate_Number]) + 1
            else:
                Candidate_Number = Candidate_Number + 1
        Candidate_Number = 0

    #Calculate Vote Percentages
    Percentages = []

    for j in Votes:
        Percentages.append(f'{round(((int(j) / Number_of_Votes) * 100), 3)}%')

    #Format & Save Analaysis Lines
    line1 = "Election Results"
    linebreak = "----------------------------------"
    line2 = f'Total Votes: {Number_of_Votes}'

    lines = [line1, linebreak, line2, linebreak]

    #Calculate & Append Election Results
    Highest_Votes = 0
    Winner = ""

    for k in range(0, len(Candidates)):
        line = f'{Candidates[k]}: {Percentages[k]} ({Votes[k]})'
        lines.append(line)
        if (Votes[k] > Highest_Votes):
            Highest_Votes = Votes[k]
            Winner = Candidates[k]
    
    lines.append(linebreak)
    lines.append(f'Winner: {Winner}')
    lines.append(linebreak)

    #Print Analysis & Write results to a text file
    with open("analysis/output.txt", "w") as f:
        for line in lines:
            print(line)
            f.write(line)
            f.write('\n')
