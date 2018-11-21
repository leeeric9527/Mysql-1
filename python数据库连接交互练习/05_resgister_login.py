from mysqlfunction import Mysqlpython
from hashlib import sha1

menu = '''(1) 注册
(2)登录
(q)退出
请选择(1 / 2 / q ):'''
while True:
    choice = input(menu)
    if choice.strip()=='1':
        # 注册功能**************************************************
        # 先让用户输入用户名
        uname = input("请输入注册的用户名:")

        # 到数据库user表中查找
        sqlh = Mysqlpython('db5')
        sele = "select username from user where username=%s"
        r = sqlh.All(sele,[uname])
        if r:
            print("该用户名以存在")
            continue
        else:
            pwd1=input("请输入密码:")
            pwd2=input("请再次输入密码:")

            # 密码一致,注册成功的情况:
            if pwd1==pwd2:
                #对密码进行加密,存入数据库
                s = sha1() # 创建sha1加密对象
                s.update(pwd1.encode('utf8')) # 加密,pwd1为字节流
                pwd = s.hexdigest() # 返回十六进制加密结果
                ins = 'insert into user values(%s,%s)'
                sqlh.zhixing(ins,[uname,pwd])
                print("注册成功")
                break
            else:
                print('密码不一致\n')
                continue
    elif choice.strip() == '2':
        #登录功能**************************************************
        sqlh = Mysqlpython('db5')

        # 接受用户输入的用户名和密码
        uname=input("请输入用户名:")
        pwd = input("请输入密码:")
        s = sha1()
        s.update(pwd.encode('utf8'))
        pwd2 = s.hexdigest()

        # 到数据库中查询
        sel = "select password from user where username=%s"
        result = sqlh.All(sel,[uname])
        if len(result) == 0:
            print("用户名错误")
        elif result[0][0] == pwd2:
            print('登陆成功')
            break
        else:
            print('密码错误')
    elif choice.strip() =='q':
        break


