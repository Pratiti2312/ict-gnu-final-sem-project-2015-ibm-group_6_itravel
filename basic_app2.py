from flask import Flask,jsonify,request
import math
import mysql.connector
from datetime import datetime
import os

mydb = mysql.connector.connect(
  host="sl-eu-gb-p05.dblayer.com",
  port="17743",
  user="admin",
  passwd="SDRCMXOYSYJHEKJL",
  database="compose"
)
mycursor = mydb.cursor()

app=Flask(__name__)
port = int(os.getenv('PORT', 8000))

@app.route('/retrivedata/<string:email>',methods=['GET'])
def retriveData(email):
    sql = "select claim_id,email,check_in,check_out,cost,creation_date from claim where email=%s"
    val=(email)
    mycursor.execute(sql,(email,))
    records = mycursor.fetchall()
    if(len(records)>0):
        return jsonify({'Result':records})
    else:
        return jsonify({'Result':'null'})

@app.route('/',methods=['GET', 'POST'])
def index():
    if(request.method=='POST'):
        some_json=request.get_json()
        return jsonify({'you sent':some_json}), 201
    else:
        return jsonify({"about":"Hello World"})

@app.route('/claim/<string:email>/<string:cord1>/<string:cord2>',methods=['GET'])
def claim(email,cord1,cord2):
    arr1=cord1.split(',')
    arr2=cord2.split(',')
    t1=[]
    t2=[]
    for i in arr1:
        t1.append(float(i))
    for i in arr2:
        t2.append(float(i))

    lon1,lat1=t1
    lon2,lat2=t2
    R=6371000                               
    phi_1=math.radians(lat1)
    phi_2=math.radians(lat2)

    delta_phi=math.radians(lat2-lat1)
    delta_lambda=math.radians(lon2-lon1)

    a=math.sin(delta_phi/2.0)**2+\
    math.cos(phi_1)*math.cos(phi_2)*\
    math.sin(delta_lambda/2.0)**2
    c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))
    meters=R*c     
    km=meters/1000.0
    ex=km*0.6*71.14
    sql = "INSERT INTO claim(email,check_in,check_out,cost,creation_date) VALUES (%s,%s,%s,%s,%s)"
    val = (email,cord1,cord2,ex,datetime.now())
    mycursor.execute(sql,val)
    mydb.commit()
    return jsonify({'Expense':ex})
@app.route('/signup/<string:username>/<string:email>/<string:password>',methods=['GET'])
def signup(username,email,password):
    sql = "INSERT INTO user_info(username,email,password) VALUES (%s,%s,%s)"
    val = (username,email,password)
    mycursor.execute(sql,val)
    mydb.commit()
    return jsonify({'Result':'Data inserted successfully'})
@app.route('/login/<string:email>/<string:password>',methods=['GET'])
def login(email,password):
    sql = "select username from user_info where email=%s and password=%s"
    val = (email,password)
    mycursor.execute(sql,val)
    records = mycursor.fetchall()
    if(len(records)>0):
        temp=records[0][0]
        return jsonify({'Result':temp})
    else:
        return jsonify({'Result':'null'})
if __name__=='__main__':
    app.run(host='0.0.0.0', port=port)
