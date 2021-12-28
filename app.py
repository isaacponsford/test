from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        username_content = request.form['username']
        password_content = request.form['password']
        print(username_content)
        print(password_content)
        return redirect('/')
    else:
        return render_template('index.html')

@app.route('/log-in')
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)