
#### PFE - Assignment Chapter 9.4 ####
#### Stephen M. Baum ####

# Write a program to read through the mbox-short.txt 
# and figure out who has sent the greatest number of 
# mail messages. The program looks for 'From ' lines 
# and takes the second word of those lines as the person 
# who sent the mail. The program creates a Python dictionary 
# that maps the sender's mail address to a count of the number 
# of times they appear in the file. After the dictionary is 
# produced, the program reads through the dictionary using a 
# maximum loop to find the most prolific committer.

# open the file
fname = input("Enter name of the file: ")
if len(fname) < 1:
    fname = 'mbox-short.txt'
fn = open(fname)

# create a dictionary that will populate later on
big = dict()

# create a dictionary
for line in fn:
    line = line.rstrip() # take away the white space
    if not line.startswith("From: "):
        continue # we are skipping non-"From: " lines
    words = line.split() # split string into a list
    big[words[1]] = big.get(words[1],0) + 1 # takes words, goes through all emails, and counts times email appears

# we will fill these in later - placeholders for now
big_name = None
big_num = None

# the final bit of critical code
for key, value in big: # this goes through the key/value pairs (key - name, value = #)
    if big_num is None or value > big_num: # if the value is bigger than what we've seen...
        big_num = value # it is the new value
        big_name = key # and has a corresponding new name
print(big_name, big_num) # print out the correct answer



