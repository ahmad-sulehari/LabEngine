import pymysql
import smtplib,os
from flask import session

import random
import string

def get_random_alphaNumeric_string(stringLength=8):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))

def get_random_Numeric_string(stringLength=8):
    Digits = string.digits
    return ''.join((random.choice(Digits) for i in range(stringLength)))

class DBHandler:
    def __init__(self, DATABASE_IP, DB_USER, DB_PASSWORD, DATABASE):
        self.DATABASE_IP = DATABASE_IP
        self.DB_USER = DB_USER
        self.DB_PASSWORD = DB_PASSWORD
        self.DATABASE = DATABASE


    def __del__(self):
        print("Destructor")

    def insertFeedback(self, id, subject, message):
        db = None
        cursor = None
        insert = False
        try:
            db = pymysql.connect(host=DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'update patient set subject=%s, message=%s where patientID=%s'
            args = (subject, message, id)
            cur.execute(sql, args)
            db.commit()
            insert = True

        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
        return insert


    def getStockQty(self):
        db = None
        cursor = None
        try:
            db = pymysql.connect(host=DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                    database=self.DATABASE)
            cur = db.cursor()
            sql = 'select itemQuantity from stock'
            cur.execute(sql)
            result = cur.fetchall()
            return result
        except Exception as e:
            print(e)

    def insertStock(self):
        db = None
        cursor = None
        insert = False
        try:
            db = pymysql.connect(host=DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'update stock set itemQuantity =40 '
            cur.execute(sql)
            insert = True

        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
        return insert



        def insertFeedback(self, id, subject, message):
            db = None
            cursor = None
            insert = False
            try:
                db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
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




    def getPatientID(self, id):
        db = None
        cursor = None
        try:
            db = pymysql.connect(host=DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'select * from patient where patientID=%s'
            args = (id)
            cur.execute(sql, args)
            result = cur.fetchall()
            return result[0]
        except Exception as e:
            print(e)


    def getPatientID2(self, name,email):
        db = None
        cursor = None
        try:
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'select patientID from patient where pName=%s AND pEmail=%s'
            args = (name,email)
            cur.execute(sql, args)
            result = cur.fetchone()
            return result[0]
        except Exception as e:
            print(e)


    def getStaffID(self, id, cnic):
        db = None
        cursor = None
        try:
            db = pymysql.connect(host=self.DATABASE_IP, port=3307, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'select * from staff where staffID=%s AND sCNIC=%s'
            args = (id,cnic)
            cur.execute(sql, args)
            result = cur.fetchone()
            return result[0]
        except Exception as e:
            print(e)

    def deleteStaff(self, id):
        db = None
        cursor = None
        try:
            db = pymysql.connect(host=DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'Delete from staff where staffID = %s'
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

    def deletePatient(self, id):
        db = None
        cursor = None
        try:
           db = pymysql.connect(host=DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
           cur = db.cursor()
           sql = 'Delete from patient where patientID = %s'
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

    def showFeedBack(self):
        db = None
        cursor = None
        try:

            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            print("here")
            sql = 'Select pName, pEmail, subject, message from patient'
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
            db = pymysql.connect(host=DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            print("here")
            sql = 'Select * from stock'
            cur.execute(sql)
            result = cur.fetchall()

        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return result


    def validateStaff(self,id,password):
        db = None
        valid = False
        try:
            db = pymysql.connect(host=self.DATABASE_IP,port=3306,user=self.DB_USER,password=self.DB_PASSWORD,database=self.DATABASE)
            cur = db.cursor()
            sql = 'select sPassword from staff where staffID=%s'
            args = (id)
            done = cur.execute(sql,args)
            tuple = cur.fetchone()
            passwd = tuple[0]
            if done:
                if password == passwd :
                    valid =True
        except Exception as e:
            print(e)
            print('error in validate staff')
        finally:
            if db != None:
                db.commit()
        return valid

    def validatePatient(self,id,password):
        db = None
        valid = False
        try:
            db = pymysql.connect(host=self.DATABASE_IP,port=3306,user=self.DB_USER,password=self.DB_PASSWORD,database=self.DATABASE)
            cur = db.cursor()
            sql = 'select pPassword from patient where patientID=%s'
            args = (id)
            done = cur.execute(sql,args)
            tuple = cur.fetchone()
            if tuple:
                passwd = tuple[0]
            if done:
                if password == passwd :
                    valid =True
        except Exception as e:
            print(e)
            print('error in validate patient')
        finally:
            if db != None:
                db.commit()
        return valid

    def checkAdmin(self,id):
        db = None
        valid = False
        try:
            db = pymysql.connect(host=self.DATABASE_IP,port=3306,user=self.DB_USER,password=self.DB_PASSWORD,database=self.DATABASE)
            cur = db.cursor()
            sql = 'select designation from staff where staffID=%s'
            args = (id)
            done = cur.execute(sql,args)
            tuple = cur.fetchone()
            designation = tuple[0]
            if done:
                if designation == 'admin' :
                    valid =True
        except Exception as e:
            print(e)
            print('error in check admin')
        finally:
            if db != None:
                db.commit()
        return valid

    def insertPatient(self, name, dob, cnic, gender, country, city, state, streetNo, houseNo, email, phoneNo):
        # id,name,birthdate,cnic,gender,country,city,state,streetNo,house no,email,password,phone number,subject,message
        db = None
        cursor = None
        insert = False
        try:
            print("Inserting patient")
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            p_id = 'pt' + get_random_Numeric_string()
            print(p_id)
            session["p_id"] = p_id
            reportID = 'rep' + get_random_Numeric_string(7)
            print(reportID)
            session["reportID"] = reportID
            password = get_random_alphaNumeric_string()
            print(password)
            sql = 'Insert into patient (patientID,pName,pBirthdate,pCNIC,pGender,pCountry,pCity,pState,pStreetNo,pHouseNo,pEmail,pPassword,pPhoneNo) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            args = (p_id, name, dob, cnic, gender, country, city, state, streetNo, houseNo, email, password, phoneNo)
            cur.execute(sql, args)
            insert = True
        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return insert

    def getStaffData(self, staff_ID):
        db = None
        cursor = None
        valid = False
        data = []
        try:
            print("Getting staff data")
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'Select * from staff where staffID = ' + '%s'
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

    def editStaffData(self, staff_ID, name, DOB, CNIC, gender, country, city, state, streetNo, houseNo, email, password,
                      phoneNo, salary):
        db = None
        cursor = None
        edited = False
        data = []
        try:
            print("editting staff data")
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'update staff set sName = ' + '%s' + ' ,sBirthdate = ' + '%s' + ', sCNIC = ' + '%s' + ', sGender = ' + '%s' + ', sCountry = ' + '%s' + ', sCity = ' + '%s' + ', sState = ' \
                  + '%s' + ', sStreetNo = ' + '%s' + ', sHouseNo = ' + '%s' + ', sEmail = ' + '%s' + ', sPassword = ' + '%s' + ', sPhoneNo = ' + '%s where staffID = ' + '%s'
            args = (
            name, DOB, CNIC, gender, country, city, state, streetNo, houseNo, email, password, phoneNo, staff_ID)
            cur.execute(sql, args)
            data = cur.fetchone()
            edited = True
        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
               db.commit()
            return edited



