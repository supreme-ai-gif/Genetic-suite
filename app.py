from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
from utils import ai_generate

app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY") or "genetic_super_secret"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/genetic.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        if User.query.filter_by(username=username).first():
            return "Username already exists"
        db.session.add(User(username=username, password=password))
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password, request.form['password']):
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        return "Invalid login"
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/tool/<name>', methods=['GET', 'POST'])
def tool(name):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        text = request.form['text']
        result = ai_generate(name, text)
        return render_template('tool_result.html', name=name, result=result)
    return render_template('tool.html', name=name)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/terms")
def terms():
    return render_template("terms.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

if __name__ == '__main__':
    app.run(debug=True)
