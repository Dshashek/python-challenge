import csv
import os

records = 0

#open CSV
csvpath = "election_data.csv"


#Create Lists
votes = []
votetotals = []
candidates = []
candidatevotes = []
candidatepercent = []

#Read CSV
with open (csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Strip Hedings
    csv_header = next(csvreader)

    #Put Votes in a list    
    for row in csvreader:
        votes.append(row[2])

    #Get Candidates
    for candidate in votes: 
        if candidate not in candidates:
            candidates.append(candidate) 

    #Get Votes for each Candidate
    counter = 0
    for candidate in candidates:
            items = votes.count(candidates[counter])
            candidatevotes.append(items)
            counter = counter + 1

    #Get total votes
    totalvotes = len(votes)

    #Get % for each candidate
    counter = 0
    for candidate in candidates:
        percentages = "{:.3%}".format(candidatevotes[counter] / totalvotes)
        candidatepercent.append(percentages)
        counter = counter + 1

    #Find the Candidate with the most votes
    winnerTotal = max(candidatevotes)
    winnerLoc = candidatevotes.index(winnerTotal)
    winner = candidates[winnerLoc]

#Print Results to the Terminal
counter = 0
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {totalvotes}")
print(f"-------------------------")
for candidate in candidates:
    print(f"{candidates[counter]}: {candidatepercent[counter]} ({candidatevotes[0]})")
    counter = counter + 1
print(f"-------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")

#Create Text File and Print results to it
counter = 0
f= open("PyPol Results.txt","w")

f.writelines(f"Election Results\n")
f.writelines(f"-------------------------\n")
f.writelines(f"Total Votes: {totalvotes}\n")
f.writelines(f"-------------------------\n")
for candidate in candidates:
    f.writelines(f"{candidates[counter]}: {candidatepercent[counter]} ({candidatevotes[0]})\n")
    counter = counter + 1
f.writelines(f"-------------------------\n")
f.writelines(f"Winner: {winner}\n")
f.writelines(f"-------------------------\n")
f.close() 
