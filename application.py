from flask import Flask,render_template,url_for,request,redirect, session
from DBHandler import DBHandler

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = app.config["SECRET_KEY"]
db = DBHandler(app.config["DATABASE_IP"], app.config["DB_USER"], app.config["DB_PASSWORD"], app.config["DATABASE"])

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/byebye")
def bye():
    session.clear()
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
        try:
            print("patientProfile")
            pHistory = []
            pHistory = db.getpHistory(pid)
            return render_template('patient.html', pHistory=pHistory)

        except Exception as e:
            print(e)
            error = str(e)
            return render_template('patient.html', pHistory=pHistory)


@app.route("/report",methods=['POST','GET'])
def showReport():
    error = None
    try:
        print("pateinttestname_app.py")
        ptReportid = db.getpReports(session["pid"])
        ptTestName = []
        ptTestName = db.getTestName(ptReportid)
        return render_template('report.html', ptTestName=ptTestName)

    except Exception as e:
        print(e)
        error = str(e)
        return render_template('report.html')

@app.route("/viewReport",methods=['POST','GET'])
def getrepid():
    testname = request.form.get('testname')
    session["testname"] = testname
    error = None
    ptReportData = []
    try:
        print("getTestReportApp")
        teststatus = db.getptTestReportStatus(session["testname"])
        if(teststatus == 1):
            testrecordid = db.getptTestReportid(session["testname"])
            ptReportData = db.getptTestReportData(testrecordid)
            return render_template('viewreport.html', ptReportData=ptReportData)
        else:
            return render_template('pendingrepo.html')

    except Exception as e:
        print(e)
        error = str(e)
        return render_template('viewreport.html', ptReportData=ptReportData)



@app.route("/admin",methods=['POST','GET'])
def dataEntry():
    if request.method == 'POST':
        return render_template('Patient_Data_Entry.html')


@app.route("/worker")
def workerProfile():
    return render_template('Worker_Profile.html')


if __name__ == '__main__':
    app.run(debug=True)
