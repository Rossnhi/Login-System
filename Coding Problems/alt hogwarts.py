lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
data='\n'.join(lines)
a=data.find("Courses")
b=data.find("Students")
c=data.find("Grades")
d=data.find("EndOfInput")
Courses=data[7:b]
Students=data[b+8:c]
Grades=data[c+6:d]
Courses=Courses.strip()
Students=Students.strip()
Grades=Grades.strip()
Students=Students.split("\n")
for i in range(len(Students)):
	Students[i]=Students[i].split("~")
Grades=Grades.replace("AB","9.0")	
Grades=Grades.replace("BC","7.0")	
Grades=Grades.replace("CD","5.0")	
Grades=Grades.replace("A","10.")	
Grades=Grades.replace("B","8.0")	
Grades=Grades.replace("C","6.0")	
Grades=Grades.replace("D","4.0")
for i in range(len(Students)):
	while Grades.find(Students[i][0])!=-1:
		if len(Students[i])==4:
			Students[i][2]+=int(float(Grades[Grades.find(Students[i][0])+8:Grades.find(Students[i][0])+11]))
			Grades=Grades.replace(Students[i][0],"done",1)
			Students[i][3]+=1
		else:
			Students[i].append(int(float(Grades[Grades.find(Students[i][0])+8:Grades.find(Students[i][0])+11])))
			Grades=Grades.replace(Students[i][0],"done",1)
			Students[i].append(1)	
for i in range(len(Students)):
	if len(Students[i])<4:
		Students[i].append(0)
		Students[i].append(1)
for i in range(len(Students)):
    Students[i][2]=Students[i][2]/Students[i][3]
x=Students[:]
for i in range(len(Students)):
    x[i].remove(Students[i][3])
Students=x
for i in range(len(Students)):
	Students[i][2]=str(Students[i][2])		
for i in range(len(Students)):
	Students[i]="~".join(Students[i])
for i in range(len(Students)):
	print(Students[i])






