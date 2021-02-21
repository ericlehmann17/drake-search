# drake-search
Fun program that searches for drake songs based on how many hits his songs have gotten on genius.com. 

This is a very simple python program that just reads from standard in and prints to standard out. While making this program, I learned a little bit about manipulating csv files, error handling, and file encodings. 

This repo includes the csv file containing all of the data about drake's songs from Genius, as well as the single python file which, when run, prompts the user to enter an upper and lower bound. These bounds determine which songs will be returned - if 1 is the lower bound and 1000 is the upper bound, only songs that have been visited between 1 and 1000 times on genius.com will show up. The program continues until the user types 'q' or 'quit', and will display a help message if the user enters 'h'.
