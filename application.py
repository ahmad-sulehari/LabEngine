from flask import Flask,render_template,url_for,request,redirect
app = Flask(__name__)


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
        result = db.insertFeedback(name, email, subject, message)
        if (result != True):
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



@app.route('/updateStock', methods=['POST'])
def feedback():
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
        mask=mask+result1[2]
        gloves= gloves + result1[3]
        containers = containers + result1[4]
        swabs = swabs + result1[5]
        syringes = syringes + result1[6]
        glassware = glassware + result1[7]
        sanitizors= sanitizors + result1[8]
        cottonPkg = cottonPkg + result1[9]
        reagents = reagents + result1[10]

        result2=db.insertStock()
        if (result2 != True):
            flash("Stock is successfully updated!")
        else:
            flash("Stock is not updated!")
            return redirect(url_for('admin'))

    except Exception as e:
        print(e)
        error = str(e)
        return redirect(url_for('admin'))



if __name__ == '__main__':
    app.run(debug=True)
