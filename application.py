from flask import Flask,render_template,url_for,request,redirect,g,session,Blueprint,flash
import os,smtplib
from DBHandler import DBHandler

import random
import string

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
    if not g.ID:
        if request.method == 'POST':
            return validate()
        else:
            return render_template('login.html')
    else:
        if g.ID.startswith('PT'):
            return redirect(url_for('patient',isValid=True))
        else:
            return redirect(url_for('staff',isValid=True))


def validate():
    try:
        session.pop('ID',None)
        user_ID = request.form['ID']
        user_password = request.form['password']
        if user_ID.startswith('st'):
            isValid = db.validateStaff(user_ID,user_password)
            if isValid:
                session['ID'] = user_ID
                return redirect(url_for('staff',isValid=True))
            else:
                return redirect(url_for('failure'))
                #return render_template('login.html',error='wrong credentials')
        done = db.validatePatient(user_ID,user_password)
        if done:
            session['ID'] = user_ID
            return redirect(url_for('patient',isValid=True))
        else:
            return redirect(url_for('failure'))
            #return render_template('login.html',error='wrong credentials')

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
        staff_ID = ID
        print(staff_ID)
        profile_data = db.getStaffData(staff_ID)
        return render_template('worker.html', data=profile_data)
    return redirect(url_for('login'))

@app.route("/worker", methods=['POST'])
def staffProfile():
    staff_ID = request.form.get('ID')
    print(staff_ID)
    session["staffID"] = staff_ID
    profile_data = db.getStaffData(staff_ID)
    return render_template('worker.html', data=profile_data)


@app.route("/editWorkerProfile", methods=['POST'])
def editWorkerProfile():
    staff_ID = session["staffID"]
    print(staff_ID)
    name = request.form.get('name')
    DOB = request.form.get('DOB')
    CNIC = request.form.get('CNIC')
    gender = request.form.get('gender')
    country = request.form.get('country')
    city = request.form.get('city')
    state = request.form.get('state')
    streetNo = request.form.get('streetNo')
    houseNo = request.form.get('houseNo')
    email = request.form.get('email')
    password = request.form.get('password')
    phoneNo = request.form.get('phoneNo')
    salary = request.form.get('salary')

    edited = db.editStaffData(staff_ID, name, DOB, CNIC, gender, country, city, state, streetNo, houseNo, email,
                              password, phoneNo, salary)
    profile_data = db.getStaffData(staff_ID)

    return render_template('worker.html', data=profile_data)


@app.route('/patientData', methods=['POST'])
def dataEntry():
    # id,name,birthdate,cnic,gender,country,city,state,streetno,house no,email,password,phone number,subject,message
    name = request.form.get('pname')
    print(name)
    dateOfBirth = request.form.get('DOB')
    CNIC = request.form.get('p_cnic')
    gender = request.form.get('pgender')
    country = request.form.get('country')
    city = request.form.get('city')
    state = request.form.get('state')
    street = request.form.get('street')
    housenumber = request.form.get('house')
    email = request.form.get('email')
    phoneNumber = request.form.get('phoneNumber')
    samples = request.form.get('numberOfSamples')
    doctor = request.form.get('doctor')
    pID = 'pt' + get_random_Numeric_string(5)
    print(pID)
    session["pID"] = pID
    reportID = 'rep' + get_random_Numeric_string(4)
    print(reportID)
    session["reportID"] = reportID
    session["samples"] = samples
    password = get_random_alphaNumeric_string(6)
    print(password)
    inserted = db.insertPatient(pID,name, dateOfBirth, CNIC, gender, country, city, state, street, housenumber, email,
                                phoneNumber,password)

    reportInserted = db.insertReportEntry(reportID,pID,doctor,samples)
    if (inserted):
        print("Record is inserted")
        return render_template('TestRecordsEntry.html')
    else:
        profile_data = db.getStaffData(session["staffID"])
        return render_template("worker.html",data=profile_data)



@app.route('/recordEntry', methods=['POST'])
def TestRecordEntry():
    test = request.form.get('testName')
    print(test)
    doctor = request.form.get('doctor')
    sampleType = request.form.get('sample')
    testRecordID = 'tr' + get_random_Numeric_string(5)
    print(testRecordID)
    #session["testrecord"] = testRecordID
    #reportID = 'rep' + get_random_Numeric_string(7)
    #print(reportID)
    #reportID =session["reportID"]
    #session["samples"] = 0
    samples = session["samples"]
    print(samples)

    inserted = db.insertTestRecord(testRecordID,session["reportID"],test,doctor,sampleType)
    if (inserted):
        print("Test Record is inserted")
        #stock is deducted
        deducted = db.deductStock(test)
        return render_template('TestRecordsEntry.html')
    else:
        profile_data = db.getStaffData(session["staffID"])
        return render_template("worker.html", data=profile_data)

@app.route('/endRecords', methods=['GET','POST'])
def endRecords():
    profile_data = db.getStaffData(session["staffID"])
    return render_template("worker.html", data=profile_data)

@app.route("/admin/<isValid>")
def admin(isValid=False):
    if isValid:
        return render_template('admin.html')
    return redirect(url_for('login'))


@app.route("/404")
def failure():
    return render_template('404.html')



@app.route("/patientRecord")
def patientRecordEntry():
    return render_template('Patient_Data_Entry.html')


@app.route("/patientRecord")
def patientRecord():
    return render_template('patientRecord.html')


@app.route('/feedback', methods=['POST'])
def feedback():
    error = None
    db = None
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        result1 = db.getPatientID2(name,email)
        if (result1 != None):
            result2 = db.insertFeedback(id, subject, message)
        else:
            flash("This patientID is invalid")
            return redirect(url_for('index'))

        if (result2 != True):
            flash("Feedback Not Sent!")
        else:
            flash("Your feedback have been Sent!")
            return redirect(url_for('index'))

    except Exception as e:
        print(e)
        error = str(e)
        return redirect(url_for('index', _anchor='feedBack'))


@app.route('/checkFeedbacks', methods=['GET', 'POST'])
def pFeedBack():
    result = db.showFeedBack()
    return render_template('feedback.html', result=result)


@app.route('/stockView', methods=['GET', 'POST'])
def stockView():
    result = db.showStockView()
    return render_template('stock.html', result=result)


@app.route('/updateStock', methods=['POST'])
def updateStock():
    error = None
    db = None
    try:
        result2 = db.insertStock()
        if (result2 == True):
            print("Stock is successfully updated!")
            flash("Stock is successfully updated!")
        else:
            flash("Stock is not updated!")
            return redirect(url_for('admin'))
    except Exception as e:
        print(e)
        error = str(e)
        return render_template('admin.html')


@app.route('/deleteStaff', methods=['GET', 'POST'])
def deleteStaff():
    staffID = request.form.get('staffID')
    cnic = request.form.get('cnic')
    error = None
    db = None
    db = DBHandler(app.config["DATABASE_IP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                   app.config["DATABASE"])
    id = db.getStaffID(staffID, cnic)
    if (id == None):
        flash("This id is not exit")
    else:
        db.deleteStaff(id)
        error = 'successfull'
        flash("Staff record is successfully removed")
    return render_template('index.html', error=error)

@app.route('/deletePatient', methods=['GET','POST'])
def deletePatient():
    patientID = request.form.get('pid')
    pName = request.form.get('pname')
    error = None
    id = db.getPatientID(patientID)
    if (id == None):
        flash("This id is not exit")
    else:
        db.deletePatient(id)
        error = 'successfull'
        flash("Patient record is successfully removed")
    return render_template('index.html', error=error)

@app.route('/dropsession')
def drop_session():
    session.pop('ID',None)
    return redirect(url_for('login'))

#for random numbers
def get_random_alphaNumeric_string(stringLength=8):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))

def get_random_Numeric_string(stringLength=8):
    Digits = string.digits
    return ''.join((random.choice(Digits) for i in range(stringLength)))

if __name__ == '__main__':
   app.run(debug=True)
