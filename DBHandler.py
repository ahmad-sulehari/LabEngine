import pymysql

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