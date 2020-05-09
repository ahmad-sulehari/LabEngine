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

@app.route("/WorkerProfile",methods=['POST'])
def new():
    #id,name,birthdate,cnic,gender,country,city,state,streetno,house no,email,password,phone number,subject,message
    name = request.form.get('pname')
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


    areaCode = request.form.get('areaCode')
    doctorsName = request.form.get('doctorsName')
    testName = request.form.get('testName')
    
    print(name)
    return render_template('new.html',name=name, pgender=gender,testName=testName)

@app.route("/worker")
def workerProfile():
    return render_template('Worker_Profile.html')


@app.route("/patientRecord")
def patientRecord():
    return render_template('patientRecord.html')

if __name__ == '__main__':
    app.run(debug=True)
