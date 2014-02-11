from sys import argv
import string

script, textfile = argv

test = open(textfile)
# TO-DO: Check if you really need this
readfile = test.read()

# Use split function to separate words followed by a space
# Convert all letters to lowercase 
# Use strip function to strip punctuation
# Initiate empty dictionary and that will store unique words and count

# Formatting characters to lower case, split to list, and remove puncutation
readfile = readfile.lower()
dash_word_string = readfile.replace("--"," ")
# Separate readfile string into a list
underscore_word_string = dash_word_string.replace("_", " ")
word_list = underscore_word_string.split()

test.close()


# TO DO ask if it's removing ---- --hello-- because of looping? 

format_list = []
for word in word_list:
    stripped_new_word = word.strip(string.punctuation)
    format_list.append(stripped_new_word)


# If item is not in dictionary, create a new key entry. If not, add 1 to the existing entry
word_dict = {}
# TO DO ask if better way than nested for loops
# iterate through list and check against dictionary to see if item in there, if not create new, if so, add one
for word in format_list:
    word_dict[word] = word_dict.get(word, 0) + 1


rev_dict = {}
for key, value in word_dict.iteritems():
    if rev_dict.get(value) != None: #if it sin there, append to the list of the value in rev_dict
        rev_dict[value].append(key)
    else: # if not in there, create a new key in rev_dict
        rev_dict[value] = [key]

    # if new_dict.get(value) != None:
    #     new_dict[value] = new_value_list.append(word)
    # else: 
    #     new_dict[value] = key

desc_ord_list = sorted(rev_dict.keys(), reverse = True)
for item in desc_ord_list:
    print "%s %s" % (item, rev_dict[item])
