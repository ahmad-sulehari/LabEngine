import pymysql
import random
import string

def get_random_alphaNumeric_string(stringLength=10):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))

def get_random_Numeric_string(stringLength=8):
    Digits = string.digits
    return ''.join((random.choice(Digits) for i in range(stringLength)))

class DBHandler:
    def __init__(self,DATABASEIP,DB_USER,DB_PASSWORD,DATABASE):
        self.DATABASEIP=DATABASEIP
        self.DB_USER=DB_USER
        self.DB_PASSWORD=DB_PASSWORD
        self.DATABASE=DATABASE

    def __del__(self):
        print("Destructor")


        def insertFeedback(self, id, subject, message):
            db = None
            cursor = None
            insert = False
            try:
                db = pymysql.connect(host=self.DATABASEIP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                     database=self.DATABASE)
                cur = db.cursor()
                sql = 'update patient set subject=%s,message=%s where patientID=%s'
                args = ( subject, message,id)
                cur.execute(sql, args)
                insert = True

            except Exception as e:
                print(e)
                print("some error")
            finally:
                if (db != None):
                    db.commit()
            return insert


        def insertStock(self, mask, gloves, containers,swabs,syringes,glassware,sanitizors,cottonPkg,reagents):
            db = None
            cursor = None
            insert = False
            try:
                db = pymysql.connect(host=self.DATABASEIP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                     database=self.DATABASE)
                cur = db.cursor()
                sql = 'insert into test (noFMasks, noFGloves, noFContainers, noFSwabs,noFSyringes,noFGlassWare,noFSanitizors,noFCottonPkg,noFReagents) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                args = (mask, gloves, containers,swabs,syringes,glassware,sanitizors,cottonPkg,reagents)
                cur.execute(sql, args)
                insert = True

            except Exception as e:
                print(e)
                print("some error")
            finally:
                if (db != None):
                    db.commit()
            return insert





    def getPatientID(self,id):
        db = None
        cursor = None
        try:
            db = pymysql.connect(host=self.DATABASEIP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'select * from patient where patientID=%s'
            args = (id)
            cur.execute(sql,args)
            result = cur.fetchone()
            return result[0]
        except Exception as e:
            print(e)

    def getStaffID(self,id,cnic):
        db = None
        cursor = None
        try:
            db = pymysql.connect(host=self.DATABASEIP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'select * from staff where staffID=%s'
            args = (id)
            cur.execute(sql, args)
            result = cur.fetchone()
            return result[0]
        except Exception as e:
            print(e)


    def deleteStaff(self,id):
        db = None
        cursor = None
        try:
            db = pymysql.connect(host=self.DATABASEIP, port=3307, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'Delete from staff where id = %s'
            args = (id)
            result = cur.execute(sql, args)
            db.commit()
            if (result == None):
                return False
            else:
                return True
        except Exception as e:
            print(e)
            return False

    def insertPatient(self,name,dob,cnic,gender,country,city,state,streetNo,houseNo,email,phoneNo):
        # id,name,birthdate,cnic,gender,country,city,state,streetNo,house no,email,password,phone number,subject,message
        db = None
        cursor = None
        insert = False
        try:
            print("Inserting patient")
            db = pymysql.connect(host=self.DATABASEIP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            p_id = 'pt' + get_random_Numeric_string()
            print(p_id)
            session["p_id"]=p_id
            reportID = 'rep' + get_random_Numeric_string(7)
            print(reportID)
            session["reportID"]=reportID
            password = get_random_alphaNumeric_string()
            print(password)
            sql = 'Insert into patient (patientID,pName,pBirthdate,pCNIC,pGender,pCountry,pCity,pState,pStreetNo,pHouseNo,pEmail,pPassword,pPhoneNo) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            args = (p_id,name,dob,cnic,gender,country,city,state,streetNo,houseNo,email,password,phoneNo)
            cur.execute(sql, args)
            insert = True
        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return insert


    def getStaffData(self,staff_ID):
        db = None
        cursor = None
        valid = False
        data =[]
        try:
            print("Getting staff data")
            db = pymysql.connect(host=self.DATABASEIP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'Select * from staff where staffID = '+ '%s'
            args = (staff_ID)
            cur.execute(sql, args)
            data = cur.fetchone();
            if (data != None):
                valid = True
        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return data

    def editStaffData(self,staff_ID,name,DOB,CNIC,gender,country,city,state,streetNo,houseNo,email,password,phoneNo,salary):
        db = None
        cursor = None
        edited = False
        data =[]
        try:
            print("editting staff data")
            db = pymysql.connect(host=self.DATABASEIP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'update staff set sName = ' + '%s' + ' ,sBirthdate = ' + '%s' + ', sCNIC = ' + '%s' + ', sGender = ' + '%s' + ', sCountry = '+'%s' + ', sCity = '+'%s'+ ', sState = '\
                  +'%s' + ', sStreetNo = '+'%s'+ ', sHouseNo = '+'%s' + ', sEmail = '+'%s'+ ', sPassword = '+'%s' + ', sPhoneNo = '+'%s where staffID = ' +'%s'
            args = (name,DOB,CNIC,gender,country,city,state, streetNo,houseNo,email,password,phoneNo,staff_ID)
            cur.execute(sql, args)
            data = cur.fetchone();
            edited = True
        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return edited


    def showFeedBack(self):
        db = None
        cursor = None
        try:
            db = pymysql.connect(host=self.DATABASEIP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            print("here")
            sql = 'Select * from feedback'
            cur.execute(sql)
            result = cur.fetchall()

        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return result

        def showStockView(self):
            db = None
            cursor = None
            try:
                db = pymysql.connect(host=self.DATABASEIP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                     database=self.DATABASE)
                cur = db.cursor()
                print("here")
                sql = 'Select * from test'
                cur.execute(sql)
                result = cur.fetchall()

            except Exception as e:
                print(e)
                print("some error")
            finally:
                if (db != None):
                    db.commit()
                return result