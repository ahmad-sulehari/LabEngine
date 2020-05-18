from flask import Flask,render_template,url_for,request,redirect,g,session,Blueprint,flash

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



#@app.route("/byebye")
#def bye():
#    session.clear()
#    return render_template('login.html')


#@app.route("/patientProfile",methods=['POST'])
#def patientProfile():
#   if request.method == 'POST':
#      # session["pid"] = request.args.get('pid')
#        # session["password"] = request.args.get('password')
#
#       pid = request.form.get('pid')
#      session["pid"] = pid
#        print(pid)
#        # print(session["pid"])
#        error = None
#        try:
#            print("patientProfile")
#            pHistory = []
#            pHistory = db.getpHistory(pid)
#            return render_template('patient.html', pHistory=pHistory)
#
#        except Exception as e:
#            print(e)
#            error = str(e)
#            return render_template('patient.html', pHistory=pHistory)
#
def isloggedIn():
    if g.ID:
        if g.ID == 'PT':
            return 1
        elif g.ID == 'ST':
            isAdmin = db.checkAdmin(g.ID)
            if isAdmin:
                return 2
            else:
                return 3



@app.route("/report",methods=['POST','GET'])
def showReport():
    error = None
    try:
        print("pateinttestname_app.py")
        ptReportid = db.getpReports(session["ID"])
        ptTestName = []
        ptTestName = db.getTestName(ptReportid)
        return render_template('report.html', ptTestName=ptTestName)

    except Exception as e:
        print(e)
        error = str(e)
        return redirect(url_for('failure'))

@app.route("/viewReport",methods=['POST','GET'])
def getrepid():
    testname = request.form.get('testname')
    session["testname"] = testname
    error = None
    ptReportData = []
    try:
        print("getTestReportApp")
        teststatus = db.getptTestReportStatus(testname)
        if(teststatus):
            reportid = db.getpatientreportID(session["ID"])
            testrecordid = db.getptTestReportid(reportid, testname)
            ptReportData = db.getptTestReportData(testrecordid)
            return render_template('viewreport.html', ptReportData=ptReportData)
        else:
            return render_template('pendingrepo.html')

    except Exception as e:
        print(e)
        error = str(e)
        return render_template('viewreport.html', ptReportData=ptReportData)

@app.route("/patient/<isValid>")
def patient(isValid=False):
    if isValid:
        pHistory = []
        pHistory = db.getpHistory(session['ID'])
        return render_template('patient.html', pHistory=pHistory)
    return redirect(url_for('login'))



#@app.route("/admin", methods=['POST'])
#def dataEntry():
#   if request.method == 'POST':
#        return render_template('Patient_Data_Entry.html')

@app.route("/Staff/<isValid>")
def staff(isValid=False):
    if isValid:
        ID = session['ID']
        isAdmin = db.checkAdmin(ID)
        if isAdmin:
            return render_template('admin.html')
        staff_ID = ID
        print(staff_ID)
        profile_data = db.getStaffData(staff_ID)
        return render_template('worker.html', data=profile_data)
    return redirect(url_for('login'))

@app.route("/worker", methods=['POST'])
def staffProfile():
    staff_ID = request.form.get('ID')
    session["ID"] = staff_ID
    profile_data = db.getStaffData(staff_ID)
    return render_template('worker.html', data=profile_data)


@app.route("/editWorkerProfile", methods=['POST'])
def editWorkerProfile():
    staff_ID = session["ID"]
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
    #samples = request.form.get('numberOfSamples')
    doctor = request.form.get('doctor')
    pID = 'pt' + get_random_Numeric_string(5)
    print(pID)
    session["pID"] = pID
    reportID = 'rep' + get_random_Numeric_string(4)
    print(reportID)
    session["reportID"] = reportID
    #session["samples"] = samples
    password = get_random_alphaNumeric_string(6)
    print(password)
    inserted = db.insertPatient(pID,name, dateOfBirth, CNIC, gender, country, city, state, street, housenumber, email,
                               phoneNumber,password)

    reportInserted = db.insertReportEntry(reportID,pID,doctor,samples)
    if (inserted):
       print("Record is inserted")
       my_email = os.getenv('BDMS_EMAIL')
       email_passwd = os.getenv('BDMS_MAIL_PASSWORD')
       with smtplib.SMTP('smtp.gmail.com',587) as smtp:
           smtp.ehlo()
           smtp.starttls()
           smtp.ehlo()
           smtp.login(my_email,email_passwd)
           subject = 'Lab Engine: Low on Stock'
           body = 'your ID is '+pID+'\nPassword: '+password
           msg =  f'subject: {subject}\n\n{body}'
           smtp.sendmail(my_email,'bcsf17m036@pucit.edu.pk',msg)
       return render_template('TestRecordsEntry.html')
    else:
       profile_data = db.getStaffData(session["ID"])
       return render_template("worker.html",data=profile_data)

    reportInserted = db.insertReportEntry(reportID,pID,doctor)
    if (inserted):
        print("Record is inserted")
        allTests = db.getAllTests()
        patientTests = db.getPatientTests(session["reportID"])
        tests = db.getNewTests(allTests, patientTests)
        return render_template('TestRecordsEntry.html',tests = tests)
    else:
        profile_data = db.getStaffData(session["ID"])
        return render_template("worker.html",data=profile_data)




@app.route('/recordEntry', methods=['POST'])
def TestRecordEntry():
    test = request.form.get('testName')
    print(test)
    doctor = request.form.get('doctor')
    sampleType = request.form.get('sample')
    testRecordID = 'tr' + get_random_Numeric_string(5)
    print(testRecordID)
    session["testrecordID"] = testRecordID

    inserted = db.insertTestRecord(testRecordID,session["reportID"],test,doctor,sampleType)
    if (inserted):
        print("Test Record is inserted")
        #stock is deducted
        deducted = db.deductStock(test)
        updated = db.updateReport(session["reportID"], session["pID"])
        allTests = db.getAllTests()
        patientTests = db.getPatientTests(session["reportID"])
        tests = db.getNewTests(allTests,patientTests)
        return render_template('TestRecordsEntry.html',tests = tests)

    else:
        profile_data = db.getStaffData(session["ID"])
        return render_template("worker.html", data=profile_data)

@app.route('/endRecords', methods=['POST'])
def endRecords():
    print(session['ID'])
    updated = db.enterNoSamples(session["reportID"])
    profile_data = db.getStaffData(session['ID'])
    return render_template("worker.html", data=profile_data)

@app.route('/reportEntry')
def reportEntry():
    print(session['ID'])
    return render_template("ReportEntry.html",data = "")

@app.route('/enterReportData', methods=['POST'])
def reportDataEntry():
    print(session['ID'])
    patientID = request.form.get('pid')
    staffID = request.form.get('sid')
    reportID = request.form.get('rid')
    testrecordID = request.form.get('trid')
    date = request.form.get('date')
    protein = request.form.get('protein')
    albumin = request.form.get('albumin')
    globulin = request.form.get('globulin')
    bilirubin = request.form.get('bilirubin')
    ast = request.form.get('ast')
    alt = request.form.get('alt')
    alp = request.form.get('alp')
    rbc = request.form.get('rbc')
    wbc = request.form.get('wbc')
    platelet = request.form.get('platelet')
    hemoglobin = request.form.get('hemoglobin')
    urea = request.form.get('urea')
    creatinine = request.form.get('creatinine')
    uricAcid = request.form.get('uricAcid')
    inserted = db.enterTestRecordReport(testrecordID,reportID,staffID,patientID,date,protein,albumin,globulin,bilirubin,ast,alt,alp,rbc,wbc,platelet,hemoglobin,urea,creatinine,uricAcid)
    updated = db.updateTestRecordStatus(testrecordID)
    if(inserted):
        profile_data = db.getStaffData(session['ID'])
        return render_template("worker.html", data=profile_data)
    else:
        return render_template("ReportEntry.html",data="Report Not entered. Any of the IDs don't exist")


@app.route("/admin/<isValid>")
def admin(isValid=False):
    if isValid:
        return render_template('admin.html')
    return redirect(url_for('login'))



#Admin Update Stock
@app.route('/UpStock',methods=['GET','POST'])
def UpStock():
    return render_template('UpdateStock.html')

#Admin Report Record
@app.route('/rRecord',methods=['GET','POST'])
def viewRecord():
    result=db.viewReports()
    return render_template('viewTotalReport.html',result=result)

@app.route('/rDRecord',methods=['GET','POST'])
def dReport():
    return render_template('DeleteReport.html')


@app.route('/aE',methods=['GET','POST'])
def aE():
    return render_template('AdminEmail.html')


@app.route('/aP',methods=['GET','POST'])
def aP():
    return render_template('AdminPassword.html')

#Admin Patient Record
@app.route('/pRecord',methods=['GET','POST'])
def viewPatient():
    result=db.viewPatientRecord()
    return render_template('viewPatient.html',result=result)

@app.route('/pDRecord',methods=['GET','POST'])
def dpatient():
    return render_template('DeletePatientRecord.html')


#Admin Staff Record
@app.route('/viewStaff', methods=['GET'])
def viewStaffMethod():
    result=db.getStaffRecord()
    return render_template('viewStaffMembers.html',result=result)

@app.route('/DStaff',methods=['GET','POST'])
def dStaff():
    return render_template('DeleteStaff.html')


#admin Account
@app.route('/Account',methods=['GET','POST'])
def SAccount():
    return render_template('Account.html')


@app.route('/adminEmail',methods=['GET','POST'])
def AdminEmail():
    cAEmail=request.form.get('cAEmail')
    nAEmail=request.form.get('nAEmail')
    id = db.getAdminID1(cAEmail)
    if(id!=None):
        result=db.updateAdminEmail(id,nAEmail)
        if(result==True):
            flash("Admin email is Successfully Changed")
            return render_template('Admin.html')
        else:
            flash("Admin email is NOT Changed")
            return render_template('Admin.html')
    flash("Admin email is NOT Changed")
    return render_template('Admin.html')


@app.route('/adminPassword',methods=['GET','POST'])
def AdminPassword():
    cAPassword=request.form.get('cAPassword')
    nAPassword=request.form.get('nAPassword')
    id = db.getAdminID(cAPassword)
    if(id!=None):
        result=db.updateAdminPassword(id,nAPassword)
        if(result==True):
            flash("Admin password is Successfully Changed")
            return render_template('Admin.html')
        else:
            flash("Admin password is NOT Changed")
            return render_template('Admin.html')
    flash("Admin password is NOT Changed")
    return render_template('Admin.html')




@app.route("/404")
def failure():
    return render_template('404.html')



@app.route("/patientRecord")
def patientRecordEntry():
    return render_template('Patient_Data_Entry.html')



@app.route("/feedback", methods=['POST'])
def feedback():
    db=None
    error = None
    result1=None
    result2=None
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        db = DBHandler('localhost', app.config["DB_USER"], app.config["DB_PASSWORD"],
                       app.config["DATABASE"])
        result1 = db.getPatientID2(name, email)
        print("Aik lgani hai chal ja")
        if (result1 != False):
            print("Aik lgani hai chal ja 2")
            result2 = db.insertFeedback(result1,subject,message)
            if (result2 != True):
                flash("Feedback Not Sent!")
        else:
            flash("Your feedback have been Sent!")
    except Exception as e:
        print(e)
        error = str(e)
        return redirect(url_for('index', _anchor='feedBack'))
    finally:
        return redirect(url_for('index'))


@app.route('/checkFeedbacks', methods=['GET', 'POST'])
def pFeedBack():
    result = db.showFeedBack()
    return render_template('feedback.html', result=result)


@app.route('/adminPage', methods=['GET', 'POST'])
def adminView():
    return render_template('admin.html')



@app.route('/stockView', methods=['GET', 'POST'])
def stockView():
    result = db.showStockView()
    return render_template('stock.html', result=result)


@app.route('/updateStock', methods=['POST'])
def updateStock():
    error = None
    result2 = db.insertStock()
    if (result2 == True):
        print("Stock is successfully updated!")
        flash("Stock is successfully updated!")
    else:
        flash("Stock is not Updated!")
    return render_template('admin.html')

@app.route('/deleteStaff', methods=['GET', 'POST'])
def deleteStaff():
    staffID = request.form.get('staffID')
    cnic = request.form.get('sCnic')
    error = None
    id = db.getStaffID(staffID, cnic)
    if (id == None):
        flash("This id is not exit")
    else:
        db.deleteStaff(id)
        error = 'successfull'
        flash("Staff record is successfully removed")
    return render_template('admin.html', error=error)


@app.route('/deletePatient', methods=['GET','POST'])
def deletePatient():
    patientID = request.form.get('patientID')
    pName = request.form.get('pName')
    error = None
    id = db.getPatientID(patientID)
    if (id == None):
        flash("This id is not exit")
    else:
        db.deletePatient(patientID)
        error = 'successfull'
        flash("Patient record is successfully removed")
    return render_template('admin.html', error=error)




@app.route('/deleteReport', methods=['GET','POST'])
def deleteReport():
    patientID = request.form.get('patientID')
    reportID = request.form.get('reportID')
    error = None
    id = db.getPatientID(patientID)
    if (id == None):
        flash("This id is not exit")
    else:
        db.deleteReport(patientID,reportID)
        error = 'successfull'
        flash("Patient report is successfully removed")
    return render_template('admin.html', error=error)


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
