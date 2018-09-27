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

# 画图并计算相关系数
file = open('students_thread/result.txt', 'w')
file.write('no average:\n')
# 无平均
for strt in ['test_grade', 'homework_grade', 'exam_grade', 'discussion_grade', 'final_grade', 'grade_level']:
    plt.plot(df['post'], df[strt], 'g.')
    plt.xlabel('post')
    plt.ylabel(strt)
    plt.title('post-' + strt)
    plt.savefig('students_thread/no_average/post-' + strt + '.png')
    plt.show()
    file.write('post-'+strt+'\t' + str(df['post'].corr(df[strt]))+'\n')

    plt.plot(df['reply'], df[strt], 'g.')
    plt.xlabel('reply')
    plt.ylabel(strt)
    plt.title('reply-' + strt)
    plt.savefig('students_thread/no_average/reply-' + strt + '.png')
    plt.show()
    file.write('reply-' + strt + '\t' + str(df['reply'].corr(df[strt]))+'\n')

    plt.plot(df['comment'], df[strt], 'g.')
    plt.xlabel('comment')
    plt.ylabel(strt)
    plt.title('comment-' + strt)
    plt.savefig('students_thread/no_average/comment-' + strt + '.png')
    plt.show()
    file.write('comment-' + strt + '\t' + str(df['comment'].corr(df[strt]))+'\n')

    plt.plot(df['total'], df[strt], 'g.')
    plt.xlabel('total')
    plt.ylabel(strt)
    plt.title('total-' + strt)
    plt.savefig('students_thread/no_average/total-' + strt + '.png')
    plt.show()
    file.write('total-' + strt + '\t' + str(df['total'].corr(df[strt]))+'\n')

    plt.plot(df['liked'], df[strt], 'g.')
    plt.xlabel('liked')
    plt.ylabel(strt)
    plt.title('liked-' + strt)
    plt.savefig('students_thread/no_average/liked-' + strt + '.png')
    plt.show()
    file.write('liked-' + strt + '\t' + str(df['liked'].corr(df[strt]))+'\n')

file.write('\n\naverage:\n')
# 平均
for strt in ['test_grade', 'homework_grade', 'exam_grade', 'discussion_grade', 'final_grade', 'grade_level']:
    df1 = df[['post', strt]].groupby(['post']).mean().reset_index()
    plt.plot(df1['post'], df1[strt], 'g-')
    plt.xlabel('post')
    plt.ylabel(strt)
    plt.title('post-' + strt)
    plt.savefig('students_thread/average/post-' + strt + '.png')
    plt.show()
    file.write('post-' + strt + '\t' + str(df1['post'].corr(df1[strt])) + '\n')

    df1 = df[['reply', strt]].groupby(['reply']).mean().reset_index()
    plt.plot(df1['reply'], df1[strt], 'g-')
    plt.xlabel('reply')
    plt.ylabel(strt)
    plt.title('reply-' + strt)
    plt.savefig('students_thread/average/reply-' + strt + '.png')
    plt.show()
    file.write('reply-' + strt + '\t' + str(df1['reply'].corr(df1[strt])) + '\n')

    df1 = df[['comment', strt]].groupby(['comment']).mean().reset_index()
    plt.plot(df1['comment'], df1[strt], 'g-')
    plt.xlabel('comment')
    plt.ylabel(strt)
    plt.title('comment-' + strt)
    plt.savefig('students_thread/average/comment-' + strt + '.png')
    plt.show()
    file.write('comment-' + strt + '\t' + str(df1['comment'].corr(df1[strt])) + '\n')

    df1 = df[['total', strt]].groupby(['total']).mean().reset_index()
    plt.plot(df1['total'], df1[strt], 'g-')
    plt.xlabel('total')
    plt.ylabel(strt)
    plt.title('total-' + strt)
    plt.savefig('students_thread/average/total-' + strt + '.png')
    plt.show()
    file.write('total-' + strt + '\t' + str(df1['total'].corr(df1[strt])) + '\n')

    df1 = df[['liked', strt]].groupby(['liked']).mean().reset_index()
    plt.plot(df1['liked'], df1[strt], 'g-')
    plt.xlabel('liked')
    plt.ylabel(strt)
    plt.title('liked-' + strt)
    plt.savefig('students_thread/average/liked-' + strt + '.png')
    plt.show()
    file.write('liked-' + strt + '\t' + str(df1['liked'].corr(df1[strt])) + '\n')



# # 使用KMeans聚类
# clf = KMeans(n_clusters=3)
# data = np.array(df[['post', 'reply', 'comment', 'total', 'liked']])
# clf.fit(data)
# train = clf.labels_
# test = np.array(df['grade_level'])
# print(NMI(train, test))
# print(test)
