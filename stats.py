import csv
import random
import sys
from termcolor import colored
import matplotlib.pyplot as plt

class Book:
    def __init__(self, info):
        self.title = info[1]
        
        self.media = info[14]
        self.tags = info[28].split(", ")
        self.collections = info[29].split(", ")

        # author
        author = info[3].split(", ")
        if len(author) == 2:
            self.authorfirst = author[1]
            self.authorlast = author[0]
        else:
            self.authorfirst = info[3]
            self.authorlast = ""

        # pages
        try:
            self.pages = int(info[21])
        except:
            self.pages = 0

        # collections
        self.fiction = False 
        self.nonfiction = False 
        self.childrens = False
        self.read = False
        self.toread = False
        if "Fiction" in self.collections:
            self.fiction = True
        if "Non-fiction" in self.collections:
            self.nonfiction = True
        if "Children's Books" in self.collections:
            self.childrens = True
        if "Read" in self.collections:
            self.read = True
        if "To read" in self.collections:
            self.toread = True 

        # convoluted location information 

        self.apartment = False
        self.home = False 
        self.ereader = False

        if(self.media != "Ebook"):
            shelves = [s for s in self.tags if "Shelf" in s]
            # if there's a shelf catalogued
            if len(shelves) > 0:
                self.shelf = shelves[0][6:]
                # if it's in my apartment
                if self.shelf == "Home":
                    self.apartment = True
                # if it's not in my apartment
                else:
                    self.home = True 
            # if there's no shelf catalogued
            else:
                # if it's hypothetically shelved somewhere
                if "Shelved" in self.tags:
                    self.shelf = "not catalogued"
                else: 
                    self.shelf = "None"
            boxes = [b for b in self.tags if "Box " in b]
            # if there's a box catalogued
            if len(boxes) > 0:
                self.box = boxes[0][4:]
                self.home = True 
            else:
                # if it's hypothetically boxed somewhere
                if "Boxed" in self.tags:
                    self.box = "not catalogued"
                    # show up for both locations just to be safe
                    self.home = True
                else: 
                    self.box = "None"
        else: 
            self.shelf = "None"
            self.box = "None"
            self.ereader = True
        
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
        
        return colored(self.title, 'blue') + " (" + self.media + ", " + str(self.pages) + "pg)" + "\nby " + self.authorfirst + " " + self.authorlast + "\n\n" + "Location: " + locationString + "\n--------------------------------"

with open('library.csv', 'r') as csvfile:
    tbrreader = csv.reader(csvfile, delimiter=',')
    totaltbr = []
    next(tbrreader)
    for row in tbrreader:
        totaltbr.append(Book(row))

    while True:
        try:
            locationChar = str(input("From which location (please enter a letter)?\nA) Apartment\nB) Home\nC) All physical\nD) Ereader\nE) Anywhere\n")).upper()
            if locationChar in ["A", "B", "C", "D", "E"]:
                print()
                break
            else: 
                print("\nInvalid character, please enter A, B, C, D, or E\n")
        except:
                print("\nInvalid input, please enter A, B, C, or D, or E\n")

    if locationChar == "A":
        subtbr = [b for b in totaltbr if b.apartment == True]
    elif locationChar == "B":
        subtbr = [b for b in totaltbr if b.home == True]
    elif locationChar == "C":
        subtbr = [b for b in totaltbr if b.ereader == False]
    elif locationChar == "D":
        subtbr = [b for b in totaltbr if b.ereader == True]
    else:
        subtbr = totaltbr


    while True:
        try:
            collectionChar = str(input("From which collection?\nA) Fiction\nB) Non-fiction\nC) Children's books\nD) Read\nE) To Read\nF) Any collection\n")).upper()
            if collectionChar in ["A", "B", "C", "D", "E", "F"]:
                print()
                break
            else: 
                print("\nInvalid character, please enter A, B, C, D, E, or F\n")
        except:
                print("\nInvalid input, please enter A, B, C, D, E, or F\n")
                    
    if collectionChar == "A":
        subtbr = [b for b in subtbr if b.fiction == True]
    elif collectionChar == "B":
        subtbr = [b for b in subtbr if b.nonfiction == True]
    elif collectionChar == "C":
        subtbr = [b for b in subtbr if b.childrens == True]
    elif collectionChar == "D":
        subtbr = [b for b in subtbr if b.read == True]
    elif collectionChar == "E":
        subtbr = [b for b in subtbr if b.toread == True]
    else:
        subtbr = subtbr 

    if (len(subtbr) == 0):
        print("Sorry, there are no books that meet those criteria.")
        exit()

    if len(subtbr) == len(totaltbr):
        givepercent = False
    else:
        givepercent = True 

    pages = 0

    for book in subtbr:
        pages = pages + book.pages

    avgpages = int(float(pages) / float(len(subtbr)))

    if givepercent:
        totalpages = 0
        for book in totaltbr:
            totalpages = totalpages + book.pages
        percentpages = int((float(pages)/float(totalpages))*100)
        percentbooks = int((float(len(subtbr))/float(len(totaltbr)))*100)
        print("Number of books: " + str(len(subtbr)) + " (" + str(percentbooks) + "%)")
        print("Total number of pages: " + str(pages) + " (" + str(percentpages) + "%)")
        print("Average number of pages: " + str(avgpages))

    else:
        print("Number of books: " + str(len(subtbr)))
        print("Total number of pages: " + str(pages))
        print("Average number of pages: " + str(avgpages))
 
    pagesarr = []
    for book in subtbr:
        pagesarr.append(book.pages)

    plt.hist(pagesarr, bins='auto')
    plt.title("Frequency of Book Length")
    plt.xlabel("Pages")
    plt.ylabel("Books")
    plt.show()

"""     while True:
        try:
            numBooks = int(input("How many books would you like from the TBR jar?\n"))
            if(numBooks <= len(subtbr)):
                print()
                break
            else: 
                print("\nInvalid number of books, please enter a number less than " + str(len(subtbr) + 1) + "\n")
        except:
            print("\nInvalid number of books, please enter a number\n")
    
    print("--------------------------------")
    books = random.sample(range(0, len(subtbr)), numBooks)
    for book in books:
        print(subtbr[book])
    
"""

