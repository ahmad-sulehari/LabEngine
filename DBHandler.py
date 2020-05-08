import pymysql

class DBHandler:
    def __init__(self,DATABASEIP , DB_USER , DB_PASSWORD , DATABASE):
        self.DATABASEIP = DATABASEIP
        self.DB_USER = DB_USER
        self.DB_PASSWORD = DB_PASSWORD
        self.DATABASE = DATABASE

    def  __del__(self):
        print("Destructor")

    def getpHistory(self, pid):

        db = None
        cursor = None
        try:
            db = pymysql.connect(self.DATABASEIP, self.DB_USER, self.DB_PASSWORD, self.DATABASE)
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
            db = pymysql.connect(self.DATABASEIP, self.DB_USER, self.DB_PASSWORD, self.DATABASE)
            cur = db.cursor()
            result = []
            print("here")
            sql = 'Select reportID from report where patientID = ' + ' %s'
            args = (pid)
            cur.execute(sql,args)
            patientID, pName, pBirthdate, pCNIC, pGender, pCountry, pCity, pState, pStreetNo, pHouseNo, pEmail, pPassword, pPhoneNo = cur.fetchone();
            print("here1")


        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return result



def Test():
    db = DBHandler("localhost", "root", "jimin123", "labengine")
    mylist = db.showWorkers("test")
    for i in mylist:
        print(i)

if __name__ == '__main__':
    Test()

