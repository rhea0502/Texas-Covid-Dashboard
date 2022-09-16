# File: Project3.py
# Student: Rhea Mudnal
# UT EID: rsm2983
# Course Name: CS303E
# 
# Date Created: 4/27/21
# Date Last Modified: 4/30/21
# Description of Program: This program shows the contents of the COVID data File depending on what the user asks to see.

import os.path

filename="county-covid-data.txt"
if not os.path.isfile(filename):
    print("File county-covid-data.txt not found.")
     
else:
    infile=open(filename, "r")
    text=infile.readline()
    text=infile.readline()
    county_list=[]
    covid_dict={}
    confirmed_cases=0
    deaths=0

    while text:
        if text[0]!="#":
            text=text.split(",")
            county_list.append(text[0])     
            count_tuple=(int(text[1]),int(text[3]))
            covid_dict[text[0]]=count_tuple
            confirmed_cases=int(text[1])+confirmed_cases
            deaths=int(text[3])+deaths

        text=infile.readline()

    
    
    infile.close()
    print("")
    print("Welcome to the Texas Covid Database Dashboard.")
    print("This provides Covid data in Texas as of 1/26/21.")
    print("Creating dictionary from file: county-covid-data.txt")
    print(" ")
    print("Enter any of the following commands:")
    print("Help - list available commands;")
    print("Quit - exit this dashboard;")
    print("Counties - list all Texas counties;")
    print("Cases <countyName>/Texas - confirmed Covid cases in specified county or statewide;")
    print("Deaths <countyName>/Texas - Covid deaths in specified county or statewide.")
    print("")
    command=input("Please enter a command: ")
    command=command.lower()
    commWords = command.split()
    comm = commWords[0]
    args = commWords[1:]
    arg = " ".join(args)
    while comm!="quit":
        if comm=="help":
            print("Help - list available commands;")
            print("Quit - exit this dashboard;")
            print("Counties - list all Texas counties;")
            print("Cases <countyName>/Texas - confirmed Covid cases in specified county or statewide;")
            print("Deaths <countyName>/Texas - Covid deaths in specified county or statewide.")

        elif comm=="counties":
            str=""
            count=0
            for county in county_list:
                count+=1
                str=str+county+", "
                if count==10:
                    print(str)
                    str=""
                    count=0
            print(str)

        elif comm=="cases":
            
            if arg.title()=="Texas":
                print("Texas total confirmed Covid cases:",confirmed_cases)
            else:
                if arg.title() in covid_dict:
                    value=covid_dict[arg.title()][0]
                    print(arg.title(), "county has", value, "confirmed Covid cases.")
                else:
                    print("County", arg, "is not recognized.")
            
        elif comm=="deaths":
            if arg.title()=="Texas":
                print("Texas total confirmed Covid deaths:", deaths)
            else:
                if arg.title() in covid_dict:
                    value=covid_dict[arg.title()][1]
                    print(arg.title(), "county has", value,"fatalities.")
                else:
                    print("County", arg, "is not recognized.")
                
        else:
            print("Command is not recognized.  Try again!")
        print("")
        command=input("Please enter a command: ")
        command=command.lower()
        commWords = command.split()
        comm = commWords[0]
        args = commWords[1:]
        arg = " ".join(args)
    print("Thank you for using the Texas Covid Database Dashboard.  Goodbye!")  

