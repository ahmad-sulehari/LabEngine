import pymysql
import smtplib,os
class DBHandler:
    def __init__(self,DATABASE_IP , DB_USER , DB_PASSWORD , DATABASE):
        self.DATABASE_IP = DATABASE_IP
        self.DB_USER = DB_USER
        self.DB_PASSWORD = DB_PASSWORD
        self.DATABASE = DATABASE


    def register(self, fname, lname, gender, birthdate, phoneNo, email, bloodGroup, country, province, city, password):
        db=None
        insert=False
        try:
            db=pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, password=self.DB_PASSWORD, database=self.DATABASE)
            cur=db.cursor()
            sql = 'INSERT INTO donors (fname,lname,birthDate,gender,phoneNo,email,bloodGroup,country,province,city,password)' \
                  ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            args = (fname, lname, birthdate, gender, phoneNo, email, bloodGroup, country, province, city, password)
            done=cur.execute(sql, args)
            if done:
                insert = True

        except Exception as e:
            print(e)
            print("some error")
        finally:
            if(db!=None):
                db.commit()
        return insert

    def checkEmail(self,email):
        db=None
        check=False
        try:
            db=pymysql.connect(host=self.DATABASE_IP,port=3306,user=self.DB_USER,password=self.DB_PASSWORD,database=self.DATABASE)
            cur=db.cursor()
            sql = 'Select email from donors'
            value = cur.execute(sql)
            check_email = cur.fetchall()
            for i in range(0, value):
                if email == check_email[i][0]:
                    check=True
        except Exception as e:
            print(e)
            print("some error")
        finally:
            if db != None:
                db.commit()
        return check

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

    def checksignin(self,email,password):
        db=None
        check=False
        try:
            db=pymysql.connect(host=self.DATABASE_IP,port=3306,user=self.DB_USER,password=self.DB_PASSWORD,database=self.DATABASE)
            cur=db.cursor()
            sql = 'Select password from donors where email=%s'
            args = (email)
            done=cur.execute(sql, args)
            tuple=cur.fetchone()
            password1=tuple[0]
            if done:
                if(password==password1):
                    check=True
        except Exception as e:
            print(e)
            print("some error")
        finally:
            if db != None:
                db.commit()
        return check

    def statusUpdate(self,email,status):
        db=None
        insert=False
        try:
            db = pymysql.connect(host="localhost", port=3306, user="root", password="1209348756", database="project")
            cur = db.cursor()
            sql = 'Update donors set status=%s where email=%s'
            args = (status,email)
            done=cur.execute(sql, args)
            if done:
                insert = True
        except Exception as e:
            print(e)
            print("some error")
        finally:
            if db != None:
                db.commit()
        return insert


    def checkrequestblood(self,bloodGroup,country,city):
        db=None
        try:
            db=pymysql.connect(host=self.DATABASE_IP,port=3306,user=self.DB_USER,password=self.DB_PASSWORD,database=self.DATABASE)
            cur=db.cursor()
            status='True'
            sql = 'Select email from donors where bloodGroup=%s and country=%s and city=%s and status=%s'
            args = (bloodGroup,country,city,status)
            done=cur.execute(sql, args)
            if done:
                email = cur.fetchall()
                data=[email,done]
                return data
        except Exception as e:
            print(e)
            print("some error")
        finally:
            if db != None:
                db.commit()


    def updateSuccess(self,email,data_update,data_check):
        db= None
        insert=False
        try:
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            if(data_check=='phoneNo'):
                sql = 'Update donors set phoneNo=%s where email=%s'
                args = (data_update,email)
                done = cur.execute(sql, args)
                if(done>0):
                    insert = True
            # if(data_check=='email'):
            #     sql = 'Update donors set email=%s where email=%s'
            #     args = (data_update,email)
            #     done = cur.execute(sql, args)
            #     if(done>0):
            #         insert = True
            if(data_check=='country'):
                sql = 'Update donors set country=%s where email=%s'
                args = (data_update,email)
                done = cur.execute(sql, args)
                if(done>0):
                    insert = True
            if(data_check=='province'):
                sql = 'Update donors set province=%s where email=%s'
                args = (data_update,email)
                done = cur.execute(sql, args)
                if(done>0):
                    insert = True
            if(data_check=='city'):
                sql = 'Update donors set city=%s where email=%s'
                args = (data_update,email)
                done = cur.execute(sql, args)
                if(done>0):
                    insert = True
            if (data_check == 'password'):
                sql = 'Update donors set password=%s where email=%s'
                args = (data_update, email)
                done = cur.execute(sql, args)
                if(done>0):
                    insert = True
        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
        return insert


    def showDonorsData(self,email):
        db = None
        try:
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, password=self.DB_PASSWORD, database=self.DATABASE)
            cur = db.cursor()
            sql = 'Select fname,lname,Birthdate,gender,phoneNo,email,bloodGroup,country,province,city,status ' \
                  'from donors where email=%s'
            args = (email)
            done=cur.execute(sql, args)
            if(done>0):
                row=cur.fetchall()
                donor = row[0][2]

                donorData=[row[0][0] +" " +row[0][1]+'&'+row[0][3]+'&'+ row[0][4]+'&'+ row[0][5]+'&'+ row[0][6]+'&'
                           + row[0][7]+'&'+ row[0][8]+'&'+ row[0][9]+'&'+ row[0][10]+'&'+donor.strftime('%m/%d/%Y')]
                return donorData

        except Exception as e:
            print(e)
            print("some error")
        finally:
            if(db!=None):
                db.commit()

    def getRecords(self):
        db = None
        try:
            db = pymysql.Connect(host = self.DATABASE_IP, port = 3306, user = self.DB_USER, password = self.DB_PASSWORD, database = self.DATABASE)
            cur = db.cursor()
            sql = 'select * from donors'
            done = cur.execute(sql)
            if done>0:
                data = cur.fetchall()
                return data
        except Exception as e:
            print(e)
        finally:
            if db!=None:
                db.commit()

    # def filterRecords(self,city,bloodgroup):
    #     db = None
    #     try:
    #         db = pymysql.Connect(host = self.DATABASE_IP, port = 3306, user = self.DB_USER, password = self.DB_PASSWORD, database = self.DATABASE)
    #         cur = db.cursor()
    #         if city and bloodgroup!=None and bloodgroup!='ALL':
    #             sql = 'select * from donors where city=%s AND bloodGroup = %s '
    #             args = (city,bloodgroup)
    #             done = cur.execute(sql,args)
    #         elif city and bloodgroup =='ALL' or bloodgroup == None:
    #             sql = 'select * from donors where city=%s'
    #             args = (city)
    #             done = cur.execute(sql,args)
    #         elif city == None and bloodgroup != 'ALL' and bloodgroup != None:
    #             sql = 'select * from donors where bloodGroup=%s'
    #             args = (bloodgroup)
    #             done = cur.execute(sql, args)
    #         else:
    #             sql = 'select * from donors'
    #             done = cur.execute(sql)
    #         if done > 0:
    #             data = cur.fetchall()
    #             return data
    #
    #     except Exception as e:
    #         print(e)
    #     finally:
    #         if db!=None:
    #             db.commit()
    #


    def delete(self,email):
        db=None
        insert=False
        try:
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'delete from donors where email=%s'
            args = email
            done=cur.execute(sql, args)
            if(done>0):
                insert = True
                # email_passwd = os.getenv('BDMS_MAIL_PASSWORD')
                # my_email = os.getenv('BDMS_EMAIL')
                # with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                #     smtp.starttls()
                #     smtp.login(my_email, email_passwd)
                #     subject = "Account Termination Successful"
                #     body = "Your account has been terminated.\n\n\n\n\n\n\nRegards:BDMS Team"
                #     msg = f'Subject: {subject}\n\n{body}'
                #     smtp.sendmail(my_email, email, msg)
        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
        return insert


