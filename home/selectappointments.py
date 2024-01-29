
import mysql.connector 
conn=mysql.connector.connect ( user='root',password='admin',database='hospital')
mycur=conn.cursor()


def selectappointments():
    mycur.execute (" SELECT a.aid,a.adate,a.atime,d.did,d.dfname,d.dlname,d.depname,d.dqual,d.dexp FROM appointmentdetails as a INNER JOIN docinfo as d ON a.did=d.did")
    a=mycur.fetchall()
    return a



def viewyourappnts(x):
    mycur.execute (" SELECT a.adate,a.atime,d.dfname,d.dlname,d.depname,d.dqual,d.dexp,ap.turn,ap.statuss FROM appointmentdetails as a INNER JOIN docinfo as d inner join appointmentSetup as ap  ON a.did=d.did and ap.aid=a.aid where ap.pid={}".format(x))
    a=mycur.fetchall()
    return a