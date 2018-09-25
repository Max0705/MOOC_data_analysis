import db_operation as dbo
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (12.0, 4.0)
for i in range(4,14):
    x = dbo.select_where('CAST(date AS date) ', 'class_trend', "ClassId='"+str(i)+"'")
    y = dbo.select_where('CAST(NewPick AS signed)', 'class_trend', "ClassId='"+str(i)+"'")
    z = dbo.select_where('CAST(NewDrop AS signed)', 'class_trend', "ClassId='"+str(i)+"'")

    # print(x)
    # print(y)
    # print(z)

    plt.plot(x,y,"g-")
    plt.plot(x,z,"r-")

    plt.ylim(0,2400)

    plt.xlabel("date")
    plt.ylabel("number of students")

    plt.title("NewPick Student Number and Total Student Number"+" of Class"+str(i))

    plt.savefig("class_trend_result/class_trend" + str(i))
    plt.show()
    print(type(x))






