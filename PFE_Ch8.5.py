
#### PFE - Assignment Chapter 8.5 ####
#### Stephen M. Baum ####

# Open the file mbox-short.txt and read it line by line. 
# When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out 
# the second word in the line (i.e. the entire address of the 
# person who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'. 
# Also look at the last line of the sample output to see how to 
# print the count.

# read the file in
fname = input("Enter the file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
f = open(fname)

# set a count at the start
count = 0

for line in f: # go over each line
    lin_cl = line.strip().split() # strip of white space/split
    if lin_cl.startswith("From: "): # only look at "From: " lines
        print(lin_cl[1]) # print the email (the '1' position item)
        count = count + 1 # add to the count
    else: # else, continue on - we only care about "From: " emails
        continue

print("There were", count, "lines in the file with From as the first word")


