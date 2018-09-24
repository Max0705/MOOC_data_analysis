import db_operation as dbo
import matplotlib.pyplot as plt
import pandas as pd

file = open("lesson_detail_result/lesson_detail_result.txt", "w")

x = ["1", "2", "3"]
y1 = []
y2 = []
# 老师批改1，系统评分2，学生互评3
submits1 = dbo.select_where('submits', 'lesson_detail', 'method like "%老师批改%"')
submits2 = dbo.select_where('submits', 'lesson_detail', 'method like "%系统评分%"')
submits3 = dbo.select_where('submits', 'lesson_detail', 'method like "%学生互评%"')
max_score1 = dbo.select_where('maxscore', 'lesson_detail', 'method like "%老师批改%"')
max_score2 = dbo.select_where('maxscore', 'lesson_detail', 'method like "%系统评分%"')
max_score3 = dbo.select_where('maxscore', 'lesson_detail', 'method like "%学生互评%"')
avg_score1 = dbo.select_where('averagescore', 'lesson_detail', 'method like "%老师批改%"')
avg_score2 = dbo.select_where('averagescore', 'lesson_detail', 'method like "%系统评分%"')
avg_score3 = dbo.select_where('averagescore', 'lesson_detail', 'method like "%学生互评%"')

total_sub1 = 0
total_sub2 = 0
total_sub3 = 0
score1 = 0
score2 = 0
score3 = 0

file.write("老师批改：\n")
if len(submits1) != 0:
    for i in range(0, len(submits1)):
        total_sub1 += submits1[i][0]
        score1 += avg_score1[i][0]/max_score1[i][0]
    y1.append(total_sub1 / len(submits1))
    y2.append(score1 / len(submits1))
    file.write(str(total_sub1 / len(submits1))+"\n")
    file.write(str(score1 / len(submits1))+"\n")
else:
    y1.append(0)
    y2.append(0)
    file.write("不存在\n")

file.write("系统评分：\n")
if len(submits2) != 0:
    for i in range(0, len(submits2)):
        total_sub2 += submits2[i][0]
        score2 += avg_score2[i][0] / max_score2[i][0]
    y1.append(total_sub2 / len(submits2))
    y2.append(score2 / len(submits2))
    file.write(str(total_sub2 / len(submits2))+"\n")
    file.write(str(score2 / len(submits2))+"\n")
else:
    y1.append(0)
    y2.append(0)
    file.write("不存在\n")

file.write("学生互评：\n")
if len(submits3) != 0:
    for i in range(0, len(submits3)):
        total_sub3 += submits3[i][0]
        score3 += avg_score3[i][0] / max_score3[i][0]
    y1.append(total_sub3 / len(submits3))
    y2.append(score3 / len(submits3))
    file.write(str(total_sub3 / len(submits3))+"\n")
    file.write(str(score3 / len(submits3))+"\n")
else:
    y1.append(0)
    y2.append(0)
    file.write("不存在\n")

plt.plot(x, y1, 'g-')
plt.savefig("lesson_detail_result/submits.png")
plt.show()
plt.plot(x, y2, 'g-')
plt.savefig("lesson_detail_result/score.png")
plt.show()

file.close()

# 相关性
method_list = dbo.select('method', 'lesson_detail')
submit_list = dbo.select('submits', 'lesson_detail')
max_score_list = dbo.select('maxscore', 'lesson_detail')
avg_score_list = dbo.select('averagescore', 'lesson_detail')

method_trans_list = []
for item in method_list:
    if "老师批改" in item[0]:
        method_trans_list.append(1)
        continue
    if "系统评分" in item[0]:
        method_trans_list.append(2)
        continue
    if "学生互评" in item[0]:
        method_trans_list.append(3)
        continue

score_trans_list = []
for i in range(0, len(max_score_list)):
    score_trans_list.append(avg_score_list[i][0]/max_score_list[i][0])

submit_trans_list = []
for item in submit_list:
    submit_trans_list.append(item[0])

method_trans_list = pd.Series(method_trans_list)
score_trans_list = pd.Series(score_trans_list)
submit_trans_list = pd.Series(submit_trans_list)

corr1 = method_trans_list.corr(score_trans_list)
corr2 = method_trans_list.corr(submit_trans_list)

print(corr1)
print(corr2)

