fp = open('out.txt')
lines = fp.read().split("\n") # Create a list containing all lines
fp.close() # Close file

fp1 = open('out1.txt')
lines1 = fp1.read().split("\n") # Create a list containing all lines
fp1.close() # Close file

fp2 = open('out_board.txt')
lines2 = fp2.read().split("\n") # Create a list containing all lines
fp2.close() # Close file


for line in lines:
    if line:
        #print(line)
        words = line.split(" ")
        for word in words:
            #print(word)
        #print("-------------")
        
        
#total amount

fare = ""
found=False
for line in lines:
    if line:
        line = line.lower()
        if "total fare" in line:
            #print(line)
            words = line.split(" ")
            for word in words:
                if word.isdigit():
                    fare=word
                    found = True
                    #print(word)
    if found:
        break
        
        
#location
loc=""
for line in lines1:
    if line:
        line = line.lower()
        if "airport" in line:
            loc = line
            break
            

location = loc.split(" ")

list_loc=[]
for loc in location:
    #print(loc)
    if loc.endswith(","):
        list_loc.append(loc[:-1])
        
from_loc = list_loc[0]
to_loc = list_loc[1]

#travelling class
travelling_class=""
for line in lines2:
    if line:
        line = line.lower()
        if "economy" in line:
            travelling_class = "Economy"
        else:
            travelling_class="Business"

#merchant
flight_merchant = ["jet airways","air india","air vistara",
                   "spicejet","air asia","indigo","goair",
                   "etihad airways","emirates","malaysia airlines"]

merchant=""
found=False
for line in lines2:
    if line:
        line = line.lower()
        for flight in flight_merchant:
            if flight in line:
                merchant=flight
                found=True
                break
        if found:
            break
#ticket number 
ticket_num =""
found=False
found_tick = False
for line in lines2:
    if line:
        line = line.lower()
        if "ticket" in line and found_tick==False:
            found_tick = True
            words = line.split(" ")
            for word in words:
                if word.isdigit():
                    ticket_num = word
                    found = True
                    break
            if found:
                break
            else:
                continue
        if found_tick:
            ticket_num = int(line)
            break

#dates
week_days = [" sun "," mon "," tue "," wed "," thu "," fri "," sat "]
dates = ""
for line in lines1:
    if line:
        line = line.lower()
        for day in week_days:
            if day in line:
                dates = line
                print(line)
                

from datetime import datetime
import re
string = dates
string = string.replace(",", "")
print(string)
datelist = re.findall(r'[0-9]+[ ]+[a-z][a-z][a-z]+[ ]+[0-9]+',string)
print(datelist)
formatted_dl = []
for dates in datelist:
	obj = datetime.strptime(dates, '%d %b %Y').date()
	final = [str(obj.year),str(obj.month),str(obj.day)]
	formatted_dl.append(final)
print(formatted_dl)
