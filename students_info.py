import db_operation as dbo
import matplotlib.pyplot as plt

re1 = dbo.select('StudentNickname' , 'view_students_info')
re2 = dbo.select('StudentRealName' , 'view_students_info')
re3 = dbo.select('StudentId' , 'view_students_info')
re4 = dbo.select('StudentSchool' , 'view_students_info')
gradelevel = dbo.select('GradeLevel' , 'view_students_info')
finalgrade = dbo.select('FinalGrade' , 'view_students_info')

point = []

for i in range(len(re1)):
    point.append(0)

for i in range(len(re1)):
    if re1[i][0]!='':
        point[i]+=1

for i in range(len(re2)):
    if re2[i][0]!='':
        point[i]+=1

for i in range(len(re3)):
    if re3[i][0]!='':
        point[i]+=1

for i in range(len(re4)):
    if re4[i][0]!='':
        point[i]+=1

print(point)

passing1=0
passing2=0
passing3=0
passing4=0
good1=0
good2=0
good3=0
good4=0
notpassing1=0
notpassing2=0
notpassing3=0
notpassing4=0
nograde1=0
nograde2=0
nograde3=0
nograde4=0

for i in range(len(point)):
    if (point[i]==1) and (gradelevel[i][0]=='合格'):
        passing1+=1
    if(point[i]==1) and (gradelevel[i][0]=='优秀'):
        good1+=1
    if(point[i]==1) and (gradelevel[i][0]=='不合格'):
        notpassing1+=1
    if (point[i] == 1) and (gradelevel[i][0] == ''):
        nograde1 += 1

    if (point[i]==2) and (gradelevel[i][0]=='合格'):
        passing2+=1
    if(point[i]==2) and (gradelevel[i][0]=='优秀'):
        good2+=1
    if(point[i]==2) and (gradelevel[i][0]=='不合格'):
        notpassing2 += 1
    if (point[i] == 2) and (gradelevel[i][0] == ''):
        nograde2 += 1

    if (point[i]==3) and (gradelevel[i][0]=='合格'):
        passing3+=1
    if(point[i]==3) and (gradelevel[i][0]=='优秀'):
        good3+=1
    if(point[i]==3) and (gradelevel[i][0]=='不合格'):
        notpassing3+=1
    if (point[i] == 3) and (gradelevel[i][0] == ''):
        nograde3 += 1

    if (point[i]==4) and (gradelevel[i][0]=='合格'):
        passing4+=1
    if(point[i]==4) and (gradelevel[i][0]=='优秀'):
        good4+=1
    if(point[i]==4) and (gradelevel[i][0]=='不合格'):
        notpassing4+=1
    if (point[i] == 4) and (gradelevel[i][0] == ''):
        nograde4 += 1

# print(re1)
# print(re2)
# print(re3)
# print(re4)
point1=passing1+good1+notpassing1+nograde1
point2=passing2+good2+notpassing2+nograde2
point3=passing3+good3+notpassing3+nograde3
point4=passing4+good4+notpassing4+nograde4

print(passing1)
print(float(passing1/point1))
print(good1)
print(float(good1/point1))
print(notpassing1)
print(float(notpassing1/point1))
print(nograde1)
print(float(nograde1/point1))

print(passing2)
print(float(passing2/point2))
print(good2)
print(float(good2/point2))
print(notpassing2)
print(float(notpassing2/point2))
print(nograde2)
print(float(nograde2/point2))

print(passing3)
print(float(passing3/point3))
print(good3)
print(float(good3/point3))
print(notpassing3)
print(float(notpassing3/point3))
print(nograde3)
print(float(nograde3/point3))

print(passing4)
print(float(passing4/point4))
print(good4)
print(float(good4/point4))
print(notpassing4)
print(float(notpassing4/point4))
print(nograde4)
print(float(nograde4/point4))

x=[1,2,3,4]
y1=[float(passing1/point1),float(passing2/point2),float(passing3/point3),float(passing4/point4)]
y2=[float(good1/point1),float(good1/point2),float(good3/point3),float(good4/point4)]
y3=[float(notpassing1/point1),float(notpassing2/point2),float(notpassing3/point3),float(notpassing4/point4)]
y4=[float(nograde1/point1),float(nograde2/point2),float(nograde3/point3),float(nograde4/point4)]

# plt.plot(x,y1,"g-")
# plt.ylim(0,1)
# plt.xlabel("information_point")
# plt.ylabel("passing_rate")
# plt.savefig("students_info_result/students_passing_rate")
# plt.show()
# print(type(x))
#
# plt.plot(x,y2,"g-")
# plt.ylim(0,1)
# plt.xlabel("information_point")
# plt.ylabel("good_rate")
# plt.savefig("students_info_result/students_good_rate")
# plt.show()
# print(type(x))
#
# plt.plot(x,y3,"g-")
# plt.ylim(0,1)
# plt.xlabel("information_point")
# plt.ylabel("notpassing_rate")
# plt.savefig("students_info_result/students_notpassing_rate")
# plt.show()
# print(type(x))
#
# plt.plot(x,y4,"g-")
# plt.ylim(0,1)
# plt.xlabel("information_point")
# plt.ylabel("nograde_rate")
# plt.savefig("students_info_result/students_nograde_rate")
# plt.show()
# # print(type(x))

plt.plot(x,y1,"g-",label='passing_rate')
plt.plot(x,y2,"r-",label='good_rate')
plt.plot(x,y3,"m-",label='notpassing_rate')
plt.plot(x,y4,"b-",label='nograde_rate')
plt.legend()
plt.ylim(0,1)
plt.xlabel("information_point")
plt.savefig("students_info_result/total")
plt.show()
print(type(x))
