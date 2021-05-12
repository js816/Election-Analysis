# PyPoll with Python

## Overview of Project

Tom, with the Colorado Board of Elections, and I worked together to analyze the results of a recent congressional election.  He provided a [CSV file](https://github.com/js816/Election-Analysis/blob/main/Resources/election_results.csv) with all votes cast in the election and Python code was developed to evaluate the votes. The tasks to complete were:

1. Calculate the total number of votes cast
2. Get a list of candidates who received votes
3. Calculate the number of votes received by each candidate
4. Calculate the percentage of votes each candidate received
5. Determine the winner of the election based upon popular vote
6. Get a list of counties where votes were cast for this election
7. Calculate the number of votes cast from each county
8. Calculate the percentage of votes cast from each county
9. Determine which county cast the highest number of votes in this election

The data were then outputted to both the terminal and a [text file](https://github.com/js816/Election-Analysis/blob/main/analysis/election_results.txt).

## Election-Audit Results

- A total of 369,711 votes were cast in this congressional election.
- Votes were cast from three different counties.  

![County_Votes](https://user-images.githubusercontent.com/82730954/118051768-2c2b0980-b347-11eb-8b1e-b4d62e3055da.PNG)

- The county that cast the highest number of votes in this election was Denver County (306,055 votes, 82.8% of the votes cast).
- Three candidates received votes in this election.

![Candidate_Votes](https://user-images.githubusercontent.com/82730954/118051791-364d0800-b347-11eb-94a0-980d48da604e.PNG)
	
- Diana DeGette won the election with 272,892 votes, 73.8% of votes cast.

## Election Audit Summary

The script developed for this project could be useful to the election board to evaluate future elections.  The code was developed to be versatile to accommodate and accurately track votes cast for any number of candidates and votes cast from any number of counties.  As long as the election_results.csv file had the same data using the same data layout, the analysis could be easily accomplished.

For some scenarios, additional development could also allow for other use cases.  For example, in school board elections if multiple seats are open and a certain number are elected, the code could be adapted to identify those receiving the highest number of votes.  

Additionally, the script could be adapted to analyze other election types such as proposed amendments and questions where votes are cast either for or against the proposal.  With development, the scripting could analyze and report if the proposal was approved or rejected. As some may require a certain percentage of votes (such as 2/3rds of the votes cast), we could discuss all potential use cases.

I would be happy to meet to discuss further use cases where this code could be beneficial to the election board.
