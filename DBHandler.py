import pymysql

import smtplib, os
from flask import session


class DBHandler:

    def __init__(self, DATABASE_IP, DB_USER, DB_PASSWORD, DATABASE):
        self.DATABASE_IP = DATABASE_IP
        self.DB_USER = DB_USER
        self.DB_PASSWORD = DB_PASSWORD
        self.DATABASE = DATABASE

    def __del__(self):
        print("Destructor")

    def getpHistory(self, pid):

        db = None
        cursor = None
        try:
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            result = []
            print("here")
            sql = 'Select * from patient where patientID = ' + ' %s'
            args = (pid)
            cur.execute(sql, args)
            patientID, pName, pBirthdate, pCNIC, pGender, pCountry, pCity, pState, pStreetNo, pHouseNo, pEmail, pPassword, pPhoneNo = cur.fetchone();
            print("here1")
            result.append(pName)
            result.append(patientID)
            result.append(pBirthdate)
            result.append(pCNIC)
            result.append(pGender)
            result.append(pCountry)
            result.append(pCity)
            result.append(pState)
            result.append(pStreetNo)
            result.append(pHouseNo)
            result.append(pEmail)
            result.append(pPassword)
            result.append(pPhoneNo)
        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return  result


    def insertFeedback(self, id, subject, message):
        db = None
        cursor = None
        insert = False
        try:
            db = pymysql.connect(host =self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
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

    def getpReports(self, pid):
        db = None
        cursor = None
        try:
            print("DBgetALLTestReportsID")
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            result = []
            sql = 'Select reportID from report where patientID = ' + ' %s'
            args = (pid)
            cur.execute(sql, args)
            reportID = cur.fetchone();
            result = reportID
            print("DBgetALLTestReportsID")

        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return result

    def getStockQty(self):
        db = None
        cursor = None
        try:
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'select itemQuantity from stock'
            cur.execute(sql)
            result = cur.fetchall()
            return result
        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return result

    def insertStock(self):
        db = None
        cur = None
        insert = False
        try:
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)            cur = db.cursor()
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
            args = (subject, message, id)
            cur.execute(sql, args)
            insert = True

        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return insert

    def updateAdminEmail(self, id,email):
        db = None
        cursor = None
        insert = False
        try:
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'update staff set sEmail=%s where staffID=%s'
            args = (email, id)
            cur.execute(sql, args)
            insert = True

        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return insert


    def updateAdminPassword(self, id,password):
        db = None
        cursor = None
        insert = False
        try:
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'update staff set sPassword=%s where staffID=%s'
            args = (password, id)
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
        cur = None
        try:
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'select * from patient where patientID = %s'
            cur.execute(sql, (id,))
            result = cur.fetchone()
            return result[0]
        except Exception as e:
            print(e, "tu banda banja getPatientId")
        finally:
            db.commit()
            return result[0]

    def getAdminID1(self, cAEmail):
        db = None
        cur = None
        try:
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'select * from staff where sEmail = %s'
            cur.execute(sql, (cAEmail,))
            result = cur.fetchone()
        except Exception as e:
            print(e)
        finally:
            db.commit()
        return result[0]


    def getAdminID(self, cAPassword):
        db = None
        cur = None
        try:
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'select * from staff where sPassword = %s'
            cur.execute(sql, (cAPassword,))
            result = cur.fetchone()
            return result[0]
        except Exception as e:
            print(e)
        finally:
            db.commit()
            return result[0]



    def getPatientID2(self, name, email):
        db = None
        cur = None
        try:
            db = pymysql.connect(host='localhost', port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'select patientID from patient where pName=%s AND pEmail=%s'
            args = (name, email)
            cur.execute(sql, args)
            result = cur.fetchone()
        except Exception as e:
            print(e)
        finally:
            db.commit()
            return result[0]

    def getStaffID(self, id, cnic):
        db = None
        cur = None
        try:
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'select * from staff where staffID=%s AND sCNIC=%s'
            args = (id, cnic)
            cur.execute(sql, args)
            result = cur.fetchone()

        except Exception as e:
            print(e)
        finally:
            if(db!=None):
                db.commit()
                return result[0]

        '''    import mysql.connector
            from mysql.connector import Error

            try:
                connection = mysql.connector.connect(host='localhost',
                                                     database='python_db',
                                                     user='pynative',
                                                     password='pynative@#29')

                cursor = connection.cursor(prepared=True)
                sql_update_query = """UPDATE Employee set Salary = %s where Id = %s"""

                data_tuple = (12000, 1)
                cursor.execute(sql_update_query, data_tuple)
                connection.commit()
                print("Employee table updated using the prepared statement")

            except mysql.connector.Error as error:
                print("parameterized query failed {}".format(error))
            finally:
                if (connection.is_connected()):
                    cursor.close()
                    connection.close()
                    print("MySQL connection is closed")
'''

    def deleteStaff(self, id):
        db = None
        cursor = None
        delete = False
        try:
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'Delete from staff where staffID = %s'
            result = cur.execute(sql, (id,))
            delete = True
        except Exception as e:
            print(e)
            return False
        finally:
            db.commit()
            return delete

    def deletePatient(self, id):
        db = None
        cursor = None
        delete = False
        try:
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'DELETE FROM patient WHERE patientID = %s'
            cur.execute(sql, (id,))
            delete = True
        except Exception as e:
            print(e)
            print("some error")
        finally:
            db.commit()
            return delete

    def deleteReport(self, id, reportID):
        db = None
        cursor = None
        deleteR = False
        try:
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'DELETE FROM report WHERE patientID = %s AND reportID = %s'
            args = (id, reportID)
            cur.execute(sql, args)
            deleteR = True
        except Exception as e:
            print(e)
            print("some error")
        finally:
            db.commit()
            return deleteR

    def showFeedBack(self):
        db = None
        cursor = None
        try:
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            print("here")
            sql = 'Select pName, pEmail, subject, message from patient Where subject IS NOT NULL'
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
        result = []
        try:
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
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

    def getTestName(self, reportid):
        db = None
        cursor = None
        tests = []
        try:
            print("DBgetTestname")
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'Select testName from testrecord where reportID = ' + ' %s'
            args = (reportid)
            cur.execute(sql, args)
            for row in cur.fetchall():
                tests.append(row[0])
            print("DBgetTestname")
        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return tests

    def getptTestReportStatus(self, testname):
        db = None
        try:
            print("DBHandlergetptTestReportStatus")
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            print("Gussa na ker bhai chalja")
            sql = """Select status from testrecord where testName = %s"""
            print("Gussa na ker bhai chalja")
            args = (testname)
            cur.execute(sql, args)
            print("Gussa na ker bhai chalja")
            result = cur.fetchone()
            print("Gussa na ker bhai chalja")
            print(result)
            print("DBHandlergetptTestReportStatus1")
        except Exception as e:
            print(e, "bhai chal jaldi")
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return result

    def validateStaff(self, id, password):
        db = None
        valid = False
        try:
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, password=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'select sPassword from staff where staffID=%s'
            args = (id)
            done = cur.execute(sql, args)
            tuple = cur.fetchone()
            passwd = tuple[0]
            if done:
                if password == passwd:
                    valid = True
        except Exception as e:
            print(e)
            print('error in validate staff')
        finally:
            if db != None:
                db.commit()
        return valid

    def validatePatient(self, id, password):
        db = None
        valid = False
        try:
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, password=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'select pPassword from patient where patientID=%s'
            args = (id)
            done = cur.execute(sql, args)
            tuple = cur.fetchone()
            if tuple:
                passwd = tuple[0]
            if done:
                if password == passwd:
                    valid = True
        except Exception as e:
            print(e)
            print('error in validate patient')
        finally:
            if db != None:
                db.commit()
        return valid

    def checkAdmin(self, id):
        db = None
        valid = False
        try:
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, password=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'select designation from staff where staffID=%s'
            args = (id)
            done = cur.execute(sql, args)
            tuple = cur.fetchone()
            designation = tuple[0]
            if done:
                if designation == 'admin':
                    valid = True
        except Exception as e:
            print(e)
            print('error in check admin')
        finally:
            if db != None:
                db.commit()
        return valid

    def insertPatient(self, pID, name, dob, cnic, gender, country, city, state, streetNo, houseNo, email, phoneNo,
                      password):
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
        finally:
            db.commit()
            return insert

    def getptTestReportid(self, testname):
        db = None
        cursor = None
        try:
            print("DBHandlergetptTestReportid")
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'select testRecordID from testrecord where testName=%s'
            args = (testname)
            cur.execute(sql, args)
            testRecordID = cur.fetchone()
            print("DBHandlergetptTestReportid1")
        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return testRecordID

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
            data = cur.fetchone()
            if (data != None):
                valid = True
        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return data

    def getStaffRecord(self):
        db = None
        cursor = None
        result = []
        try:
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            print("here")
            sql = 'Select * from staff'
            cur.execute(sql)
            result = cur.fetchall()
        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return result

    def viewPatientRecord(self):
        db = None
        cursor = None
        result = []
        try:
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            print("here")
            sql = 'Select * from patient'
            cur.execute(sql)
            result = cur.fetchall()
        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return result

    def getpatientreportID(self, pid):
        db = None
        try:
            print("getpatientreportID")
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            print("a gya")
            sql = "Select reportID from report where patientID = %s"
            print("a gya")
            args = (pid)
            cur.execute(sql, args)
            reportID = cur.fetchone()
            print(reportID)
        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return reportID

    def viewReports(self):
        db = None
        cursor = None
        result = []
        try:
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            print("here")
            sql = 'Select * from report'
            cur.execute(sql)
            result = cur.fetchall()
        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return result

    def getptTestReportData(self, testid):
        db = None
        cursor = None
        try:
            print("DBHandlergetptTestReportData")
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'Select * from patientReport  where testRecordID  = ' + ' %s'
            args = (testid)
            cur.execute(sql, args)
            result = []
            testRecordID, reportID, staffID, patientID, reportReceivedDate, protein, albumin, globulin, bilirubin, ast, alt, alp, rbc, wbc, platelet, hemoglobin, urea, creatinine, uricAcid = cur.fetchone();
            print("DBHandlergetptTestReportData")
            result.append(testRecordID)
            result.append(reportID)
            result.append(staffID)
            result.append(patientID)
            result.append(reportReceivedDate)
            result.append(protein)
            result.append(albumin)
            result.append(globulin)
            result.append(bilirubin)
            result.append(ast)
            result.append(alt)
            result.append(alp)
            result.append(rbc)
            result.append(wbc)
            result.append(platelet)
            result.append(hemoglobin)
            result.append(urea)
            result.append(creatinine)
            result.append(uricAcid)
            print("DBHandlergetptTestReportData1")
        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return result

    def insertReportEntry(self,reportID,pID,doctor):
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
            cur.execute(sql1, args1)
            staffID = cur.fetchone()
            print(staffID[0])

            sql = 'insert into report (reportID,patientID,staffID) values (%s,%s,%s)'
            args = (reportID,pID,staffID[0])
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

    def enterNoSamples(self,reportID):
        updated = False
        try:
            print("Entering no samples")
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql1 = 'select count(*) as totalRecords from testrecord where reportID = %s'
            args1 = (reportID)
            cur.execute(sql1,args1)
            samples = cur.fetchone()
            sql = 'update report set noFSamples = %s where reportID = %s'
            args = (samples[0],reportID)
            cur.execute(sql,args)
            updated = True
        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return updated

    def enterTestRecordReport(self,testrecordID,reportID,staffID,patientID, date, protein, albumin, globulin,bilirubin,
                              ast, alt, alp, rbc, wbc, platelet, hemoglobin, urea, creatinine,uricAcid):
        inserted = False
        try:
            print("Entering Test REcord Report")
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql1 = 'insert into patientReport values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            args1 = (testrecordID,reportID,staffID,patientID, date, protein, albumin, globulin,bilirubin,
                              ast, alt, alp, rbc, wbc, platelet, hemoglobin, urea, creatinine,uricAcid)
            cur.execute(sql1,args1)
            inserted = True
        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
        return inserted

    def updateTestRecordStatus(self,testrecordID):
        updated = False
        try:
            print("Updating testRecord status")
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'update testrecord set status = \'1\' where testRecordID = %s'
            args = (testrecordID)
            cur.execute(sql, args)
            updated = True
        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
        return updated

    def updateReport(self,reportID, pID):
        db = None
        cursor = None
        inserted = False
        payment = 0.0
        try:
            print("Updating report")
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql1 = 'select testName from testrecord where reportID = ' + '%s'
            args1 = (reportID)
            cur.execute(sql1, args1)
            result = cur.fetchall()
            print(result)
            for row in result:
                print(row[0])
                sql2 = 'select testPrice from test where testName = ' + '%s'
                args2 = (row[0])
                cur.execute(sql2, args2)
                bill = cur.fetchone()
                payment = payment + bill[0]
                print(payment)


            sql3 = 'Update report set payment = %s where reportID = %s'
            args3 = (payment, reportID)
            cur.execute(sql3,args3)

            inserted = True
        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return inserted

    def getAllTests(self):
        db = None
        cursor = None
        data = []
        try:
            print("Getting all tests")
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'Select testName from test'
            cur.execute(sql)
            data = cur.fetchall()
        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return data


    def getPatientTests(self, reportID):
        db = None
        cursor = None
        data = []
        try:
            print("Getting patient tests")
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'Select testName from testrecord where reportID = %s'
            args = (reportID)
            cur.execute(sql,args)
            data = cur.fetchall()
        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return data

    def getNewTests(self, allTests, patientTests):
        test = []
        exist = False
        for t in allTests:
            for patientT in patientTests:
                if(t == patientT):
                    exist = True
            if(exist == False):
                test.append(t)
            else:
                exist = False
        return test

    def deductStock(self, testName):
        db = None
        cursor = None
        deducted = False
        try:
            print("Deducting stock")
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            # name, price, masks, gloves, containers, swabs, syringes, glasswares, sanitizer, cotton, reagents
            sql1 = 'select noFMasks, noFGloves, noFContainers, noFSwabs, noFSyringes, noFGlassWare,noFSanitizors, noFCottonPkg, noFReagents from test where testName = ' + '%s'
            args1 = (testName)
            cur.execute(sql1, args1)
            noFMasks, noFGloves, noFContainers, noFSwabs, noFSyringes, noFGlassWare, noFSanitizors, noFCottonPkg, noFReagents = cur.fetchone()
            print(noFContainers)
            sql = 'select * from stock'
            cur.execute(sql)
            for row in cur.fetchall():
                if row[1] == 'Masks':
                    noFMasks = row[2] - noFMasks
                    sql2 = 'update stock set itemQuantity =  ' + '%s where itemName = %s'
                    args2 = (noFMasks, "Masks")
                    cur.execute(sql2, args2)
                elif row[1] == 'Gloves':
                    noFGloves = row[2] - noFGloves
                    sql2 = 'update stock set itemQuantity = ' + ' %s where itemName = %s'
                    args2 = (noFGloves, "Gloves")
                    cur.execute(sql2, args2)
                elif row[1] == 'Containers':
                    noFContainers = row[2] - noFContainers
                    sql2 = 'update stock set itemQuantity = ' + '%s where itemName = %s'
                    args2 = (noFContainers, "Containers")
                    cur.execute(sql2, args2)
                elif row[1] == 'Swabs':
                    noFSwabs = row[2] - noFSwabs
                    sql2 = 'update stock set itemQuantity = ' + '%s where itemName = %s'
                    args2 = (noFSwabs, "Swabs")
                    cur.execute(sql2, args2)
                elif row[1] == 'Syringes':
                    noFSyringes = row[2] - noFSyringes
                    sql2 = 'update stock set itemQuantity = ' + '%s where itemName = %s'
                    args2 = (noFSyringes, "Syringes")
                    cur.execute(sql2, args2)
                elif row[1] == 'Glassware':
                    noFGlassWare = row[2] - noFGlassWare
                    sql2 = 'update stock set itemQuantity = ' + '%s where itemName = %s'
                    args2 = (noFGlassWare, "Glassware")
                    cur.execute(sql2, args2)
                elif row[1] == 'Sanitizer':
                    noFSanitizors = row[2] - noFSanitizors
                    sql2 = 'update stock set itemQuantity = ' + '%s where itemName = %s'
                    args2 = (noFSanitizors, "Sanitizer")
                    cur.execute(sql2, args2)
                elif row[1] == 'Cotton':
                    noFCottonPkg = row[2] - noFCottonPkg
                    sql2 = 'update stock set itemQuantity = ' + '%s where itemName = %s'
                    args2 = (noFCottonPkg, "Cotton")
                    cur.execute(sql2, args2)
                elif row[1] == 'Reagents':
                    noFReagents = row[2] - noFReagents
                    sql2 = 'update stock set itemQuantity = ' + '%s where itemName = %s'
                    args2 = (noFReagents, "Reagents")
                    cur.execute(sql2, args2)

            if (
                    noFMasks < 40 or noFGloves < 40 or noFContainers < 40 or noFSwabs < 40 or noFSyringes < 40 or noFGlassWare < 40 or noFSanitizors < 40 or noFCottonPkg < 40 or noFReagents < 40):
                print("notify admin")
            deducted = True
        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return deducted

    def insertTestRecord(self, testRecordID, reportID, test, doctor, sampleType):
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
            cur.execute(sql1, args1)
            staffID = cur.fetchone()
            print(staffID)
            sql = 'insert into testrecord(testrecordID,reportID,testName,staffID,sampleType) values (%s,%s,%s,%s,%s)'
            args = (testRecordID,reportID,test,staffID[0],sampleType)
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

