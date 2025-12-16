input_file_handle = open("all.txt", "r")              # open the file
input_string = input_file_handle.read()                        # slurp it all in as one string
input_string = input_string.lower()                            # lower-case it

for punctuation_mark in '!"#$%&\'()*+,-./:;<=>?@[\\^_`{|}~':   # replace all punctuation mark (no
    input_string = input_string.replace(punctuation_mark, "")  # good really as this'll turn "don't"
                                                               # into "dont"; see Perl book page
                                                               # pp. 39-40 for a better way using
                                                               # 'split')
tokencount=0                                           # initialize an integer to count tokens
word_frequencies = {}                                  # and a dict to hold the type,count pairs

for word in input_string.split():                       # split input_string on whitespace, iterate
    tokencount += 1                                     # through the resulting list of words
    if not word in word_frequencies:                    # and either create with value 1 a dictionary
        word_frequencies[word] = 1                      # key for each word or if the key exists
    else:                                               # then increment that key's value
        word_frequencies[word] += 1                     # (this is equivalent to the 'set' method
                                                        # that Bryan uses to get types from tokens)

print ("Types:", len(word_frequencies))
print ("Tokens:", tokencount)

flipped_dict_list=[]                                    # because we can't sort a dict on its values
                                                        # we need a list of tuples to hold key,value
                                                        # pairs flipped to value,key pairs and then
                                                        # we can sort that list
            
for key,value in word_frequencies.items():  # iterate thru the list of tuples (one per key,value
    flipped_dict_list.append((value,key))   # pair) that is returned by the .items method applied 
                                            # to the dict and append (in reversed order as value,key)
                                            # that tuple to our new, flipped list

flipped_dict_list=sorted(flipped_dict_list, reverse=True)   # sort the new list on its key (which
                                                            # is the dict's value)

for key, value in flipped_dict_list:                        # and then iterate thru the new list
    print(key, ":", value)                                  # printing out its tuples
