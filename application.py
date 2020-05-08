
from flask import Flask,render_template,url_for,request,redirect, session
from DBHandler import DBHandler

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = app.config["SECRET_KEY"]

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/patient",methods=['POST'])
def patientProfile():
    if request.method == 'POST':
        #session["pid"] = request.args.get('pid')
        #session["password"] = request.args.get('password')

        pid = request.form.get('pid')
        session["pid"]=pid
        print(pid)
        #print(session["pid"])
        error = None
        db = None
        try:
            db = DBHandler("localhost", "root", "jimin123", "labengine")
            print("patientProfile")
            pHistory = []
            pHistory = db.getpHistory(pid)
            return render_template('patient.html', pHistory=pHistory)

        except Exception as e:
            print(e)
            error = str(e)
            return render_template('patient.html')


app.route('/report', methods=['POST'])
def showReport():
    if request.method == 'POST':
        error = None
        db = None
        try:
            db = DBHandler("localhost", "root", "jimin123", "labengine")
            print("patientProfile")
            ptReports = []
            ptReports = db.getpReports(session["pid"])
            return render_template('patientReport.html', ptReports=ptReports)

        except Exception as e:
            print(e)
            error = str(e)


@app.route("/admin",methods=['POST'])
def dataEntry():
    if request.method == 'POST':
        return render_template('Patient_Data_Entry.html')


@app.route("/worker")
def workerProfile():
    return render_template('Worker_Profile.html')

@app.route("/patientRecord")
def patientRecord():
    return render_template('patientRecord.html')


if __name__ == '__main__':
    app.run(debug=True)
