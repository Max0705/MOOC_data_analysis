import db_operation as dbo

# 系统评分1，老师批改2，学生互评3
submits1 = dbo.select_where('submits', 'lesson_detail', 'method like "%系统评分%"')
submits2 = dbo.select_where('submits', 'lesson_detail', 'method like "%老师批改%"')
submits3 = dbo.select_where('submits', 'lesson_detail', 'method like "%学生互评%"')
max_score1 = dbo.select_where('maxscore', 'lesson_detail', 'method like "%系统评分%"')
max_score2 = dbo.select_where('maxscore', 'lesson_detail', 'method like "%老师批改%"')
max_score3 = dbo.select_where('maxscore', 'lesson_detail', 'method like "%学生互评%"')
avg_score1 = dbo.select_where('averagescore', 'lesson_detail', 'method like "%系统评分%"')
avg_score2 = dbo.select_where('averagescore', 'lesson_detail', 'method like "%老师批改%"')
avg_score3 = dbo.select_where('averagescore', 'lesson_detail', 'method like "%学生互评%"')

print(len(submits2))
total_sub1 = 0
total_sub2 = 0
total_sub3 = 0
score1 = 0
score2 = 0
score3 = 0
for i in range(0, len(submits1)):
    total_sub1 += submits1[i][0]
    score1 += avg_score1[i][0]/max_score1[i][0]

for i in range(0, len(submits2)):
    total_sub2 += submits2[i][0]
    score2 += avg_score2[i][0] / max_score2[i][0]

for i in range(0, len(submits3)):
    total_sub3 += submits3[i][0]
    score3 += avg_score3[i][0] / max_score3[i][0]

print(total_sub1/len(submits1))
print(total_sub2/len(submits2))
print(total_sub3/len(submits3))
print(score1/len(submits1))
print(score2/len(submits2))
print(score3/len(submits3))
