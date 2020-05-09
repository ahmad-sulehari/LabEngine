from flask import Flask,render_template,url_for,request,redirect,g,session
import os,smtplib
from DBHandler import DBHandler


app = Flask(__name__)

app.config.from_object('config')
app.secret_key=app.config["SECRET_KEY"]
db = DBHandler(app.config["DATABASE_IP"], app.config["DB_USER"], app.config["DB_PASSWORD"], app.config["DATABASE"])


@app.before_request
def before_request():
    g.ID=None
    if 'ID' in session:
        g.ID=session['ID']


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        validate()
    return render_template('login.html')


def validate():
    try:
        session.pop('ID',None)
        user_ID = request.form['ID']
        user_password = request.form['password']
        if user_ID.startswith('ST'):
            isValid = db.validateStaff(user_ID,user_password)
            if isValid:
                return redirect(url_for('staff',isValid=True))
            else:
                return redirect(url_for('login'))
        done= db.validatePatient(user_ID,user_password)
        if done:
            session['ID'] = user_ID;
            return redirect(url_for('patient',isValid=True))
        else:
            return redirect(url_for('login'))

    except Exception as e:
        print(e)
        error = str(e)
        return redirect(url_for('failure'))


@app.route("/patient/<isValid>")
def patient(isValid=False):
    if isValid:
        return render_template('patient.html')
    return redirect(url_for('login'))


@app.route("/Staff/<isValid>")
def staff(isValid=False):
    if isValid:
        ID = session['ID']
        isAdmin = db.checkAdmin(ID)
        if isAdmin:
            return redirect(url_for('admin'))
        return render_template('Staff.html')
    return redirect(url_for('login'))



@app.route("/admin/<isValid>")
def admin(isValid=False):
    if isValid:
        return render_template('admin.html')
    return redirect(url_for('login'))


@app.route("/404")
def failure():
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True)
