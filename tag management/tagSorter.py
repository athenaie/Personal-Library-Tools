import cmd
import csv
import pyperclip
import pprint

blackList = []

seriesAndSets = ["A Practical Guide", "A Series of Unfortunate Events", "Agatha Christie", "Animorphs", "Arcturus Crime Classics", "Arcturus Paperback Classics", "Bear in the Big Blue House", "Big Comfy Couch", "Big Little Books", "Choose Your Own Adventure", "Curious George", "Doctor Who", "Don\'t Sweat", "Franklin Library", "Ghosts of Fear Street", "Give Yourself Goosebumps", "Goosebumps", "Harry Potter", "Heron Classics", "Life\'s Library", "Lord of the Rings", "Magic School Bus", "Mouse Works", "Mr. Men & Little Miss", "Nancy Drew", "Narnia Box Set", "Out and About With Pooh", "Penguin Great Ideas", "Puffin Classics", "Puffin in Bloom", "Ripley\'s", "Seuss", "Star Wars", "Sterling Set", "The School of Life", "Uncle John\'s Bathroom Reader", "Vintage Classics", "Western Canadian Literature for Youth", "Winnie the Pooh", ]
blackList.extend(seriesAndSets)
readathons = ["Bookcrossing Read-a-thon", "Buzzword Read-a-thon: WWWWWH", "Buzzword Read-a-thon: You", "O.W.L.s Magical Readathon", "Reading Rush", "Sci-Fi Summer Readathon"]
blackList.extend(readathons)
greatest = ["Top 1 000 Greatest Books of All Time", "Top 1 100 Greatest Books of All Time", "Top 1 200 Greatest Books of All Time", "Top 1 300 Greatest Books of All Time", "Top 1 500 Greatest Books of All Time", "Top 10 Greatest Books of All Time", "Top 100 Greatest Books of All Time", "Top 1200 Greatest Books of All Time", "Top 2 100 Greatest Books of All Time", "Top 200 Greatest Books of All Time", "Top 300 Greatest Books of All Time", "Top 400 Greatest Books of All Time", "Top 500 Greatest Books of All Time", "Top 600 Greatest Books of All Time", "Top 700 Greatest Books of All Time", "Top 800 Greatest Books of All Time"]
blackList.extend(greatest)
boxes = ["Box 01", "Box 02", "Box 05", "Box 06", "Box 07", "Box 08", "Box 09", "Box 11", "Box 12", "Box Christmas"]
blackList.extend(boxes)
shelves = ["Shelf A0", "Shelf A1", "Shelf A2", "Shelf A3", "Shelf A4", "Shelf A5", "Shelf A6", "Shelf B0", "Shelf B1", "Shelf B2", "Shelf B3", "Shelf B4", "Shelf B5", "Shelf B6", "Shelf C0", "Shelf C1", "Shelf C2", "Shelf C3", "Shelf C4", "Shelf C5", "Shelf C6", "Shelf D0", "Shelf D1", "Shelf D2", "Shelf D3", "Shelf D4", "Shelf D5", "Shelf D6", "Shelf E0", "Shelf E1"]
blackList.extend(shelves)
home = ["Shelf Home", "Shelf Read in 2019/2020"]
blackList.extend(home)
years = ["Read in 2008", "Read in 2009", "Read in 2010", "Read in 2011", "Read in 2012", "Read in 2013", "Read in 2014", "Read in 2015", "Read in 2016", "Read in 2017", "Read in 2018", "Read in 2019", "Read in 2020"]
blackList.extend(years)
otherExlusions = ["Boxed", "Shelved", "Readathon", "Read-a-long", "Shelf unknown", "To consign", "To catalogue", "TBR 2019", "Pages error", "Possible info errors", "Check Dedication", "Missing words", "Youth Favourites Shelf"]
blackList.extend(otherExlusions)

print(len(blackList))

tags = []

existingTags = input("Enter a list of existing tags:\n").rstrip(",")
if existingTags != "":
    tags = existingTags.split(", ")
    tags = [x.strip() for x in tags]

print(tags)

addYear = input("\nDo you want to add a year read (y/n)?\n")
if addYear == "y":
    year = input("\nWhat year did you read this book?\n")
    if year != "":
        tags.append("Read in " + year)
        print(tags)

addSeriesOrSet = input("\nDo you want to add a Series, Set, Author, or Publisher (y/n)?\n")
if addSeriesOrSet == "y":
    pprint.pprint(seriesAndSets)
    newTag = input("\nWhich would you like to add?\n")
    if newTag != "" and newTag != "n":
        tags.append(newTag)
        print(tags)

addReadathon = input("\nWas this part of a Readathon (y/n)?\n")
if addReadathon == "y":
    pprint.pprint(readathons)
    newTag = input("\nWhich would you like to add?\n")
    if newTag != "" and newTag != "n":
        tags.append(newTag)
        tags.append("Readathon")
        print(tags)

where = input("\nWhere is the book (home/shelved/boxed/unknown)?\n")
if where == "boxed":
    pprint.pprint(boxes)
    newTag = input("\nWhich would you like to add?\n")
    if newTag != "" and newTag != "n":
        tags.append(newTag)
        tags.append("Boxed")
        print(tags)
elif where == "shelved":
    pprint.pprint(shelves)
    newTag = input("\nWhich would you like to add?\n")
    if newTag != "" and newTag != "n":
        tags.append(newTag)
        tags.append("Shelved")
        print(tags)
elif where == "unknown":
    tags.append("Shelf unknown")
    print(tags)
elif where == "home":
    want = input("\nIs this on the 2019/2020 read shelf (y/n)?\n")
    if want == 'y':
        tags.append("Shelf Home")
        tags.append("Shelf Read in 2019/2020")
        tags.append("Shelved")
        print(tags)

moreTags = input("\nDo you want to add more tags (y/n)?\n")

count = 0
if moreTags == "y":
    with open('tags.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for tag in row:
                count += 1
                if tag not in tags:
                    if tag not in blackList:
                        want = input("\nDo you want to add the tag \"" + tag + "\" (y/n)?\n")
                        if want == "y":
                            tags.append(tag)
                            print(tags)
                        elif want == "" or want == "n":
                            pass
                        elif want == "quit":
                            break
                        else:
                            tags.append(want)
                            print(tags)
                else:
                    remove = input("\nThe tag \"" + tag + "\" is already added, do you want to remove it (y/n)?\n")
                    if remove == "y":
                        tags.remove(tag)
                        print(tags)

tags.sort()
tags = list(filter(None, tags))
tagsString = ""
print("This book has " + str(len(tags)) + " tags of a possible " + str(count) + ".\n")
for tag in tags:
    tagsString += tag + ", "
print(tagsString)
pyperclip.copy(tagsString)
