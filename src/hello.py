print("hello world!");

x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")

print("using","separator","on","phrase", sep="-");

def printChampion(country,times): 
    print(country,"wins",times,"world cups", sep=" ", end="\n\n");

country = "Brazil";
times = 5;

printChampion(country,times);

country = "Italy";
times = 4;

printChampion(country,times);
