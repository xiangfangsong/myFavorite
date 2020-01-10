# -*- coding: utf-8 -*-
import pymysql
from flask import Flask, request, jsonify
from flask_cors import CORS

#数据库连接
db = pymysql.connect("127.0.0.1","root","123456","myfavorite")
cursor = db.cursor()

#后端服务启动
app = Flask(__name__)
CORS(app, resources=r'/*')

@app.route('/login/list', methods=['POST'])
def login_list():
    if request.method == "POST":
        cursor.execute("select id,username,role,ctime from login")
        data = cursor.fetchall()
        temp={}
        result=[]
        if(data!=None):
            for i in data:
                temp["id"]=i[0]
                temp["username"]=i[1]
                temp["role"]=i[2]
                temp["ctime"]=i[3]
                result.append(temp.copy()) #特别注意要用copy，否则只是内存的引用
            print("result:",len(data))
            return jsonify(result)
        else:
            print("result: NULL")
            return jsonify([])

@app.route('/login/add', methods=['POST'])
def login_add():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        role = request.form.get("role")
        try:
            cursor.execute("insert into login(username,password,role) values (\""
                            +str(username)+"\",\""+str(password)+"\",\""+
                            str(role)+"\")")
            db.commit() #提交，使操作生效
            print("add a new user successfully!")
            return "1"
        except Exception as e:
            print("add a new user failed:",e)
            db.rollback() #发生错误就回滚
            return "-1"

@app.route('/login/login', methods=['POST'])
def login_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        cursor.execute("select id,username,role,ctime from login where username=\""
                       +str(username)+"\" and password=\""+str(password)+"\"")
        data = cursor.fetchone()
        if(data!=None):
            print("result:",data)
            jsondata = {"id":str(data[0]),"username":str(data[1]),
                        "role":str(data[2]),"ctime":str(data[3])}
            return jsonify(jsondata)
        else:
            print("result: NULL")
            jsondata = {}
            return jsonify(jsondata)

@app.route('/login/update', methods=['POST'])
def login_update():
    if request.method == "POST":
        id = request.form.get("id")
        password = request.form.get("password")
        try:
            cursor.execute("update login set password=\""+str(password)
                            +"\" where id="+str(id))
            db.commit()
            print("update password successfully!")
            return "1"
        except Exception as e:
            print("update password failed:",e)
            db.rollback() #发生错误就回滚
            return "-1"

@app.route('/login/update_role', methods=['POST'])
def login_update_role():
    if request.method == "POST":
        id = request.form.get("id")
        role = request.form.get("role")
        try:
            cursor.execute("update login set role=\""+str(role)
                            +"\" where id="+str(id))
            db.commit()
            print("update role successfully!")
            return "1"
        except Exception as e:
            print("update role failed:",e)
            db.rollback() #发生错误就回滚
            return "-1"

@app.route('/login/del', methods=['POST'])
def login_del():
    if request.method == "POST":
        id = request.form.get("id")
        try:
            cursor.execute("delete from login where id="+str(id))
            db.commit()
            print("delete user"+str(id)+" successfully!")
            return "1"
        except Exception as e:
            print("delete the user failed:",e)
            db.rollback() #发生错误就回滚
            return "-1"


@app.route('/favorite/list', methods=['POST'])
def favorite_list():
    if request.method == "POST":
        uid = request.form.get("uid")
        if(uid == 0): #查询全部公开的收藏数据
            cursor.execute("select id,wname,wurl,uid,type,count,ctime from favorite "
                           +"where type=0 order by count desc")
        else:
            cursor.execute("select id,wname,wurl,uid,type,count,ctime from favorite "
                           +"where type=0 or uid="+str(uid)+" order by count desc")
        data = cursor.fetchall()
        temp={}
        result=[]
        if(data!=None):
            for i in data:
                temp["id"]=i[0]
                temp["wname"]=i[1]
                temp["wurl"]=i[2]
                temp["uid"]=i[3]
                temp["type"]=i[4]
                temp["count"]=i[5]
                temp["ctime"]=i[6]
                result.append(temp.copy()) #特别注意要用copy，否则只是内存的引用
            print("result:",len(data))
            return jsonify(result)
        else:
            print("result: NULL")
            return jsonify([])

@app.route('/favorite/add', methods=['POST'])
def favorite_add():
    if request.method == "POST":
        wname = request.form.get("wname")
        wurl = request.form.get("wurl")
        uid = request.form.get("uid")
        _type = request.form.get("type")
        try:
            cursor.execute("insert into favorite(wname,wurl,uid,type) values (\""
                            +str(wname)+"\",\""+str(wurl)+"\",\""+str(uid)+"\",\""
                            +str(_type)+"\")")
            db.commit() #提交，使操作生效
            print("add a new favorite successfully!")
            return "1"
        except Exception as e:
            print("add a new favorite failed:",e)
            db.rollback() #发生错误就回滚
            return "-1"

@app.route('/favorite/del', methods=['POST'])
def favorite_del():
    if request.method == "POST":
        id = request.form.get("id")
        try:
            cursor.execute("delete from favorite where id="+str(id))
            db.commit()
            print("delete favorite"+str(id)+" successfully!")
            return "1"
        except Exception as e:
            print("delete the favorite failed:",e)
            db.rollback() #发生错误就回滚
            return "-1"
        
@app.route('/favorite/update', methods=['POST'])
def favorite_update():
    if request.method == "POST":
        id = request.form.get("id")
        wname = request.form.get("wname")
        wurl = request.form.get("wurl")
        _type = request.form.get("type")
        try:
            cursor.execute("update favorite set wname=\""+str(wname)
                            +"\", wurl=\""+str(wurl)+"\", type=\""
                            +str(_type)+"\" where id="+str(id))
            db.commit()
            print("update favorite successfully!")
            return "1"
        except Exception as e:
            print("update favorite failed:",e)
            db.rollback() #发生错误就回滚
            return "-1"

@app.route('/favorite/count', methods=['POST'])
def favorite_count():
    if request.method == "POST":
        id = request.form.get("id")
        try:
            cursor.execute("update favorite set count=count+1 where id="+str(id))
            db.commit()
            print("count successfully!")
            return "1"
        except Exception as e:
            print("count failed:",e)
            db.rollback() #发生错误就回滚
            return "-1"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=9090)
    db.close()
    print("Good bye!")
