

classes = {
    "ANTH 110":{
    "- Course Name: ":"Cultural Anthropology", 
    "- Professor: ": "Daughtry", 
    "- Units: ": 6, 
    "- Meets:": ["M 8:30 - 9:40","W 8:30 - 9:40","F 8:30 - 9:40"]} , 
    "CMSC 140": 
    {"- Course Name: ":"Intro to Python Programming", 
    "- Professor: ": "Ackles", 
    "- Units: ": 6, 
    "- Meets:": ["M 9:50 - 11:00","W 9:50 - 11:00","R 10:25 - 12:10"]}, 
    "MATH 230": 
    {"- Course Name: ":"Discrete Mathematics", 
    "- Professor: ": "Sattler", 
    "- Units: ": 6, 
    "- Meets:": ["M 1:50 - 3:00","W 1:50 - 3:00","F 1:50 - 3:00"]}
}

for i in classes.keys():
    print("Course Code: ",i)
    for x in classes[i].keys():
        if x == "- Meets:":
            print(x[0])
            print(x[1])
            print(x[2])
        else:
            print (x, classes[i][x])
    print("----")