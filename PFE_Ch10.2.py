
#### PFE - Assignment Chapter 10.2 ####
#### Stephen M. Baum ####

# Write a program to read through the mbox-short.txt 
# and figure out the distribution by hour of the day for 
# each of the messages. You can pull the hour out from the 
# 'From ' line by finding the time and then splitting the 
# string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print 
# out the counts, sorted by hour as shown below.

# open the file
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fn = open(name)

# we will fill these later
hcount = dict() 
hlst = []

# here is the main loop itself
for line in fn:
    words = line.split()
    if len(words) > 2 and words[0] == 'From': # only selecting the "From" lines
        hr = words[5].split(':') # split based on the colon
        hcount[hr[0]] = hcount.get(hr[0], 0) + 1 # take the first item (the hour)
    else: # or, move on
        continue

# update and sort the list itself
for k,v in hcount.items():
    hlst.append((k,v))
    
hlst.sort()
for k,v in hlst:
    print(k,v)
