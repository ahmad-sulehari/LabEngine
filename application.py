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

if __name__ == '__main__':
    app.run(debug=True)
