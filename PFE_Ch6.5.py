
#### PFE - Assignment Chapter 6.5 ####
#### Stephen M. Baum ####

# Write code using find() and string slicing (see section 6.10) 
# to extract the number at the end of the line below. 
# Convert the extracted value to a floating point number 
# and print it out.

text = "X-DSPAM-Confidence:        0.8475"
start = text.find('0') # this starts where the '0' is
end = text.find('5') # this ends where the '5' is
print(start, end) # confirms that these are far out lines

dec = text[start: end+1] # this isolates the value of interest
print(float(dec)) # prints the float
