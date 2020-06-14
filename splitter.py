#!/usr/bin/python
import argparse
import math

# initialize variables
counter = 0
filename = "file.txt"
limitlanes= 50
newfiles=1


# create parser
parser = argparse.ArgumentParser()

# add arguments to the parser
parser.add_argument('-f','--filename', type=str, help=' specify the name of the file that must be splitted. default value "file.txt"')
parser.add_argument('-l','--maxlines', type=int, help=' specify number of lines where the document must be splitted. default value 50')
parser.add_argument('-o','--outputfiles', type=int, help=' specify number final files do you want to have. This option will invalidate the option of splitting the document by line numbers. The lines in each new file will be divided automatically.')

# parse the arguments
args = parser.parse_args()

# get the arguments value
if args.filename :
    filename = args.filename 
    print("Will process {}".format(filename))
if args.maxlines :
     limitlanes = args.maxlines 
     print("Splitting the file every {} lanes".format(limitlanes))
if args.outputfiles :
     number_of_lines = len(open(filename).readlines(  ))
     limitlanes = math.ceil(number_of_lines/args.outputfiles)
     print("Splitting the file in {} files".format(limitlanes))

# Start reading the file

with open(filename) as file_in:
    f = open(str("splitted{}.txt").format(str(newfiles)), "a")
    for line in file_in:
        f.write(line)
        counter+=1
        # When the number of lines reach a split point create a new document. 
        if counter%limitlanes == 0:
            f.close()
            newfiles+=1
            f = open(str("splitted{}.txt").format(str(newfiles)), "a")
    # If there are any remaining lines create a new document. 
    if f:
        f.close()
        newfiles+=1
    # Show operations result. 
print ("============================================================")
print ("                  SPLITTING HAS FINISHED                    ")
print ("============================================================")
print ("                     SUMMARY OF THE JOB                     ")
print ("                  From File: {}".format(filename))
print ("                  Limit of Lanes per file: {}".format(limitlanes))
print ("                  Total of lines {}".format(counter))
print ("                  Total new files: {}".format(newfiles-1))
print ("============================================================")
