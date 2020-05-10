from flask import Flask,render_template,url_for,request,redirect,session
app = Flask(__name__)
from DBHandler import DBHandler

app.config.from_object('config')
app.secret_key=app.config["SECRET_KEY"]
db = DBHandler(app.config["DATABASE_IP"], app.config["DB_USER"], app.config["DB_PASSWORD"], app.config["DATABASE"])

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/patient",methods=['POST'])
def patientProfile():
    if request.method == 'POST':
        return render_template('patient.html')


@app.route("/staffLogin",methods=['POST'])
def showWorkerProfile():
    staff_ID = request.form.get('staffID')
    print(staff_ID)
    session["staffID"] = staff_ID
    profile_data = db.getStaffData(staff_ID)
    return render_template('worker.html', data = profile_data)


@app.route("/editWorkerProfile",methods=['POST'])
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

    edited = db.editStaffData(staff_ID,name,DOB,CNIC,gender,country,city,state,streetNo,houseNo,email,password,phoneNo,salary)
    profile_data = db.getStaffData(staff_ID)
    
    return render_template('worker.html', data=profile_data)



@app.route('/WorkerProfile',methods=['POST', 'GET'])
def dataEntry():
    #id,name,birthdate,cnic,gender,country,city,state,streetno,house no,email,password,phone number,subject,message
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
    inserted = db.insertPatient(name,dateOfBirth,CNIC,gender,country,city,state,street,housenumber,email,phoneNumber)
    #patient personal data entry
    #testrecords
    #
    #report
    areaCode = request.form.get('areaCode')
    doctorsName = request.form.get('doctorsName')
    testName = request.form.get('testName')
    if(inserted):
        print("Record is inserted")
    print(name)
    return render_template('new.html',name=name, pgender=gender,testName=testName)

@app.route("/patientData")
def patientDataEntry():
    return render_template('Patient_Data_Entry.html')


@app.route("/patientRecord")
def patientRecord():
    return render_template('patientRecord.html')


@app.route('/feedback', methods=['POST'])
def feedback():
    error = None
    db = None
    try:
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                       app.config["DATABASE"])
        result1=db.getUserId()
        if (result1 != None):
            result2 = db.insertFeedback(id, subject, message)
        else:
            flash="This patientID is invalid"
            return redirect(url_for('index'),anchor='feedback')

        if (result2 != True):
            flash("Feedback Not Sent!")
        else:
            flash("Your feedback have been Sent!")
            return redirect(url_for('index', _anchor='feedBack'))

    except Exception as e:
        print(e)
        error = str(e)
        return redirect(url_for('index', _anchor='feedBack'))





@app.route('/checkFeedbacks', methods=['GET', 'POST'])
def pFeedBack():
    db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                   app.config["DATABASE"])
    result = db.showFeedBack()
    return render_template('feedbacks.html', result=result)





@app.route('/stockView', methods=['GET', 'POST'])
def userFeedBack():
    db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                   app.config["DATABASE"])
    result = db.showStockView()
    return render_template('stock.html', result=result)


@app.route("/deleteStaff", methods=["GET", "POST"])
def deleteStaff():
    staffID = request.form["staffID"]
    cnic = request.form["cnic"]
    error = None
    db = None
    db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"], app.config["DATABASE"])
    id = db.getStaffID(staffID,cnic)
    if (id == None):
        error="This id is not exit"
    else:
        db.deleteStaff(id)
        error='successfull'

    return render_template('deleteUser.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)
