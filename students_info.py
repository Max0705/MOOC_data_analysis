import db_operation as dbo

re = dbo.select('*', 'view_students_info')
print(re)
