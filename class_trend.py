import db_operation as dbo

for i in range(4,15):
    x = dbo.select_where('Date', 'class_trend', "ClassId='i'")
    y = dbo.select_where('NewPick', 'class_trend', "ClassId='i'")
    z = dbo.select_where('NewDrop', 'class_trend', "Class_id='i'")



