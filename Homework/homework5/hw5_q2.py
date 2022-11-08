
import re

major_courses = [
    "BIOL 130",
    "BIOL 150",
    "BIOL 280",
    "PHYS 141",
    "PHYS 151",
    "GEOL 110",
    "GEOS 210",
    "BIOL 650"
]



def get_courses(major_courses):
    bio_courses = []
    for course in major_courses:
        name, num = course.split()
        m = int(num)
        if "BIOL" == name:
            bio_courses = bio_courses + [m]
    return(bio_courses)

get = get_courses(major_courses)
print(get)