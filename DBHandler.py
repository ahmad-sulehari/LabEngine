import pymysql
from flask import session
class DBHandler:
    def __init__(self,DATABASE_IP , DB_USER , DB_PASSWORD , DATABASE):
        self.DATABASE_IP = DATABASE_IP
        self.DB_USER = DB_USER
        self.DB_PASSWORD = DB_PASSWORD
        self.DATABASE = DATABASE

    def  __del__(self):
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
            cur.execute(sql,args)
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
            return result


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
            cur.execute(sql,args)
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
            cur.execute(sql,args)
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
        result = None
        try:
            print("DBHandlergetptTestReportStatus")
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            print("Gussa na ker bhai chalja")
            sql = """Select status from testrecord where testName = %s"""
            print("Gussa na ker bhai chalja")
            args = (testname)
            cur.execute(sql, (args,))
            print("Gussa na ker bhai chalja")
            result = cur.fetchone()
            print("Gussa na ker bhai chalja")
            print(result)
            print("DBHandlergetptTestReportStatus1")
        except Exception as e:
            print(e,"bhai chal jaldi")
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return result

    def getptTestReportid(self, testname):
        db = None
        cursor = None
        try:
            print("DBHandlergetptTestReportid")
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor(prepared = True)
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


