from flask import Flask, render_template, request, flash, session, redirect
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)

app.config['SECRET_KEY'] = "SuperSecret67"

DATABASE = "app.db"

def query_db(sql,args=(),one=False):
    '''connect and query- will retun one item if one=true and can accept arguments as tuple'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    cursor.execute(sql, args)
    results = cursor.fetchall()
    db.commit()
    db.close()
    return (results[0] if results else None) if one else results

@app.route('/')
def index():
    results = query_db("SELECT * FROM snake") 
    return render_template('index.html')

#adding in second route
@app.route('/Post')
def Post():
    return render_template('post.html')

@app.route('/Home')
def Home():
    return render_template('index.html')

@app.route('/Signup', methods=['GET', 'POST'])
def Signup():

    if request.method == "POST":

        username = request.form['username']

        password = request.form['password']

        hashed_password = generate_password_hash(password)

        sql = "INSERT INTO User (username, password) VALUES (?, ?);"   #create a query to insert ther data
        query_db(sql,(username, hashed_password))  #execute the query
        flash("Sign up Succsessful")
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/snake/<int:id>')
def snake(id):
    sql = "SELECT * FROM snake WHERE id=?"
    snake = query_db(sql,args=(id,),one=True)
    return render_template('Snakes.html', snake=snake)

if __name__ == "__main__":
    app.run(debug=True)

    