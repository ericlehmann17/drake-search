#learned a little bit about csv files and the csv library while making this program. Also have a pretty cool way to search for popular drake songs!

import csv
from string import * 

# convert_num: converts things like "1M" or "2.4K" to 1000000 and 2400 
# converts input string to a list of chars, manipulates that list, then remakes the string and casts to int
def convert_num(n):     # returns 0 if a songs is n/a, -1 if unreleased
    listn = [char for char in str(n)]
    newlistn = []
    for char in listn:
        if char == '.':
            pass
        elif char == 'K':
            for i in range(2):
                newlistn.append('0')
        elif char == 'M':
            for i in range(5):
                newlistn.append('0')
        else:
            newlistn.append(char)
    
    newstringn = ''.join(newlistn)
    newintn = 0
    if newstringn:
        if newstringn == '(Unreleased)':
            newintn = -1
        else:
            newintn = int(newstringn)
    return newintn

        
        
# function that finds all drake songs with # of genius hits between the bounds
def find_drake(lower, upper):      #n will be the minimum number of genius hits the returned songs got
    with open("drake_data.csv", encoding = 'utf8') as drake_data:
        csv_reader = csv.reader(drake_data, delimiter = ',')    #csv reader makes an iterator over the rows of the csv
        first_line = True
        for row in csv_reader:
            if first_line:
                #print(f"Column names are {', '.join(row)}")
                first_line = False
            else:
                if (convert_num(row[4]) >= lower) and (convert_num(row[4]) <= upper): #if this song's hits are between the bounds
                    print(f"{row[0]}, {row[1][:-7]}, {row[4]}")     #print the album title, song title, and the number of hits

#main function, run at the end of the file
def main():
    print("Welcome to DrakeSearch.")
    print()
    print("This program allows you to search for Drake songs by")
    print("the amount of hits his songs have on Genius.")
    print()
    while(1):
        lower = input("Enter a lower bound: (type 'q' or 'quit' to quit, or 'h' for help) ")
        if lower.lower() == "q" or lower.lower() == "quit": break
        if lower.lower() == "h":
            print("\nINSTRUCTIONS:\n")
            print("When prompted to enter the bounds, enter only integers.\n")
            print("The bounds determine what songs are returned. Only songs that")
            print("have been visited MORE than <lower bound> number of times and ")
            print("LESS than <upper bound> number of times will be returned.\n")
            continue
        try: 
            lowern = int(lower)
        except ValueError as e:
            print("That is not a number. Please only enter integers.\n")
            continue

        upper = input("Enter an upper bound: ")
        try: 
            uppern = int(upper)
        except ValueError as e:
            print("That is not a number. Please only enter integers.\n")
            continue
        
        print("SEARCH RESULTS:\n")
        find_drake(lowern, uppern)

main()





