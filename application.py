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


@app.route("/WorkerProfile",methods=['POST'])
def new():
    name = request.form.get('q4_fullName4');
    print(name)
    return render_template('new.html',name=name)

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
def stockView():
    db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                   app.config["DATABASE"])
    result = db.showStockView()
    return render_template('stock.html', result=result)





@app.route('/updateStock', methods=['POST'])
def updateStock():
    error = None
    db = None
    try:

        mask = request.form['noFMasks']
        gloves = request.form['noFGloves']
        containers = request.form['noFContainers']
        swabs = request.form['noFSwabs']
        syringes = request.form['noFSyringes']
        glassware = request.form['noFGlassWare']
        sanitizors = request.form['noFSanitizors']
        cottonPkg = request.form['noFCottonPkg']
        reagents = request.form['noFReagents']

        db = DBHandler(app.config["DATABASEIP"], app.config["DB_USER"], app.config["DB_PASSWORD"],
                       app.config["DATABASE"])
        result1 = db.showStockView()
        if(result1!=None):
            mask=mask+result1[2]
            gloves= gloves + result1[3]
            containers = containers + result1[4]
            swabs = swabs + result1[5]
            syringes = syringes + result1[6]
            glassware = glassware + result1[7]
            sanitizors= sanitizors + result1[8]
            cottonPkg = cottonPkg + result1[9]
            reagents = reagents + result1[10]
            result2=db.insertStock(mask, gloves,containers,swabs,syringes,glassware,sanitizors,cottonPkg,reagents)
            if (result2 == True):
                flash("Stock is successfully updated!")
            else:
                flash("Stock is not updated!")
            return redirect(url_for('admin'))
        else:
            flash("Stock is not updated!")
            return redirect(url_for('admin'))

    except Exception as e:
        print(e)
        error = str(e)
        return redirect(url_for('admin'))


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
