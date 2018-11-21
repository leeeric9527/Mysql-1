# import pymysql

# db = pymysql.connect(host='localhost',user='root',password='123456',database='db5',charset='utf8')
# cursor = db.cursor()

# sel = 'select * from t1'
# cursor.execute(sel)

# # All = cursor.fetchall()
# # for x in All:
# #     print(x)
# one=cursor.fetchone()
# print(one)
# print('*'*40)

# # fetchmany(2)
# Many = cursor.fetchmany(2)
# print(Many)
# print('*'*40)

# #fetchall()
# All = cursor.fetchall()
# print(All)

# db.commit()
# cursor.close()
# db.close()

import pymysql
#创建游标对象
db = pymysql.connect('localhost','root','123456','db5',charset='utf8',port=3306)
#创建游标对象
cur = db.cursor()
try:
    sel = 'select * from t1'
    cur.execute(sel)
    one = cur.fetchone()
    print(one)
    print('='*40)
    many = cur.fetchmany(2)
    print(many)
    All=cur.fetchall()
    print(All[1][1])
    db.commit()
except Exception as e:
    print("出现异常",e)
    db.rollback()
cur.close()
db.close()

