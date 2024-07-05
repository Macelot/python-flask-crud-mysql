from flask import Flask
from flask import render_template,request,redirect
from flask import Flask
import mysql.connector

from utils import err
import math

app = Flask(__name__)

mysql=mysql.connector.connect(
   host="127.0.0.1",
   port="3306",
   user="root2",
   passwd="usbw",
   database="test"
)

def create_table():
    try:
        cur = mysql.cursor()
        cur.execute(
            '''
            CREATE TABLE IF NOT EXISTS cars (
                id INT AUTO_INCREMENT PRIMARY KEY ,
                `brand` varchar(30) NOT NULL,
                `model` varchar(30) NOT NULL,
                `price` varchar(10) NOT NULL
            )
            '''
        )
        mysql.commit()
        cur.close()
    except Exception as e:
        print("Error while creating table",e)
        
create_table()

@app.route("/list" , methods=['GET','POST'])
def list():
    if request.method == 'GET':
       req = request.args.get('pageno')
       pageno = int(req)
    else:
       pageno = 1
   
    no_of_records_per_page = 5;
    offset =  (int(pageno - 1)) * int(no_of_records_per_page)
    cursor_count = mysql.cursor()
    cursor_count.execute("SELECT COUNT(*) FROM cars")
    total_fetch = cursor_count.fetchall()
    total_rows = total_fetch[0][0]
    total_pages = math.ceil(total_rows / no_of_records_per_page)
    cursor = mysql.cursor()
    query = "SELECT * FROM cars LIMIT %s, %s"
    tuple1 = (offset, no_of_records_per_page)
    cursor.execute(query,tuple1)
    cars = cursor.fetchall()
    cursor.close()
    return render_template('list.html', cars=cars, pageno=pageno, total_pages=total_pages, total_rows=total_rows)

@app.route("/add", methods=['GET','POST'])
def add():
    if request.method == 'GET':
        errors = dict()
        return render_template('add.html', errors = errors)

    if request.method == 'POST':
        brand = request.form['brand']
        model = request.form['model']
        price = request.form['price']
        errors = err(brand,model,price)
        if errors:
            return render_template('add.html', errors = errors, brand = brand, model = model, price = price)
        else:
            cursor = mysql.cursor()
            sql = "INSERT INTO cars (brand, model, price) VALUES (%s, %s, %s)"
            val = (brand, model, price)
            cursor.execute(sql, val)
            mysql.commit()
            cursor.close()
            return redirect('/list?pageno=1')

@app.route("/edit/<int:id>", methods=['GET','POST'])
def edit(id):
    cursor = mysql.cursor()
    sql = "SELECT * FROM cars WHERE id= %s"
    val = (id,)
    cursor.execute(sql, val)
    car = cursor.fetchone()
    mysql.commit()
    cursor.close()
    errors = dict()
    if request.method == 'POST':
        brand = request.form['brand']
        model = request.form['model']
        price = request.form['price']
        errors = err(brand,model,price)
        if errors:
            return render_template('edit.html', errors = errors, car = car, brand = brand, model = model, price = price)
        else:
            cursor = mysql.cursor()
            sql = "UPDATE cars SET brand=%s, model=%s, price=%s WHERE id=%s"
            val = (brand, model, price, id)
            cursor.execute(sql, val)
            mysql.commit()
            cursor.close()
            return redirect('/list?pageno=1')

    return render_template('edit.html', car = car, errors = errors)

@app.route("/delete/<int:id>", methods=['GET','POST'])
def delete(id):
    cursor = mysql.cursor()
    sql = "DELETE FROM cars WHERE id= %s"
    val = (id,)
    cursor.execute(sql, val)
    mysql.commit()
    cursor.close()
    return redirect('/list?pageno=1')
