import csv
import os

records = 0

#open CSV
csvpath = "budget_data.csv"

#Create Lists
profitandloss = []
AvgChg = []
Changes = []
Months = []

#Read CSV
with open (csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Strip Hedings
    csv_header = next(csvreader)
    
    #Populate list with values and count the number of values pulled
    for row in csvreader:
        profitandloss.append(row[1])
        Months.append(row[0])
        records = len(profitandloss)

    #Sum net profit
    netprofit = sum((int(i) for i in profitandloss))
    
    #set starting pointer positions for monthly changes
    firstpointer = 0
    secondpointer = 1

    #Get Monthy changes
    for i in profitandloss:
        if secondpointer < records:
            Changes.append((int(profitandloss[secondpointer]) - int(profitandloss[firstpointer])))
            firstpointer = (firstpointer + 1)
            secondpointer = (secondpointer + 1)
       
    #find Average Change
    AvgChg = sum((int(c) for c in Changes)) / (records - 1)
    
        #Find Month with greatest changes
    BestChange = max(Changes)
    BestMonth = Changes.index(BestChange)
    WorstChange = min(Changes)
    WorstMonth = Changes.index(WorstChange)
       
#Print Results
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {records} ")
print(f"Total: ${netprofit}")
print(f"Average Change: ${'{:,.2f}'.format(AvgChg)}")
print(f"Greatest Increase in Profits: {Months[BestMonth + 1]} (${max(Changes)})")
print(f"Greatest Decrease in Profits: {Months[WorstMonth +1]} (${min(Changes)})")


#Create Text File and Print results to it
f= open("PyBank Results.txt","w")
f.writelines(f"Financial Analysis\n")
f.writelines(f"----------------------------\n")
f.writelines(f"Total Months: {records} \n")
f.writelines(f"Total: ${netprofit}\n")
f.writelines(f"Average Change: ${'{:,.2f}'.format(AvgChg)}\n")
f.writelines(f"Greatest Increase in Profits: {Months[BestMonth + 1]} (${max(Changes)})\n")
f.writelines(f"Greatest Decrease in Profits: {Months[WorstMonth +1]} (${min(Changes)})\n")
f.close() 