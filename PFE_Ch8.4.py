
#### PFE - Assignment Chapter 8.4 ####
#### Stephen M. Baum ####

# Open the file romeo.txt and read it line by line. 
# For each line, split the line into a list of words 
# using the split() method. The program should build a 
# list of words. For each word on each line check to see 
# if the word is already in the list and if not append 
# it to the list. When the program completes, sort and 
# print the resulting words in python sort() order as 
# shown in the desired output.

# open the file
fname = input("Put the file name here: ")
if len(fname) > 1:
    fname = "romeo.txt"
f = open(fname)

# create an empty list
lst = []

# go through all the text
for line in f: # read each line
    words = line.split() # split the line into a list of words
    for w in words: # go through each word
        if w not in words: # if the word is not in the list
            lst.apppend(w) # add it to the list
        lst.sort() # sort the list
print(lst) # print the list

