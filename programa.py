# Practica 2 - Alberto Jose Dominguez Lizardo - 1089458

import os

# Variables
nGroups = 0

students = 'Estudiantes.txt'
themes = 'Temas.txt'

students_set = set([])
themes_set = set([])

students_list = []
themes_list = []
groups_list = []

class groups:
    ID = 0
    nStudents = 0
    nThemes = 0
    students = []
    themes = []

# Process

with open(students) as txt_file:
    lines = txt_file.readlines()

for line in lines:
    students_set.add(line)

with open(themes) as txt_file:
    lines = txt_file.readlines()

for line in lines:
    themes_set.add(line)

for a in students_set:
    students_list.append(a)

for a in themes_set:
    themes_list.append(a)

print("The number of students: " + str(len(students_list)))
print("The number of themes: " + str(len(themes_list)))
nGroups = int(input("Insert the number of groups: "))

while nGroups > len(students_list):
    print("The numbers of groups is bigger than the number of students.")
    nGroups = int(input("Insert the number of groups: "))    

while nGroups > len(themes_list):
    print("The numbers of groups is bigger than the number of themes.")
    nGroups = int(input("Insert the number of groups: "))

for i in range(nGroups):
    g = groups()

    g.ID = i
    g.nStudents = 0
    g.students = []
    g.nThemes = 0
    g.themes = []

    groups_list.append(g)

auxiliar = 0
for a in range(len(students_list)):
    groups_list[auxiliar].students.append(students_list[a])
    groups_list[auxiliar].nStudents += 1

    auxiliar += 1

    if(auxiliar >= len(groups_list)):
        auxiliar = 0

auxiliar = 0
for a in range(len(themes_list)):
    groups_list[auxiliar].themes.append(themes_list[a])
    groups_list[auxiliar].nThemes += 1

    auxiliar += 1

    if(auxiliar >= len(groups_list)):
        auxiliar = 0
        
# Output
for i in groups_list:
    print("\nGroup # " + str(i.ID) + f" (Number of students: {i.nStudents}, Number of themes: {i.nThemes})")
    print("\n\tStudents: ")
    for a in i.students:
        print("\t\t"+a) 
    print("\tThemes: ")
    for j in i.themes:
        print("\t\t"+j)

input()
