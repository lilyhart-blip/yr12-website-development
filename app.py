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

@app.route('/Signup', methods=['GET', 'POST'])
def Signup():
        if request.method == "POST":
            username = request.form['username']
            password = request.form['password']
    # if it is, then get data from request
    # Then actually send that data to the DB
    # Probably redirect or give user some 'toast' as success - flash
        flash("Sign up Succsessful")
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

    