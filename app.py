from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

#adding in second page
@app.route('/Post')
def Post():
    return render_template('post.html')


if __name__ == "__main__":
    app.run(debug=True)

    