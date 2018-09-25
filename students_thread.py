import db_operation as dbo

re = dbo.select('*', 'view_students_thread')
print(re)
