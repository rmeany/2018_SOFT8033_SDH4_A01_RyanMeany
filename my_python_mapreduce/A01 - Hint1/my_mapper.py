#!/usr/bin/python

# --------------------------------------------------------
#           PYTHON PROGRAM
# Here is where we are going to define our set of...
# - Imports
# - Global Variables
# - Functions
# ...to achieve the functionality required.
# When executing > python 'this_file'.py in a terminal,
# the Python interpreter will load our program,
# but it will execute nothing yet.
# --------------------------------------------------------

import sys
import codecs




# ------------------------------------------
# FUNCTION my_map
# ------------------------------------------
def my_map(input_stream, languages, num_top_entries, output_stream):
    list_of_tuples = []
    for text_line in input_stream:
        word_list = text_line.split(' ')
        lang = word_list[0]
        for x in range(0, languages.__len__()):
            if text_line.startswith(languages[x]):
                title = word_list[1]
                view = int(word_list[2])
                projVal = lang, title, view
                list_of_tuples.append(projVal)

    sorted_list = sorted(list_of_tuples, key=lambda x: (x[0], x[2]), reverse=True)

    lang_dict = dict()

    for line in sorted_list:
        if line[0] in lang_dict:
            # append the new number to the existing array at this slot
            array = (line[1], line[2])
            lang_dict[line[0]].append(array)
        else:
            # create a new array in this slot
            array = (line[1], line[2])
            lang_dict[line[0]] = [array]

    for key in lang_dict:
        for index in range(0, num_top_entries):
            if len(lang_dict[key]) > index:
                print(key, lang_dict[key][index])
                # output_stream.write(key+"\t"+str(lang_dict[key][index])+"\n")
                output_stream.write(
                    key + "\t(" + lang_dict[key][index][0] + "," + str(lang_dict[key][index][1]) + ")" + "\n")
    pass

# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(debug, i_file_name, o_file_name, languages, num_top_entries):
    # We pick the working mode:

    # Mode 1: Debug --> We pick a file to read test the program on it
    if debug == True:
        my_input_stream = codecs.open(i_file_name, "r", encoding='utf-8')
        my_output_stream = codecs.open(o_file_name, "w", encoding='utf-8')
    # Mode 2: Actual MapReduce --> We pick std.stdin and std.stdout
    else:
        my_input_stream = sys.stdin
        my_output_stream = sys.stdout

    # We launch the Map program
    my_map(my_input_stream, languages, num_top_entries, my_output_stream)

# ---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
# ---------------------------------------------------------------
if __name__ == '__main__':
    # 1. Input parameters
    debug = True

    i_file_name = "pageviews-20180219-100000_0.txt"
    o_file_name = "mapResult.txt"

    languages = ["en", "es", "fr"]
    num_top_entries = 5

    # 2. Call to the function
    my_main(debug, i_file_name, o_file_name, languages, num_top_entries)
