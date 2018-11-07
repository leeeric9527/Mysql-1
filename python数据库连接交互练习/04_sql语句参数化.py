import pymysql

db = pymysql.connect(host='localhost',user='root',password='123456',charset='utf8')
cursor = db.cursor()
cursor.execute('use db5')
name = input('请输入姓名:')
score = int(input('请输入成绩'))
try:
    ins= 'insert into t1(name,score) values(%s,%s)'
    # execute中第二个参数一定要为列表
    cursor.execute(ins,[name,score])
    db.commit()
    print('添加成功')
except:
    db.rollback()
cursor.close()
db.close()


如果没在创建数据连接对象后面的括号里添加charset=utf8;
那么在下面创建的游标对象中写cursor.execute("use db5")
name = ///
score= ///
try:
    ins = 'insert into t1(name,score) values(%s,%s)'
    cursor.execute(ins,[name,score])
    db.commit()
    print("添加成功")
except:
    db.rollback()
cursor.close()
db.close()
