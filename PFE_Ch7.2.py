
#### PFE - Assignment Chapter 7.2 ####
#### Stephen M. Baum ####

# Write a program that prompts for a file name, 
# then opens that file and reads through the file, 
# looking for lines of the form:
 # X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point 
# values from each of the lines and compute the average 
# of those values and produce an output as shown below. 
# Do not use the sum() function or a variable named 
# sum in your solution.

# open the file 
fname = input("Enter the file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt" # this is the file name
fh = open(fname)

# create two variables that will be useful
count = 0 # this will populate with the N
total = 0.0 # this is the total (not the sum hehe)

# write code to look through the file
for line in fh:
    line = line.strip() # remove all white space
    if line.startswith("X-DSPAM-Confidence:"): # only for lines that start with this weirdness
        count = count + 1 # the count is just the total N
        total = total + float(line[20:]) # the total is more complex - it is the sum of all of floating point values
    else: # remember, we are skipping lots of lines
        continue
print("Average spam confidence:", float(total/count)) # this will print things out in desired format


