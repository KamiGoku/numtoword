import numpy as np

sample = "15128670987";
s_len = len(sample);

inputeng = "1800painter";
inputnum = "1-800-724-6837";

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

t= open('translateddictionary.txt',"w+");
with open('translateddictionary.txt',"w+") as t:
    with open('dictionary.txt',"r") as f:
        for line in f:
            result="";
            temp_str = line;
            for i in range(len(temp_str)-1):
                result = result + txt_to_num(temp_str[i]);
            result = result + "\n";
            #breakpoint();
            t.write(result);   
    f.closed
t.closed

def number_to_words(str):
    return;
def words_to_number(str):
    result = "";
    for i in range(s_len):
        if str[i].isalpha:
            result = result + txt_to_num(str[i]);
        else:
            result = result + str[i];
    return result;
def all_wordification(str):        
    return;



