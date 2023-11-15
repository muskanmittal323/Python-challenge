#Author: Muskan Mittal
#Module 3 Challenge

#Importing csv module
import csv

with open ('budget_data.csv') as csvfile: #Starting csv file handling

    csvFilereader=csv.reader(csvfile, delimiter=',') #Specifying delimiter and variable that holds the data
    headerRow=next(csvFilereader) #Reading the header row first in the given dataset

    #Declaring variables
    months=[] #Generating list named "months" for the "Date" column
    proflosses=[] #Generating list named "proflosses" for the "Profit/Losses" column

    #Setting the start conditions
    totalamt=0
    avgChange=0
    monChange=0
    monCount=0
    Inc=0
    Dec=0
    IncA=0
    DecB=0
    loopA=0
    loopB=0

    #loop for Reading every row of data after the header and writing the data into the assigned lists
    for row in csvFilereader:
        month=row[0] #Assigning column 0 as month
        profloss=row[1] #Assigning column 1 as profloss
        months.append(month) #Adding next line to list months
        proflosses.append(profloss) #Adding next line to list prolosses
    
    m_count = len(months) #Count the total of months in the "Date" column

#Begining the data analysis

# Firts Loop: loop through the list proflosses (Assumming variable loopA as loop index counter)
for loopA in range (m_count):
    totalamt=totalamt+int(proflosses[loopA]) #Calculating the total amount


# Second Loop: loop through list proflosses (Assumming variable loopB as loop index counter)
for loopB in range (m_count-1): #Restricting the loop to avoid overflow (last line +1)
    avgChange=avgChange+(float(proflosses[loopB+1])-float(proflosses[loopB])) #Calculating sum of changes

    monChange=(float(proflosses[loopB+1])-float(proflosses[loopB])) #Calculating the monthly change

    if monChange>Inc: #Checking the condition for greatest increase
        Inc=monChange
        IncA=loopB
    else:
        Inc=Inc



    if monChange<Dec: #Checking the condition for greatest decrease
        Dec=monChange
        DecB=loopB
    else:
        Dec=Dec


#Prints the expected output lines in a specified format

analysis=f'\
Financial Analysis\n\
----------------------------\n\
Total Months: {m_count}\n\
Total: ${totalamt}\n\
Average Change: ${round(avgChange/(m_count-1),2)}\n\
Greatest Increase in Profits: {months[IncA+1]} (${int(Inc)})\n\
Greatest Decrease in Profits: {months[DecB+1]} (${int(Dec)})\n'

print(analysis) #Prints results on the output screen

#Exporting a text file with the results into a file named pybankResult.txt

file1=open("pybankResult.txt","w") #Opening in write mode or if file does not exist then creating a file named pybankResult.txt
file1.writelines(analysis) #Writing the analysis Results into pybankResult.txt
file1.close() #Closing the pybankResult.txt in write mode