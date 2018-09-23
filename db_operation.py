import pymysql

def select(row, table):
    db = pymysql.connect(host='139.199.6.55', port=3306, user='MOOC', passwd='iX5&iKapuC23VCG', db='mooc')

    cursor = db.cursor()

    sql = "select " + row + " from " + table

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        print('successfully select')
        return results
    except Exception:
        print('error')
        print(Exception)
    finally:
        cursor.close()
        db.close()


def select_where(row, table, con):
    db = pymysql.connect(host='139.199.6.55', port=3306, user='MOOC', passwd='iX5&iKapuC23VCG', db='mooc')

    cursor = db.cursor()

    sql = "select " + row + " from " + table + " where " + con

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        print('successfully select')
        return results
    except Exception:
        print('error')
        print(Exception)
    finally:
        cursor.close()
        db.close()


if __name__ == '__main__':
    re = select('*', 'lesson_detail')
    print(re)
