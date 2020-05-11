import pymysql
import smtplib,os
from flask import session




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

    def insertPatient(self, pID,name, dob, cnic, gender, country, city, state, streetNo, houseNo, email, phoneNo,password):
        # id,name,birthdate,cnic,gender,country,city,state,streetNo,house no,email,password,phone number,subject,message
        db = None
        cursor = None
        insert = False
        try:
            print("Inserting patient")
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'Insert into patient (patientID,pName,pBirthdate,pCNIC,pGender,pCountry,pCity,pState,pStreetNo,pHouseNo,pEmail,pPassword,pPhoneNo) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            args = (pID, name, dob, cnic, gender, country, city, state, streetNo, houseNo, email, password, phoneNo)
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

    def insertReportEntry(self,reportID,pID,doctor,samples):
        db = None
        cursor = None
        insert = False
        try:
            print("Inserting Report entry")
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql1 = 'select staffID from staff where sName = ' + '%s'
            args1 = (doctor)
            cur.execute(sql1,args1)
            staffID = cur.fetchone()
            print(staffID[0])
            print(samples[0])
            sql = 'insert into report (reportID,patientID,staffID,noFSamples) values (%s,%s,%s,%s)'
            args = (reportID,pID,staffID[0],int(samples))
            cur.execute(sql, args)
            insert = True
            print("Report ka record insert ho gya")
        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return insert

    def deductStock(self,testName):
        db = None
        cursor = None
        deducted = False
        try:
            print("Deducting stock")
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            #name, price, masks, gloves, containers, swabs, syringes, glasswares, sanitizer, cotton, reagents
            sql1 = 'select noFMasks, noFGloves, noFContainers, noFSwabs, noFSyringes, noFGlassWare,noFSanitizors, noFCottonPkg, noFReagents from test where testName = ' + '%s'
            args1 = (testName)
            cur.execute(sql1,args1)
            noFMasks, noFGloves, noFContainers, noFSwabs, noFSyringes, noFGlassWare, noFSanitizors, noFCottonPkg, noFReagents = cur.fetchone()
            print(noFContainers)
            sql = 'select * from stock'
            cur.execute(sql)
            for row in cur.fetchall():
                if row[1] == 'Masks':
                    noFMasks = row[2] - noFMasks
                    sql2 = 'update stock set itemQuantity =  ' + '%s where itemName = %s'
                    args2 = (noFMasks,"Masks")
                    cur.execute(sql2,args2)
                elif row[1] == 'Gloves':
                    noFGloves = row[2] - noFGloves
                    sql2 = 'update stock set itemQuantity = '  + ' %s where itemName = %s'
                    args2 = (noFGloves,"Gloves")
                    cur.execute(sql2, args2)
                elif row[1] == 'Containers':
                    noFContainers = row[2] - noFContainers
                    sql2 = 'update stock set itemQuantity = ' + '%s where itemName = %s'
                    args2 = (noFContainers,"Containers")
                    cur.execute(sql2, args2)
                elif row[1] == 'Swabs':
                    noFSwabs = row[2] - noFSwabs
                    sql2 = 'update stock set itemQuantity = ' + '%s where itemName = %s'
                    args2 = (noFSwabs,"Swabs")
                    cur.execute(sql2, args2)
                elif row[1] == 'Syringes':
                    noFSyringes = row[2] - noFSyringes
                    sql2 = 'update stock set itemQuantity = ' +'%s where itemName = %s'
                    args2 = (noFSyringes,"Syringes")
                    cur.execute(sql2, args2)
                elif row[1] == 'Glassware':
                    noFGlassWare = row[2] - noFGlassWare
                    sql2 = 'update stock set itemQuantity = ' + '%s where itemName = %s'
                    args2 = (noFGlassWare,"Glassware")
                    cur.execute(sql2, args2)
                elif row[1] == 'Sanitizer':
                    noFSanitizors = row[2] - noFSanitizors
                    sql2 = 'update stock set itemQuantity = ' +  '%s where itemName = %s'
                    args2 = (noFSanitizors,"Sanitizer")
                    cur.execute(sql2, args2)
                elif row[1] == 'Cotton':
                    noFCottonPkg = row[2] - noFCottonPkg
                    sql2 = 'update stock set itemQuantity = ' + '%s where itemName = %s'
                    args2 = (noFCottonPkg ,"Cotton")
                    cur.execute(sql2, args2)
                elif row[1] == 'Reagents':
                    noFReagents = row[2] - noFReagents
                    sql2 = 'update stock set itemQuantity = ' +'%s where itemName = %s'
                    args2 = ( noFReagents ,"Reagents")
                    cur.execute(sql2, args2)

            if(noFMasks < 40 or noFGloves < 40 or noFContainers < 40 or noFSwabs < 40 or noFSyringes < 40 or noFGlassWare < 40 or noFSanitizors < 40 or noFCottonPkg < 40 or noFReagents < 40):
                print("notify admin")
            deducted = True
        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return deducted

    def insertTestRecord(self,testRecordID,reportID,test,doctor,sampleType):
        db = None
        cursor = None
        insert = False
        try:
            print("Inserting Test record")
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql1 = 'select staffID from staff where sName = ' + '%s'
            args1 = (doctor)
            cur.execute(sql1,args1)
            staffID = cur.fetchone()
            print(staffID)
            sql = 'insert into testrecord(testrecordID,reportID,testName,staffID,sampleType) values (%s,%s,%s,%s,%s)'
            args = (testRecordID,reportID,test,staffID,sampleType)
            cur.execute(sql, args)
            insert = True
        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return insert


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



