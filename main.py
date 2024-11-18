from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/create')
def create():
    return render_template('Create.html')

@app.route('/update')
def update():
    return render_template('update.html')

@app.route('/information')
def information():
    return render_template('info.html')

@app.route('/settings')
def settings():
    return render_template('Settings.html')

@app.route('/account')
def account():
    return render_template('login.html')

@app.route('/contracts')
def contracts():
    return render_template('Signature.html')

@app.route('/Signature')
def signature():
    return render_template('Signature.html')

if __name__ == '__main__':
    app.run(debug=False)
