#NOTE:-The Students which are in quiz file are the student who attend the class
#NOTE:-For accurate Answer please add any random name after the last name in "quiz student" file
#NOTE:-Please write all the students name in Total_student File
#NOTE:-Make scure "Present Student","quiz_student","Totla_student" fils should created before renning this
class_attend=open("class_attend.txt","r")
quiz_attend=open("quiz_attend.txt","r")
class_only=open("class_only.txt","w")
quiz_only=open("quiz_only.txt","w")
present=open("real_present.txt","w")
no_class_student=0
no_quiz_student=0
class_student=[]
quiz_student=[]
no_student=[]
for i in class_attend:
    class_student.append(i)
#print("No of student who attend the class is ",no_class_student)
for i in quiz_attend:
        quiz_student.append(i)
#print("No of student who attend the Quiz is ",no_quiz_student)
flag=0
for i in range(len(class_student)):
    for j in range(len(quiz_student)):
        if class_student[i]==quiz_student[j]:
            #print(i)
            flag=3
            present.write(class_student[i])

    if flag==0:
        no_student.append(class_student[i])
for i in range(len(class_student)):
    for j in range(len(no_student)):
        if class_student[i]==no_student[j]:
            class_only.write(class_student[i])

for i in range(len(quiz_student)):
    for j in range(len(no_student)):
        if quiz_student[i]==no_student[j]:
            quiz_only.write(quiz_student[i])