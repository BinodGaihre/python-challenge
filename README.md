# python-challenge
# Overview
* The repository comprises two sections one for PyBank (Financial Records) and the other one PyPoll (Poll Data)
* Each of the section consists of the following
    >Files to access the data being used residing in resource folder.
    >Code files in order to calculate the metrices of the dataset provided.
    >Output files where the results is written residing in analysis folder.
* Visual studio code was used to for coding purposes
## About the Code
* Imported os to get the path of the file and the directory.
* Imported csv to read the exsiting resource file and write the result
* Used appropriate formulas to calculate the metrics like
    >increase/decrease in profit/loss, average change of profit/loss over a period of time etc for financial records in PyBank.
    >total vote counts, individual vote counts with their respective percentage of vote count for poll data in PyPoll.
### About the output
* For PyBank
    >Total months - The number of months with the profit/loss data.
    >Total - Sum of the overall profit/loss occured.
    >Average Change - The average of the total changes which happened over the months.
    >Greatest increase/decrease in profits - The highest amount of profit gained and the higest amount of profit lost.
* For PyPoll
    >Total Votes - Total number of votes casted.
    >List of the names of the candidate with their respective vote percentage and vote counts
    >Name of the Winner with the highest vote count.
