from flask import Flask,render_template,url_for,redirect,request
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="VPK@2003"
app.config["MYSQL_DB"]="contact"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql=MySQL(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add",methods=["GET","POST"])
def add():
    if request.method=='POST':
        cname=request.form['cname']
        mno=request.form['mno']
        mail=request.form['mail']
        addr=request.form['addr']
        con=mysql.connection.cursor()
        sql="insert into contact_det(cname,cno,email,address) value(%s,%s,%s,%s)"
        con.execute(sql,[cname,mno,mail,addr])
        mysql.connection.commit()
        con.close()
        return redirect(url_for("home"))
    return render_template("add.html")   

@app.route("/view")
def view():
    con= mysql.connection.cursor()
    sql="SELECT cid,cname,cno,email,address from contact_det"
    con.execute(sql)
    res=con.fetchall()  
    return render_template("view.html",datas=res)

@app.route("/update/<string:cid>",methods=["GET","POST"])
def edit(cid):
    
    if request.method=='POST':
        cname=request.form['cname']
        mno=request.form['mno']
        email=request.form['email']
        address=request.form['address']
        con=mysql.connection.cursor()
        sql="update contact_det set cname=%s,cno=%s,email=%s,address=%s where cid=%s"
        con.execute(sql,[cname,mno,email,address,cid])
        mysql.connection.commit()
        con.close()
        return redirect(url_for("view"))
        
    con=mysql.connection.cursor()
    sql="select * from contact_det where cid=%s"
    con.execute(sql,[cid])
    res=con.fetchone()
    return  render_template("update.html",datas=res) 


@app.route("/delete/<string:id>",methods=["GET","POST"])
def delete(id):
    con=mysql.connection.cursor()
    sql="delete from contact_det where cid=%s"
    con.execute(sql,[id])
    mysql.connection.commit()
    con.close()
    return redirect(url_for("view"))  
@app.route("/search")
def search():
  
    return render_template("search.html")
 
@app.route("/searchshow",methods=["GET","POST"])
def searchshow():
    if request.method=='POST':
        cname=request.form['cname']
        mno=request.form['cno']
       
        con=mysql.connection.cursor()
        sql="select * from contact_det where cname=%s or cno=%s"
        con.execute(sql,[cname,mno])
        res=con.fetchall()
        mysql.connection.commit()
        con.close()
        return render_template("searchshow.html",datas=res)
    return render_template("searchshow.html")

if(__name__=='__main__'):
    app.run(debug=True)    
