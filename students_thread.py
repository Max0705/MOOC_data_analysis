import db_operation as dbo
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from nmi import NMI
import time
# time1 = time.time()
#
# # 优秀1，合格2，不合格3
# post = dbo.select('post', 'view_students_thread')
# reply = dbo.select('reply', 'view_students_thread')
# comment = dbo.select('comment', 'view_students_thread')
# total = dbo.select('total', 'view_students_thread')
# liked = dbo.select('liked', 'view_students_thread')
# print("select post over")
#
# grade_level = dbo.select('gradelevel', 'view_students_thread')
# test_grade = dbo.select('testgrade', 'view_students_thread')
# homework_grade = dbo.select('homeworkgrade', 'view_students_thread')
# exam_grade = dbo.select('examgrade', 'view_students_thread')
# discussion_grade = dbo.select('discussiongrade', 'view_students_thread')
# final_grade = dbo.select('finalgrade', 'view_students_thread')
# print("select score over")
# time2 = time.time()
# print(time2-time1)
#
# # 修改列表格式，删除无成绩的数据
# df = pd.DataFrame(columns=['post', 'reply', 'comment', 'total', 'liked', 'test_grade', 'homework_grade', 'exam_grade', 'discussion_grade', 'final_grade', 'grade_level'])
# for i in range(0, len(post)):
#     temp_list = []
#     if grade_level[i][0] != '':
#         temp_list.append(post[i][0])
#         temp_list.append(reply[i][0])
#         temp_list.append(comment[i][0])
#         temp_list.append(total[i][0])
#         temp_list.append(liked[i][0])
#         temp_list.append(test_grade[i][0])
#         temp_list.append(homework_grade[i][0])
#         temp_list.append(exam_grade[i][0])
#         temp_list.append(discussion_grade[i][0])
#         temp_list.append(final_grade[i][0])
#         if grade_level[i][0] == '优秀':
#             temp_list.append(1)
#             print("xxxxx")
#         if grade_level[i][0] == '合格':
#             temp_list.append(2)
#         if grade_level[i][0] == '不合格':
#             temp_list.append(3)
#
#         df.loc[len(df)] = temp_list
#
# time3 = time.time()
# print(time3-time2)
#
# df.to_csv('students_thread/dataframe_temp.csv', index=False)
df = pd.read_csv('students_thread/dataframe_temp.csv')
print(df)

# 画图
# 无平均
for str in ['test_grade', 'homework_grade', 'exam_grade', 'discussion_grade', 'final_grade', 'grade_level']:
    plt.plot(df['post'], df[str], 'g.')
    plt.xlabel('post')
    plt.ylabel(str)
    plt.title('post-' + str)
    plt.savefig('students_thread/no_average/post-' + str + '.png')
    plt.show()

    plt.plot(df['reply'], df[str], 'g.')
    plt.xlabel('reply')
    plt.ylabel(str)
    plt.title('reply-' + str)
    plt.savefig('students_thread/no_average/reply-' + str + '.png')
    plt.show()

    plt.plot(df['comment'], df[str], 'g.')
    plt.xlabel('comment')
    plt.ylabel(str)
    plt.title('comment-' + str)
    plt.savefig('students_thread/no_average/comment-' + str + '.png')
    plt.show()

    plt.plot(df['total'], df[str], 'g.')
    plt.xlabel('total')
    plt.ylabel(str)
    plt.title('total-' + str)
    plt.savefig('students_thread/no_average/total-' + str + '.png')
    plt.show()

    plt.plot(df['liked'], df[str], 'g.')
    plt.xlabel('liked')
    plt.ylabel(str)
    plt.title('liked-' + str)
    plt.savefig('students_thread/no_average/liked-' + str + '.png')
    plt.show()

# 平均
for str in ['test_grade', 'homework_grade', 'exam_grade', 'discussion_grade', 'final_grade', 'grade_level']:
    df1 = df[['post', str]].groupby(['post']).mean().reset_index()
    plt.plot(df1['post'], df1[str], 'g-')
    plt.xlabel('post')
    plt.ylabel(str)
    plt.title('post-' + str)
    plt.savefig('students_thread/average/post-' + str + '.png')
    plt.show()

    df1 = df[['reply', str]].groupby(['reply']).mean().reset_index()
    plt.plot(df1['reply'], df1[str], 'g-')
    plt.xlabel('reply')
    plt.ylabel(str)
    plt.title('reply-' + str)
    plt.savefig('students_thread/average/reply-' + str + '.png')
    plt.show()

    df1 = df[['comment', str]].groupby(['comment']).mean().reset_index()
    plt.plot(df1['comment'], df1[str], 'g-')
    plt.xlabel('comment')
    plt.ylabel(str)
    plt.title('comment-' + str)
    plt.savefig('students_thread/average/comment-' + str + '.png')
    plt.show()

    df1 = df[['total', str]].groupby(['total']).mean().reset_index()
    plt.plot(df1['total'], df1[str], 'g-')
    plt.xlabel('total')
    plt.ylabel(str)
    plt.title('total-' + str)
    plt.savefig('students_thread/average/total-' + str + '.png')
    plt.show()

    df1 = df[['liked', str]].groupby(['liked']).mean().reset_index()
    plt.plot(df1['liked'], df1[str], 'g-')
    plt.xlabel('liked')
    plt.ylabel(str)
    plt.title('liked-' + str)
    plt.savefig('students_thread/average/liked-' + str + '.png')
    plt.show()

# 使用KMeans聚类
clf = KMeans(n_clusters=3)
data = np.array(df[['post', 'reply', 'comment', 'total', 'liked']])
clf.fit(data)
train = clf.labels_
test = np.array(df['grade_level'])
print(NMI(train, test))
print(test)
