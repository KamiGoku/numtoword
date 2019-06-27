import random

List = [];

################################# Helper functions ######################################## 

def phone_to_num(str):
    return(str.replace('-',''));

def num_to_phone(str):
    #find word positions
    indexdash = [idx for idx in [0,1,4,7] if str[idx].isnumeric()];#eliminate phone dash in the middle of words
    for i in range(1, len(str)):
        if (str[i].isnumeric() != str[i-1].isnumeric()):
            indexdash.append(i);
    indexdash = list(set(indexdash));
    segs = [str[i:j] for i,j in zip(indexdash, indexdash[1:]+[None])];#index shift mapping
    result = '-'.join(segs);
    return result;

def txt_to_num(str):
    if str in "abc":
        return "2";
    elif str in "def":
        return "3";
    elif str in "ghi":
        return "4";
    elif str in "jkl":
        return "5";
    elif str in "mno":
        return "6";
    elif str in "pqrs":
        return "7";
    elif str in "tuv":
        return "8";
    else:
        return "9";

def generate_dict():
    t= open('translateddictionary.txt',"w+").close();
    with open('translateddictionary.txt',"w+") as t:
        with open('dictionary.txt',"r") as f:
            for line in f:
                result="";
                temp_str = line;
                for i in range(len(temp_str)-1): #ignoring the new line character
                    result = result + txt_to_num(temp_str[i]);
                result = result + "\n";
                #breakpoint();
                t.write(result);   
        f.closed
    t.closed
    return;

def look_up_dict(str,lim):
    result = [];
    if(len(str)>=(lim+1)): #only find words with at least lim letters
        with open('translateddictionary.txt',"r") as dictionary:
            for index, line in enumerate(dictionary,0):
                if str == line:
                    result.append(index);
        dictionary.closed
    return result;

def loop_through(str1,str2):
    #breakpoint();
    if not str2: #check for empty string
        return;        
    else:
        str1_new = str1 + str2[0];#add first characters
        str2_new = str2.replace(str2[0], '', 1); #remove first character
        loop_through(str1_new,str2_new);
        for i in range(len(str2)):
            
            indexes = look_up_dict(str2[0:(i+1)]+"\n",2);#find index of matching number strings,
            #limit the minimum characters per word (the current value is 2) when looking up the dictionary can reduce run time significantly and elimite unnecessary combinations
            
            if indexes: #found in dict
                words = [];
                with open('dictionary.txt',"r") as f:#find the words based on the index
                    lines=f.readlines();
                    words = [lines[idx] for idx in indexes];
                f.closed
                List.extend([str1 + w[0:(i+1)] + str2.replace(str2[0:(i+1)], '', 1) for w in words]);
                str2_new = str2.replace(str2[0:(i+1)],'',1);
                for j in range(len(words)):
                    str1_new = str1 + words[j][0:(i+1)];
                    loop_through(str1_new, str2_new);
        return;

################################## Main functions #########################################

def words_to_number(str):
    numstr = phone_to_num(str);
    result = "";
    for i in range(len(numstr)):
        if numstr[i].isalpha():
            result = result + txt_to_num(numstr[i]);
        else:
            result = result + numstr[i];
    result = num_to_phone(result);
    return result;

def all_wordifications(str):
    generate_dict(); #generate words to number string dictionary
    numstr = phone_to_num(str);
    List.clear();
    loop_through(numstr[0],numstr[1:len(numstr)]); #recursion function 
    result = [num_to_phone(element) for element in List];
    print("C = 9");
    return result;

def number_to_words(str):
    return random.choice(all_wordifications(str));
