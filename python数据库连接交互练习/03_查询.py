import pymysql

db = pymysql.connect(host='localhost',user='root',password='123456',database='db5',charset='utf8')
cursor = db.cursor()

sel = 'select * from t1'
cursor.execute(sel)

# All = cursor.fetchall()
# for x in All:
#     print(x)
one=cursor.fetchone()
print(one)
print('*'*40)

# fetchmany(2)
Many = cursor.fetchmany(2)
print(Many)
print('*'*40)

#fetchall()
All = cursor.fetchall()
print(All)

db.commit()
cursor.close()
db.close()

