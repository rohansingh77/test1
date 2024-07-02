from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<html><h1>Hello, Flask! I am Rohan How are you</h1></html> "
@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
