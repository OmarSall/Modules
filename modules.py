import time     #builtin lib
import os       #standard lib
import sys      
import pandas as pd     #3rd party lib

# while True:
#     if os.path.exists("files/vegetables3.txt"):

#         with open("files/vegetables3.txt") as file:
#              print(file.read())
#     else:
#         print("File does not exist.")
#     time.sleep(10)

while True:
    if os.path.exists("files/temps_today.csv"): 
        data = pd.read_csv("files/temps_today.csv")
        print(data.mean()["st1"])
    else:
        print("File does not exist.")
    time.sleep(10)