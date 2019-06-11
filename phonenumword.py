import numpy as np

sample = "15128670987";
s_len = len(sample);

t= open('translateddictionary.txt',"w+")
with open('translateddictionary.txt') as t:
    with open('dictionary.txt') as f:
        for line in f:
            result="";
            temp_str = line;
            for i in range(0,len(temp_str)-2):
                result = result + txt_to_num(temp_str[i]);
            breakpoint();
            t.write(result);   
    f.closed
t.closed
N = 2000; #Dictionary line number

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
def number_to_words(str):

    return;
def words_to_number(str):
    return;
def all_wordification(str):        
    return;
