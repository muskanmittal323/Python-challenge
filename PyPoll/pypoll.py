#Author: Muskan Mittal
#Module 3 Challenge

import csv #Import csv module

with open ('election_data.csv') as csvfile: #Starting csv file handling

    csvreader=csv.reader(csvfile, delimiter=',') #Specifying delimiter and variable that holds the data
    header=next(csvreader) #Reading the header row first in the given dataset

    #Declaring variables
    voterIds=[] #Generating a list named "voterIds" for the "Voter ID" column
    county=[] #Generating a list named "counties" for the "counties" column
    candidates=[] #Generating a list named "candidates" for the "Candidate" column
    actualCandidateNames=[] #Generating a list for actual candidate names
    foundvoteCountPercent=[] #Generating a list for total votes for each found candidate
    printResult=[] #Generating a list for result printout of each found candidate
    voteCountPercent=[] #Generating a list for percentage of votes for each found candidate

    #Seteting the start conditions
    lc=0
    wvotes=0 # Vote counter for winning
    lvotes=0 # Vote counter for losing
    loop1=0
    loop2=0
    loop3=0
    loop4=0
    
     #loop for Reading every row of data after the header and writing the data into the assigned lists
    for row in csvreader:
        voterid=row[0] #Assigning column 0 as voterid
        counties=row[1] #Assigning column 1 as counties
        candidate=row[2] #Assigning column 2 as candidate
        voterIds.append(voterid) #Adding next line to list voterIds
        county.append(counties) #Adding next line to list counties
        candidates.append(candidate) #Adding next line to list candidates
    
    lc= len(voterIds) #Counting the total number of votes casted in the "Voter ID" column

#Beginning the data analysis

actualCandidateNames.append(candidates[0]) #Pre-loading the first candidate name for comparison process

#First loop: loop through the list of candidates to determine candidates voted for (assuming variable loop1 as loop index counter)
for loop1 in range (lc-1):
    if candidates[loop1+1] != candidates[loop1] and candidates[loop1+1] not in actualCandidateNames: # check condition
        actualCandidateNames.append(candidates[loop1+1])

n=len(actualCandidateNames)

#Second loop: Assuming variable loop2 as loop index counter
for loop2 in range (n): #Range of loop is assumed depending upon how many candidates were found in the first loop
    foundvoteCountPercent.append(candidates.count(actualCandidateNames[loop2])) #Counting the total votes of candidates and adding them to the list total

lvotes=lc #Pre-loading loservoters with the maximum votes for the < comparison

#Third loop: Assuming variable loop3 as loop index counter
for loop3 in range(n): #Range of loop is assumed depending on how many candidates were found in the first loop
    voteCountPercent.append(f'{round((foundvoteCountPercent[loop3]/lc*100), 3)}%') #Calculating the % per candidate found
    if foundvoteCountPercent[loop3]>wvotes: #Check condition for finding the candidate with the highest vote count
        winner=actualCandidateNames[loop3]
        wvotes=foundvoteCountPercent[loop3]
    if foundvoteCountPercent[loop3]<lvotes: #Check condition for finding the candidate with the lowest vote count
        loser=actualCandidateNames[loop3]
        lvotes=foundvoteCountPercent[loop3]

#Fourth loop: Assuming variable loop4 as loop index counter
for loop4 in range(n):
    printResult.append(f'{actualCandidateNames[loop4]}: {voteCountPercent[loop4]} ({foundvoteCountPercent[loop4]})') #Formatting the list printResult

resultlines='\n'.join(printResult) #Preparing a new combined list of results for printout (where each candidate with the result gets a new line)

#Prints the expected output lines in a specified format

analysis=f'\
Election Results\n\
----------------------------\n\
Total Votes: {lc}\n\
----------------------------\n\
{resultlines}\n\
----------------------------\n\
Winner: {winner}\n\
----------------------------\n'

print(analysis) #Prints results on the output screen

#Exporting a text file with the results into a file named pypollResult.txt

file1=open("pypollResult.txt","w") #Opening in write mode or if file does not exist then creating a file named pypollResult.txt
file1.writelines(analysis) #Writing the analysis Results into pypollResult.txt
file1.close() #Closing the pypollResult.txt in write mode