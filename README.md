This is a Python version 3.6 of the Print Queue Simulator.
This program simulates a printing queue. It has four major functions:
Job Submit, Print, Queue Contents, and Remove. 
It also reads in commands from online textfiles.

Assignment
"The goal of this assignment is to give you practice implementing and using linked lists.  You should begin by identifying the functions that you will need to write that will manipulate your linked lists. For instance, you will need a function to print the contents of the list, a function to add a new node to a list in the appropriate place, a function to remove a node from the head of the list etc.  Write these functions first and test them. Then integrate these functions into your program that implements the entire problem.    The most difficult part of the assignment will be keeping the queue in the correct sorted order.  You may wish to start this assignment by ignoring this requirement and just adding new jobs to the front of the queue.  

Jobs that are sent to the printer are printed one at a time.   If there are many jobs in the printer, the jobs must "queue", that is, wait in a line to be printed.    When a job arrives, it is put into the queue.  When a job finishes, the printer checks the queue to see if any jobs are waiting.  If so, it takes the next job off the queue and prints it. In this assignment, you are going to simulate this process.

Your queue will be a linked list with each node representing a job.   The "data" in the node will store the job id (an integer),  the number of pages to print, whether to print in color or black and white, the estimated time that the job will take (in seconds) and the data type of the file that is to be printed.  Your printer only prints files of the following types:  "docx", "pdf", "jpg", "pptx".  Other file types that are sent to the printer will be ignored and not added to the queue.

The scheduling algorithm that your printer uses is a "shortest job first" algorithm where the print queue is kept in sorted order according to the estimated length of the job.    Therefore, the shortest job will be at the head of the list and the longest job will be at the tail of the list.   The printer always chooses the job at the head of the queue to print next.   If two jobs have the same completion time, the job that arrived first should be ahead of the new job in the queue.

Print times are estimated  in the following manner:

pdf files:  30 seconds per page for colour, 4 seconds per page for black and white
pptx and  docx files:  20 seconds per page for colour, 6 seconds per page for black and white
jpg files:  60 seconds per page for colour, 10 seconds per page for black and white
When a job arrives for printing, it is added to the queue in the correct location based on its time estimate.   All (valid) jobs are put on the queue, even if nothing is currently printing.

When the printer selects a job from the queue for printing, it is removed from the queue.

The printer displays the number of jobs waiting in the queue on its LED display along with the total estimate time for all jobs in the queue. 

Your program will implement the above specifications.  The input for your program will be a file of jobs and commands that you will process which will "drive" your program.  The following indicates what should be done in each case:

Command1: Job Submit
An example of a new job is:

submit 101 pdf 16 bw  

The keyword submit indicates that the line is a new job that is being submitted.  Next is the (integer) id followed by the type of the file.  The file type will be one of "pdf", "docx", "pptx",  or "jpg".  Next is the number of pages (an integer).  The last value is either "bw" or "colour".  You will need to calculate the time estimate in your program.

After processing this line, your program should print "Adding job XXX to the queue.  It will require YYY seconds to process", where XXX is the job id and YYY is the processing time.

Command 2: Print
The print keyword indicates that the next job should be taken off the queue.   In response, your program should print "Printing job XXX" where XXX is the job id.   Your program does not need to account for print time – that is, if two print statements appear one after the other, you do not have to "wait" until the first job is printed.   If there is nothing in the queue to print, you should print "Nothing to print".

Command 3: Queue Contents
When you see a line that reads "queue contents", your program should print the number of items currently in the queue along with the total estimated print time for all these jobs.  This simulates the "LED" on the printer.

Command 4: Remove
Removes the print job from the queue.  This simulates a manual removal (ie. someone has canceled the job).

Reading from the Input File
The input file that you will use resides on a web page.  You will read a line of the web page (a command) and process the command, then read another line etc.    Here is some code to help get you started in reading the file:

import urllib.request    #this loads a library you will need.  Put this line at the top of your file.


def readHtml():
    response = urllib.request.urlopen("http://research.cs.queensu.ca/home/cords2/printsim.txt")
    html = response.readline()  #reads one line
    data = html.decode('utf-8').split()   #splits this line into a list of "tokens"  (print it to see what you get)
    #at this point you have a list representing this command ---
    #now take action depending on what the command is."
