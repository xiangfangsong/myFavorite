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
        cursor.execute("SELECT id,username,role,ctime FROM login")
        data = cursor.fetchall();
        temp = {}
        result = []
        if(data!=None):
            for i in data:
                temp["id"]=i[0]
                temp["username"]=i[1]
                temp["role"]=i[2]
                temp["ctime"]=i[3]
                result.append(temp.copy())
            print("result: ",len(data))
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
            cursor.execute("INSERT INTO login(username,password,role) VALUES (\""+str(username)
                +"\",\""+str(password)+"\","+str(role)+")")
            db.commit()
            print("add a new user successfully")
            return "1"
        except Exception as e:
            print("add a new user failed: ",e)
            db.rollback()
            return "-1"

@app.route('/login/del', methods=['POST'])
def login_del():
    if request.method == "POST":
        id = request.form.get("id")
        try:
            cursor.execute("DELETE FROM login WHERE id="+str(id))
            db.commit()
            print("delete the user successfully")
            return "1"
        except Exception as e:
            print("delete the user failed: ",e)
            db.rollback()
            return "-1"

@app.route('/login/update', methods=['POST'])
def login_update():
    if request.method == "POST":
        id = request.form.get("id")
        password = request.form.get("password")
        try:
            cursor.execute("UPDATE login SET password=\""+str(password)+"\" where id="+str(id))
            db.commit()
            print("update successfully")
            return "1"
        except Exception as e:
            print("update failed: ",e)
            db.rollback()
            return "-1"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8899)
    db.close()
    print("Good bye!")
