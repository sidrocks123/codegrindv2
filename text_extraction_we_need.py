import re

def min_edit_dist(word1,word2):
    len_1 = len(word1)
    len_2 = len(word2)
    x=[[0]*(len_2+1) for _ in range(len_1+1)]
    for i in range(0,len_1+1):
        x[i][0]=i
    for j in range(0,len_2+1):
        x[0][j]=j
    for i in range(1,len_1+1):
        for j in range(1,len_2+1):
            if word1[i-1]==word2[j-1]:
                x[i][j] = x[i-1][j-1]
            else:
                x[i][j]=min(x[i][j-1],x[i-1][j],x[i-1][j-1])+1
    return x[i][j]
    
def string_processing(string):
    #convert it to lowercase
    string= string.lower()
    #remove all thecharacters but lowercase alphabet by none
    string=re.sub(r"[^a-z]","",string)
    return string
    
def look_for_keyword(word):
    #Important keywords occur in boarding pass and e-ticket
    keywords = ["flight","flt","date","from","to","amt","amount",
            "fare","total fare","pnr","etk","eticket","eticketno"]
    word=string_processing(word)
    for i in keywords:
        i=string_processing(i)
        if min_edit_dist(word,i) <= 2*len(word)/3:
            return i            
  
def look_for_merchant(word):
    #flight merchants in India
    flight_merchant = ["jet airways","air india","air vistara",
                   "spicejet","air asia","indigo","goair",
                   "etihad airways","emirates","malaysia airlines"]
    word = string_processing(word)
    for i in flight_merchant:
        i = string_processing(i)
        #print(word,i)
        if min_edit_dist(word,i) <= 2*len(word)/3:
            return i
          
 
            
  
