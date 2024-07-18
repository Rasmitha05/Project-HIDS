from flask import Flask , request , render_template  ,session
import numpy as np 
import pandas as pd
from preprocess import modelp
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
import os


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

app.config["MONGO_URI"] = "mongodb://localhost:27017/apptest"
mongo = PyMongo(app)
app.secret_key  = os.urandom(24)

# mongo.db.users.insert_one({"index": 1,"name":"","email":"","password":"","Benign":0 , "Generic": 0 , "Exploits":0 , "Reconnaissance":0,"Fuzzers":0,"DoS":0,"Analysis":0,"Backdoors":0,"Worms":0,"Shellcode":0})
# mongo.db.users.insert_one({"index":1 , "name":"","email":"","password":""})


@app.route('/dashboard')
def home():
    return render_template("dashboard 3.html",name=session['name'])

@app.route('/team')
def team():
    return render_template("team.html",name=session['name'])


@app.route('/settings')
def settings():
    return render_template("setting.html",name=session['name'])

@app.route('/', methods = ['GET','POST'])
def login():
    if request.method =="POST":
        email = request.form.get("email")
        password = request.form.get("password")
        session['email'] = email
        user = mongo.db.users.find_one({"email":email})
        session['name'] = user['name']
        if email =="" or password =="":
            return render_template("login.html",error = "Enter all the details.")
        elif user and check_password_hash(user['password'],password):
            return render_template("dashboard 3.html",name = session['name'])
        else:
            return render_template("login.html",error="Wrong email or password.Please try again.")
            
    else:
        return render_template("login.html")

@app.route('/signup' , methods = ['GET','POST'])
def signup():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        existingUser = mongo.db.users.find_one({"email":email})
        if name=="" or email=="" or password == "":
            return render_template("signup.html",error="Enter all the details.")
        elif existingUser:
            return render_template("signup.html",error="User with same email already exists.")
        else:
            hashed_pass = generate_password_hash(password)
            mongo.db.users.insert_one({"index": 1,"name":name,"email":email,"password":hashed_pass,"Benign":0 , "Generic": 0 , "Exploits":0 , "Reconnaissance":0,"Fuzzers":0,"DoS":0,"Analysis":0,"Backdoors":0,"Worms":0,"Shellcode":0})
            return render_template("signup.html",success = "Account created. Login to continue.")
    else:
        return render_template("signup.html")

@app.route('/product', methods = ['GET','POST'])
def product():
    inputtxt=""
    email = session.get('email' , 'Def')
    # inputtxt = "175.45.176.0,41751,149.171.126.19,80,tcp,FIN,0.212162,768,9664,62,252,2,5,http,26093.26758,338382.9375,10,14,255,255,210689189,2498352965,77,690,1,4309,1183.576439,1177.47934,1424220060,1424220060,23.466444,14.715153,0.040095,0.020862,0.019233,0,1,1,, ,1,1,1,1,1,1,1"
    if request.method == "POST":
        try:
            inputtxt = request.form.get('inputcols')
            result = modelp(inputtxt)
            a = list(mongo.db.users.find({"email":email}))
            for dict in a:
                del dict['_id']
            mongo.db.users.update_one({"email":email},{"$set": {result:dict[result]+1}})
            if result=='Benign':
                return render_template("product.html",result=result,ans="Safe",name=session['name'])
            else:
                return render_template("product.html",result=result,ans="Not Safe(Malware)",name=session['name'])
        except Exception:
            pass
        result = "Enter inputs correctly"
        return render_template("product.html",result = result , name = session['name'])
    else:
        return render_template("product.html",result="Empty",name=session['name'])

@app.route('/analytics')
def analytics():
    email = session.get('email','Def')
    a = list(mongo.db.users.find({"email":email}))
    for dict in a:
        del dict['_id']
        Benign = dict['Benign']
        Generic = dict["Generic"]
        Exploits =dict["Exploits"]
        Reconnaissance = dict['Reconnaissance']
        Fuzzers = dict["Fuzzers"]
        DoS = dict["DoS"]
        Analysis = dict["Analysis"]
        Backdoors =dict['Backdoors']
        Worms = dict['Worms']
        Shellcode = dict["Shellcode"]
    return render_template("analytics.html",benign = Benign ,generic = Generic , exploits = Exploits , recon = Reconnaissance , fuzzers = Fuzzers , dos = DoS ,analysis = Analysis , backdoor = Backdoors , worms = Worms , shellcode = Shellcode,name=session['name'])

if __name__ == "__main__":
    app.run(debug=True,port = 5001)
