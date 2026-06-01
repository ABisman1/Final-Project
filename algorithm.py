#assign students there grades etc.
studentcount = int(input("enter amount of students"))
listofstudents = []
listofstudents_grades = []
for x in range(studentcount):
	student = str(input(f"enter student {x} name"))
	studentgrade = int(input(f"enter grade of student {student}"))
	listofstudents.append(student)
	listofstudents_grades.append(studentgrade)
	print(f'{listofstudents[x]} - {listofstudents_grades[x]}')


tablecount = int(input("enter amount of tables"))
tables = []
listofseatpertable = []
for x in range(tablecount):
	table = str(input(f"enter table {x} name"))
	seats = int(input(f"enter seats for table {table}"))
	tables.append(table)
	listofseatpertable.append(seats)
	print(f'{tables[x]} - {listofseatpertable[x]}')

Group 
#assign students for the group 
for x in range(studentcount):
