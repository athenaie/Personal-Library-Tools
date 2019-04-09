import csv
import random

class Book:
    def __init__(self, info):
        self.title = info[1]
        self.author = info[3]
        self.media = info[14]
        self.tags = info[28].split(",")
        self.collections = info[29].split(",")
        if(self.media != "Ebook"):
            shelves = [s for s in self.tags if "Shelf" in s]
            if len(shelves) > 0:
                self.shelf = shelves[0][7:]
            else:
                if "Shelved" in self.tags:
                    self.shelf = "not catalogued"
                else: 
                    self.shelf = "None"
            boxes = [b for b in self.tags if "Box " in b]
            if len(boxes) > 0:
                self.box = boxes[0][5:]
            else:
                if "Boxed" in self.tags:
                    self.box = "not catalogued"
                else: 
                    self.box = "None"
        else: 
            self.shelf = "None"
            self.box = "None"
        
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
                if self.shelf == "not catalogued":
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

    books = random.sample(range(0, total-1), numBooks)
    
    subtbr = totaltbr

    print("--------------------------------")
    for book in books:
        print(subtbr[book])

