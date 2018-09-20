import pymysql


def select(str):
    db = pymysql.connect(host='139.199.6.55', port=3306, user='MOOC', passwd='iX5&iKapuC23VCG', db='mooc')

    cursor = db.cursor()

    sql = "select * from " + str

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        print('successfully select')
        return results
    except:
        print('error')
    finally:
        cursor.close()
        db.close()


if __name__ == '__main__':
    re = select('lesson_detail')
    print(re)
