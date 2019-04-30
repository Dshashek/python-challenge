import csv
import os

records = 0

#open CSV
csvpath = "election_data.csv"


#Create Lists
votes = []
candidates = []

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

    #Total Votes for Each Candidate
    totalVotes = len(votes)
    votes1 = votes.count(candidates[0])
    votes2 = votes.count(candidates[1])
    votes3 = votes.count(candidates[2])
    votes4 = votes.count(candidates[3])

    #Calculate Percentage for Each Candidate
    percent1 = "{:.3%}".format(votes1 / totalVotes)
    percent2 = "{:.3%}".format(votes2 / totalVotes)
    percent3 = "{:.3%}".format(votes3 / totalVotes)
    percent4 = "{:.3%}".format(votes4 / totalVotes)

    #Put Candidates/Votes in a Dictionary
    results = {
        votes1:candidates[0],
        votes2:candidates[1],
        votes3:candidates[2],
        votes4:candidates[3]
    }

    #Find the Winner's Name from the Dictionary
    winnerTotal = (max(results))

    for votes, name in results.items():
        if votes == winnerTotal:
            winner = name

#Print Results to the Terminal
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {totalVotes}")
print(f"-------------------------")
print(f"{candidates[0]}: {percent1} ({votes1})")
print(f"{candidates[1]}: {percent2} ({votes2})")
print(f"{candidates[2]}: {percent3} ({votes3})")
print(f"{candidates[3]}: {percent4} ({votes4})")
print(f"-------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")

#Create Text File and Print results to it
f= open("PyPol Results.txt","w")

f.writelines(f"Election Results\n")
f.writelines(f"-------------------------\n")
f.writelines(f"Total Votes: {totalVotes}\n")
f.writelines(f"-------------------------\n")
f.writelines(f"{candidates[0]}: {percent1} ({votes1})\n")
f.writelines(f"{candidates[1]}: {percent2} ({votes2})\n")
f.writelines(f"{candidates[2]}: {percent3} ({votes3})\n")
f.writelines(f"{candidates[3]}: {percent4} ({votes4}))\n")
f.writelines(f"-------------------------\n")
f.writelines(f"Winner: {winner}\n")
f.writelines(f"-------------------------\n")
f.close() 
