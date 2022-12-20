
#### PFE - Assignment Chapter 7.1 ####
#### Stephen M. Baum ####

# Write a program that prompts for a file name, 
# then opens that file and reads through the file, 
# and print the contents of the file in upper case. 
# Use the file words.txt to produce the output below.

fname = input("Enter the name of the file: ")
if len(fname) < 1:
    fname = "words.txt" # hit 'enter' - more smooth 
fh = open(fname)
for line in fh: # go over each line in fh
    line_cl = line.rstrip() # remove the white space from things
    line_up = line_cl.upper() # then, get stuff in uppercase
    print(line_up)