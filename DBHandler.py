import pymysql

class DBHandler:
    def __init__(self,DATABASEIP,DB_USER,DB_PASSWORD,DATABASE):
        self.DATABASEIP=DATABASEIP
        self.DB_USER=DB_USER
        self.DB_PASSWORD=DB_PASSWORD
        self.DATABASE=DATABASE

    def __del__(self):
        print("Destructor")


        def insertFeedback(self, name, email, subject, message):
            db = None
            cursor = None
            insert = False
            try:
                db = pymysql.connect(host=self.DATABASEIP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                     database=self.DATABASE)
                cur = db.cursor()
                sql = 'insert into feedbacks (name,email,subject,message) values (%s,%s,%s,%s)'
                args = (name, email, subject, message)
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