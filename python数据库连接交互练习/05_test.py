from mysqlfunction import Mysqlpython


sqlh = Mysqlpython('db5')
sqlh.zhixing("update t1 set score=100")

r = sqlh.All('select * from t1')
for x in r:
    print(x)
print("--------------------")

c = sqlh.Many('select * from t1',1)
print(c)
b = sqlh.All("select * from t1")
print(b)

