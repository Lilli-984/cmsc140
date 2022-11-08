
import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd


temps = []
hats = []
# if the txt was in a differet folder: 
filepath = Path("Classwork") / "hats.txt"
#open(filepath)
with open(filepath) as f:
    for line in f.readlines():
        t, h = line.strip().split(" ")
        temps.append(int(t))
        hats.append(int(h))

print(temps)
print(hats)
plt.scatter(temps, hats)
plt.show()

def get_temp(filename):
    max_hats = 0
    max_temp = 0
    with open(filename) as f:
        next(f) # this allows us to skip the first line, which is header text
        for line in f.readlines():
            t, h = line.split(" ")
            t = int(t)
            h = int(h)
# last three lines: t,h = line.strip().split(" ")
            if h > max_hats:
                max_hats = h
                max_temp = t
    return max_temp

max_temperature = get_temp(filepath)
print(max_temperature)
#plot_temps

#Excerise 1
filep = Path("baseball.txt")
def get_best_team(filep):
    best_team= ""
    best_record = 0
    with open("baseball.txt"):
        next(f)
        for line in f.readlines():
            line = line.strip()
            team, w, l = line.split(",")
            record = int(w)/int(l)
            if record > best_record:
                best_record = record
                best_name = team
    return best_team
        

import pandas as pd
prof_info = {
    "Ackles" : {
        "classes": ["Python", "Algorithms"],
        "office": "Steitz 131",
        "firstname": "Acacia"
    },
    "Krebsbach" : {
        "classes": ["Java", "FYS"],
        "office": "Briggs 411"
    },
    "Gregg" : {
        "classes": ["Web Devel", "Algorithms"],
        "office": "Briggs 413"

    }
}
df = pd.DataFrame(data=prof_info)
print(df)
print(df["Ackles"]["classes"])
print(df.loc["classes", "Ackles"])
print(df.iloc[1,2])

hatsPath = Path("Classwork") / ("hats.txt")
hattemps = pd.read_csv(hatsPath, sep = " ")