from sys import argv
import string

script, textfile = argv

test = open(textfile)
# TO-DO: Check if you really need this
readfile = test.read()

# Separate readfile string into a list
# Use split function to separate words followed by a space
# Convert all letters to lowercase 
# Use strip function to strip punctuation
# Initiate empty dictionary and that will store unique words and count

# Formatting characters to lower case, split to list, and remove puncutation
readfile = readfile.lower()
word_list = readfile.split()

# TO-DO Ask instructors if there is a better way? (twain.txt is messy, lots of punct)
# TO-DO Check to see if punct is grouped together in ascii table, google comprehensive punct pack?

# TO-DO Puncutation

# format_list = []

"""
write a function
TO-DO ask if there is a way to do this without nested for loop
punctuation = [",", '.', '[', ']', '"', '(', ')', ':', ';', '?', '!', "'"]

for word in word_list:
    new_word = 

print format_list
"""

# If item is not in dictionary, create a new key entry. If not, add 1 to the existing entry
word_dict = {}

# TO DO ask if better way than nested for loops
# iterate through list and check against dictionary to see if item in there, if not create new, if so, add one
for word in word_list:
     # need to change this format_list once fixed
        if word_dict.get(word) != None:
            word_dict[word] += 1
        else: 
            word_dict[word] = 1

for key, value in word_dict.iteritems():
    print str(key) + ' ' + str(value)

test.close()