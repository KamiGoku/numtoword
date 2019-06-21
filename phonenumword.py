import numpy as np

sample = "15128670987";
s_len = len(sample);

inputeng = "1800painter";
inputnum = "18007246837";

List = [];
#N = 2000; #Dictionary line number

def txt_to_num(str):
    if str in "abc":
        return "2"
    elif str in "def":
        return "3"
    elif str in "ghi":
        return "4"
    elif str in "jkl":
        return "5"
    elif str in "mno":
        return "6"
    elif str in "pqrs":
        return "7"
    elif str in "tuv":
        return "8"
    else:
        return "9"

def look_up_dict(str):
    result = [];
    with open('translateddictionary.txt',"r") as dictionary:
        for index, line in enumerate(dictionary,0):
            if str in line:
                result.append(index);
    dictionary.closed
    return result;

def loop_through(str1,str2):
    if not str2: #check for empty string
        return;        
    else:
        for i in range(len(str2)):
            indexes = look_up_dict(str2[0:i]+"\n");#find index of matching number strings
            ##if not indexes: #not found in dict
            str1_new = str1 + str2[0:(i+1)];#add first 0 to i characterss
            str2_new = str2.replace(str2[0:(i+1)], '', 1); #remove first 0 to i characters
            loop_through(str1_new,str2_new);
            if indexes: #found in dict
                words = [];
                with open('dictionary.txt',"r") as f:#find the words based on the index
                    lines=f.readlines();
                    words = [lines[idx] for idx in indexes];
                f.closed
                List.append([str1 + w[0:(i+1)] + str2.replace(str2[0:(i+1)], '', 1) for w in words]);
                (loop_through(str1 + w[0:(i+1)],str2.replace(str2[0:(i+1)])) for w in words);
        return;
##t= open('translateddictionary.txt',"w+");
##with open('translateddictionary.txt',"w+") as t:
##    with open('dictionary.txt',"r") as f:
##        for line in f:
##            result="";
##            temp_str = line;
##            for i in range(len(temp_str)-1): #ignoring the new line character
##                result = result + txt_to_num(temp_str[i]);
##            result = result + "\n";
##            #breakpoint();
##            t.write(result);   
##    f.closed
##t.closed

def number_to_words(str):
    return;

def words_to_number(str):
    result = "";
    for i in range(s_len):
        #breakpoint();
        if str[i].isalpha():
            result = result + txt_to_num(str[i]);
        else:
            result = result + str[i];
    return result;

def all_wordification(str):
    List.clear();
    loop_through(str[0],str[1:len(str)])                       
    return;
    print(*List, sep = "\n");
                             
print(words_to_number(inputeng));
all_wordification(sample);
