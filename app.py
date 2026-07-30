from flask import Flask, render_template, request, flash, session, redirect
import sqlite3

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
    print('sanity check', request.method, request.form)
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
# if it is, then get data from request
# Then actually send that data to the DB
# Probably redirect or give user some 'toast' as success - flash
        flash("Sign up Succsessful")
    sql = "INSERT INTO User (userid, username, password) VALUES (?);"   #create a query to insert ther data
    query_db(sql,(item,))  #execute the query
    return render_template('signup.html')

@app.route('/signuppage')
def signuppage():
    return render_template('signuppage.html')

@app.route('/snake/<int:id>')
def snake(id):
    sql = "SELECT * FROM snake WHERE id=?"
    snake = query_db(sql,args=(id,),one=True)
    return render_template('Snakes.html', snake=snake)

if __name__ == "__main__":
    app.run(debug=True)

    