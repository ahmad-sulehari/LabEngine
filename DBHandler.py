import pymysql
import smtplib,os


class DBHandler:
<<<<<<< HEAD
    def __init__(self, DATABASE_IP, DB_USER, DB_PASSWORD, DATABASE):
        self.DATABASE_IP = DATABASE_IP
        self.DB_USER = DB_USER
        self.DB_PASSWORD = DB_PASSWORD
        self.DATABASE = DATABASE
=======
    def __init__(self,DATABASE_IP,DB_USER,DB_PASSWORD,DATABASE):
        self.DATABASE_IP=DATABASE_IP
        self.DB_USER=DB_USER
        self.DB_PASSWORD=DB_PASSWORD
        self.DATABASE=DATABASE
>>>>>>> d15476f780dbd43d1c309ef21db9702fa8a40897

    def __del__(self):
        print("Destructor")

    def insertFeedback(self, id, subject, message):
        db = None
        cursor = None
        insert = False
        try:
            db = pymysql.connect(host='localhost', port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
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

<<<<<<< HEAD
    def getStockQty(self):
        db = None
        cursor = None
        try:
            db = pymysql.connect(host='localhost', port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
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
            db = pymysql.connect(host='localhost', port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
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


    def getPatientID(self, id):
        db = None
        cursor = None
        try:
            db = pymysql.connect(host='localhost', port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
=======
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


        def insertStock(self, mask, gloves, containers,swabs,syringes,glassware,sanitizors,cottonPkg,reagents):
            db = None
            cursor = None
            insert = False
            try:
                db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
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
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
>>>>>>> d15476f780dbd43d1c309ef21db9702fa8a40897
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
<<<<<<< HEAD
            db = pymysql.connect(host='localhost', port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
=======
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
>>>>>>> d15476f780dbd43d1c309ef21db9702fa8a40897
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
<<<<<<< HEAD
            db = pymysql.connect(host='localhost', port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
=======
            db = pymysql.connect(host=self.DATABASE_IP, port=3307, user=self.DB_USER, passwd=self.DB_PASSWORD,
>>>>>>> d15476f780dbd43d1c309ef21db9702fa8a40897
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
            db = pymysql.connect(host='localhost', port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
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
           db = pymysql.connect(host='localhost', port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
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
<<<<<<< HEAD
            db = pymysql.connect(host='localhost', port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
=======
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
>>>>>>> d15476f780dbd43d1c309ef21db9702fa8a40897
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

<<<<<<< HEAD
    def showStockView(self):
        db = None
        cursor = None
        try:
            db = pymysql.connect(host='localhost', port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
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
=======
        def showStockView(self):
            db = None
            cursor = None
            try:
                db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
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
            sql = 'select sPassword from staff where patientID=%s'
            args = (id)
            done = cur.execute(sql,args)
            tuple = cur.fetchone()
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
>>>>>>> d15476f780dbd43d1c309ef21db9702fa8a40897
