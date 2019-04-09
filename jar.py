import csv
import random

class Book:
    def __init__(self, info):
        self.title = info[1]
        self.author = info[3]
        self.media = info[14]
        self.tags = info[28].split(",")
        self.collections = info[29].split(",")

        # convoluted location information 

        # to be safe if there is missing information
        self.apartment = True
        self.home = True

        if(self.media != "Ebook"):
            shelves = [s for s in self.tags if "Shelf" in s]
            # if there's a shelf catalogued
            if len(shelves) > 0:
                self.shelf = shelves[0][7:]
                # if it's in my apartment
                if self.shelf == "Home":
                    self.apartment = True
                    self.home = False
                # if it's not in my apartment
                else:
                    self.apartment = False 
                    self.home = True 
            # if there's no shelf catalogued
            else:
                # if it's hypothetically shelved somewhere
                if "Shelved" in self.tags:
                    self.shelf = "not catalogued"
                    # show up for both locations just to be safe
                    self.home = True
                    self.apartment = True
                else: 
                    self.shelf = "None"
            boxes = [b for b in self.tags if "Box " in b]
            # if there's a box catalogued
            if len(boxes) > 0:
                self.box = boxes[0][5:]
                # no boxes in my apartment
                self.apartment = False 
                self.home = True 
            else:
                # if it's hypothetically boxed somewhere
                if "Boxed" in self.tags:
                    self.box = "not catalogued"
                    # show up for both locations just to be safe
                    self.home = True
                    self.apartment = True
                else: 
                    self.box = "None"
        else: 
            self.shelf = "None"
            self.box = "None"
            # assume I have my ereader
            self.home = True
            self.apartment = True
        
    def __str__(self):
        locationString = "Unknown"
        if self.media != "Ebook":
            if self.shelf != "None":
                if self.shelf == "Home":
                    locationString = "My apartment"
                elif self.shelf == "not catalogued":
                    locationString = "Shelved somewhere"
                else:
                    locationString = "At home on Shelf " + self.shelf
            if self.box != "None":
                if self.box == "not catalogued":
                    locationString = "Boxed somewhere"
                else:
                    locationString = "At home in Box " + self.box
        else:
            locationString = "On my ereader"
        
        return self.title + " (" + self.media + ")" + "\nby " + self.author + "\n\n" + "Location: " + locationString + "\n--------------------------------"

with open('tbr.csv', 'r') as csvfile:
    tbrreader = csv.reader(csvfile, delimiter=',')
    totaltbr = []
    next(tbrreader)
    for row in tbrreader:
        totaltbr.append(Book(row))
    total = len(totaltbr)
    while True:
        try:
            numBooks = int(input("How many books would you like from the TBR jar?\n"))
            if(numBooks <= total):
                print()
                break
            else: 
                print("\nInvalid number of books, please enter a number less than " + str(total + 1) + "\n")
        except:
            print("\nInvalid number of books, please enter a number\n")

    while True:
        try:
            locationChar = str(input("From where (please enter a letter)?\nA) Apartment\nB) Home\nC) Anywhere\n")).upper()
            if locationChar == "A" or locationChar == "B" or locationChar == "C":
                print()
                break
            else: 
                print("\nInvalid character, please enter A, B, or C\n")
        except:
                print("\nInvalid input, please enter A, B, or C\n")

    if locationChar == "A":
        subtbr = [b for b in totaltbr if b.apartment == True]
    elif locationChar == "B":
        subtbr = [b for b in totaltbr if b.home == True]
    else:
        subtbr = totaltbr
    
    books = random.sample(range(0, len(subtbr) - 1), numBooks)

    print("--------------------------------")
    for book in books:
        print(subtbr[book])

