from flask import Flask, request, render_template, url_for, redirect, sessions, session, Blueprint, flash
from DBHandler import DBHandler

app = Flask(__name__)
app.config.from_object('config')

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/patient", methods=['GET','POST'])
def patientProfile():
    if request.method == 'POST':
        return render_template('patient.html')


@app.route("/admin", methods=['POST'])
def dataEntry():
    if request.method == 'POST':
        return render_template('Patient_Data_Entry.html')


@app.route("/WorkerProfile", methods=['GET','POST'])
def new():
    name = request.form.get('q4_fullName4');
    print(name)
    return render_template('new.html', name=name)


@app.route("/worker")
def workerProfile():
    return render_template('Worker_Profile.html')


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
        db = DBHandler(app.config["DATABASE_IP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                   app.config["DATABASE"])
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
    db = DBHandler(app.config["DATABASE_IP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                   app.config["DATABASE"])
    result = db.showFeedBack()
    return render_template('feedback.html', result=result)


@app.route('/stockView', methods=['GET', 'POST'])
def stockView():
    db = DBHandler(app.config["DATABASE_IP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                   app.config["DATABASE"])
    result = db.showStockView()
    return render_template('stock.html', result=result)


@app.route('/updateStock', methods=['POST'])
def updateStock():
    error = None
    db = None
    try:
        db = DBHandler(app.config["DATABASE_IP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                   app.config["DATABASE"])
        result2 = db.insertStock()
        if (result2 == True):
            print("Stock is successfully updated!")
            flash("Stock is successfully updated!")
        else:
            flash("Stock is not updated!")
        render_template('admin.html')
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
    db = None
    db = DBHandler(app.config["DATABASE_IP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                   app.config["DATABASE"])
    id = db.getPatientID(patientID)
    if (id == None):
        flash("This id is not exit")
    else:
        db.deletePatient(id)
        error = 'successfull'
        flash("Patient record is successfully removed")
    return render_template('index.html', error=error)




if __name__ == '__main__':
   app.run(debug=True)
