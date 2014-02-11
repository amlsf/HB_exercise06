from sys import argv
import string

script, textfile = argv

test = open(textfile)
readfile = test.read()

# Formatting characters to lower case 
readfile = readfile.lower()

#Formatting replace -- with space to later split to diff words in step after next
dash_word_string = readfile.replace("--"," ")

# Formatting to replace underscore with space to later split to another word in list in next step
underscore_word_string = dash_word_string.replace("_", " ")

# Separate readfile string into a list separated. no argument defaults to spaces and /n /t
word_list = underscore_word_string.split()

test.close()


# TO DO ask if it's removing ---- --hello-- because of looping? (no that's how strip works, all leading, trailing punct)
# strips out punctuation
format_list = []
for word in word_list:
    stripped_new_word = word.strip(string.punctuation)
    format_list.append(stripped_new_word)


# this creates a dictionary of words as keys and number of instaces as values (we had a for loop before but Nick showed us a shortcut)
# If item is not in dictionary, create a new key entry. If not, add 1 to the existing entry
word_dict = {}
# TO DO ask if better way than nested for loops
# iterate through list and check against dictionary to see if item in there, if not create new, if so, add one
for word in format_list:
    word_dict[word] = word_dict.get(word, 0) + 1


# this reverses the word_dict so values are keys and keys are values
rev_dict = {}
for key, value in word_dict.iteritems():
    if rev_dict.get(value) != None: #if it sin there, append to the list of the value in rev_dict
# no need for none, just truthy falsey
        rev_dict[value].append(key)
    else: # if not in there, create a new key in rev_dict
        rev_dict[value] = [key]

    # if new_dict.get(value) != None:
    #     new_dict[value] = new_value_list.append(word)
    # else: 
    #     new_dict[value] = key

# This sorts the keys in numerical descending order, and then orders the words in the value lists in alpha order
# How would you pull this out of the list? 
desc_ord_list = sorted(rev_dict.keys(), reverse = True)
for item in desc_ord_list:
    rev_dict[item].sort()
#   print "%s %s" % (item, rev_dict[item])
# TO DO print rev_dict[item].sort()
# print rev_dict['2']  (Why doesn't this print?) 

# TODO Can I do this without a nested for loop? Use a join function expression to replace inner for loop
for key in desc_ord_list:
    for i in range(len(rev_dict[key])):
        print key, rev_dict[key][i]
        i += 1