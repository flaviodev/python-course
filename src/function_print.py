print("hello world!");

print("using","separator","on","phrase", sep="-");

def print_champion(country,times): 
    print(country,"wins",times,"world cups", sep=" ", end="\n\n");

country = "Brazil";
times = 5;

print_champion(country,times);

country = "Italy";
times = 4;

print_champion(country,times);
