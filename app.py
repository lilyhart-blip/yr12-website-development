from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

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
    return render_template('index.html')

#adding in second
@app.route('/Post')
def Post():
    return render_template('post.html')

@app.route('/Home')
def Home():
    return render_template('index.html')

@app.route('/signup', methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        #try to find this user in the database- note- just keepin' it simple so usernames must be unique
        sql = "SELECT * FROM user WHERE username = ?"
        user = query_db(sql=sql,args=(username,),one=True)
        if user:
            #we got a user!!
            #check password matches-
            if check_password_hash(user[2],password):
                #we are logged in successfully
                #Store the username in the session
                session['user'] = user
                flash("Logged in successfully")
            else:
                flash("Password incorrect")
        else:
            flash("Username does not exist")
    return render_template('signup.html')

@app.route('/signuppage')
def signuppage():
    return render_template('signuppage.html')

def query_db(sql, args=(), one=False):
    '''connect and query- will retun one item if one=true and can accept arguments as tuple'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    cursor.execute(sql, args)
    results = cursor.fetchall()
    db.commit()
    db.close()
    return (results[0] if results else None) if one else results

if __name__ == "__main__":
    app.run(debug=True)

    