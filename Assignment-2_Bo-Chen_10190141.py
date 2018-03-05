"""
Bo Chen (10190141)
CISC 121 Assignment #2: Print Queue Simulator
July 24, 2017

This is a Python version 3.6 of the Print Queue Simulator.
This program simulates a printing queue. It has four major functions:
Job Submit, Print, Queue Contents, and Remove. 
It also reads in commands from online textfiles.
Detailed explination can be found here: https://goo.gl/Pwa1gw
"""
import urllib.request

"""
The commands() function follows the commands from the printsim.txt on the
CS.QUEENSU.CA webpage. It takes commands and runs specific fuctions based
on the action given.
"""
def commands():
    #flag to see if queue is empty
    flag = False
    response = urllib.request.urlopen("http://research.cs.queensu.ca/home/cords2/printsim.txt")
    for line in response:
        job = line.decode('utf-8').split()
        #run submit fuction
        if job[0] == 'submit':
            #checks if valid file type
            if (job[2] == 'pdf') or (job[2] == 'jpg') or (job[2] == 'docx') or (job[2] == 'pptx'):
                #if queue is empty, initilize a linked list
                if flag == False:
                    flag = True
                    node = {}
                    node['data'] = job[1:6]
                    node['next'] = None
                    head = node
                    print('Adding job',job[1],'to the queue. It will require',
                    time(head,job[1:6]),'seconds to process')
                else:
                    head = submitJ(head, job)
            else:
                print("File type'",job[2],"'not supported")
                continue
        #run queue fuction
        elif job[0] == 'queue':
            if flag == False:
                print("Nothing in que")
            queueJ(head, job)
        #run print fuction
        elif job[0] == 'print':
            if flag == False:
                print("Nothing to print")
            temp = printJ(head,job)
            #if queue is empty
            if temp == False:
                flag = False
            else:
                head = temp
        #run remove fuction
        elif job[0] == 'remove':
            if flag == False:
                print("Nothing in que")
            temp = removeJ(head, job)
            #if queue is empty
            if temp == False:
                flag = False
            else:
                head = temp
        else:
            continue

"""
The submitJ() fuction submits a job into the queue following the "shortest job first" algorithm.
It takes the head of the linked list and the current job being processed. It displayes the
current job ID number and the time--returned from time()--that is required to process it.  
"""
def submitJ(head, job):
    newNode = {}
    newNode['data'] = job[1:6]
    ptr = head
    print('Adding job',job[1],'to the queue. It will require',
    time(head,job[1:6]),'seconds to process')
    #"shortest job first" algorithm
    #if the shortest spot if the first node
    if time(head,ptr['data']) > time(head,job[1:6]):
        newNode['next'] = head
        head = newNode
        return head
    #if the shortest is not the first node
    else:
        while (ptr['next'] != None) and (time(head,ptr['next']['data']) < time(head,job[1:6])):
            ptr = ptr['next']
        newNode['next'] = ptr['next']
        ptr['next'] = newNode
        return head

"""
The queueJ() fuction prints the number of items currently in the queue along with the 
total estimated print time for all the jobs. It takes the head of the linked list and 
the current job being processed.   
"""
def queueJ(head, job):
    ptr = head
    counter = 0
    seconds = 0
    while ptr != None:
        a = time(head,ptr['data'])
        seconds = seconds + a
        counter = counter + 1
        ptr = ptr['next']
    print("Number of items currently in the queue:",counter,
    ". Total estimated print time for all these jobs:", seconds)

"""
The printJ() takes the next job off the queue and the prints the job ID. 
It takes the head of the linked list and the current job being processed.   
"""
def printJ(head, job):
    ptr = head
    print("Printing job",ptr['data'][0]) 
    head = head['next']
    #checks if linked list is empty
    if head == None:
        return False
    else:
        return head
        
"""
The removeJ() fuction removes a specific job based on the input ID. 
It takes the head of the linked list and the current job being processed.   
"""
def removeJ(head, job):
    print("File ID'",job[1],"'removed from queue")
    ptr = head
    #if taget is the first node
    if ptr['data'][0]==job[1]: #
        head = head['next']
    #if taget is the last node
    else:
        while ptr['next'] != None: 
            prew = ptr
            ptr = ptr['next']
        if ptr['data'][0]==job[1]:
            prev['next'] = None
            return head
    ptr = head
    #if taget is not the first or last node
    while ptr['next'] != None:
        if ptr['data'][0]==job[1]:
            ptr['data'] = ptr['next']['data'] 
            ptr['next'] = ptr['next']['next']
        ptr = ptr['next']
    #checks if linked list is empty
    if head == None:
        return False
    else:
        return head

"""
The time() fuction calculates the time needed to process the print job. 
It takes the head of the linked list and the current job being processed.   
"""
def time(head, job):
    seconds = 0
    if (job[1]) == "pdf":
        if job[3] == 'bw':
            seconds = int(job[2]) * 4
        else:
            seconds = int(job[2]) * 30
    elif job[1] == "jpg":
        if job[3] == 'bw':
            seconds = int(job[2]) * 10
        else:
            seconds = int(job[2]) * 60
    elif (job[1] == "docx") or (job[1] == "pptx"):
        if job[3] == 'bw':
            seconds = int(job[2]) * 6
        else:
            seconds = int(job[2]) * 20
    return seconds

"""
The main() fuction initates the program. 
"""
def main():
    commands()
main()
